#!/usr/bin/env python3
"""Deterministic structural checks for the v0.76 FDE design toolkit."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path


EXPECTED_SOURCE_COUNT = 68
EXPECTED_CORE_COUNT = 12
EXPECTED_DECISIONS = {"merge": 46, "handoff": 14, "drop": 8}
REQUIRED_HEADINGS = (
    "## When to use",
    "## Inputs",
    "## Output",
    "## Procedure",
    "## Acceptance gates",
    "## Do not use",
)


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_review(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return {}
    fields: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.+?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"'")
    return fields


def validate_source_bodies(
    source_root: Path, rows: list[dict[str, str]], errors: list[str]
) -> None:
    for row in rows:
        source_path = source_root / row["source_phase"] / row["source_skill"] / "SKILL.md"
        if not source_path.is_file():
            errors.append(f"missing v0.75 source body: {source_path}")
            continue
        text = source_path.read_text(encoding="utf-8")
        fields = frontmatter(text)
        if fields.get("name") != row["source_skill"]:
            errors.append(
                f"v0.75 frontmatter name mismatch: {source_path} "
                f"({fields.get('name')!r})"
            )
        if not fields.get("description"):
            errors.append(f"v0.75 missing frontmatter description: {source_path}")


def validate(root: Path, source_root: Path | None) -> list[str]:
    errors: list[str] = []
    manifest = load_json(root / "manifest.json")
    handoffs_document = load_json(root / "external-handoffs.json")
    eval_document = load_json(root / "validation" / "eval-cases.json")
    rows = load_review(root / "validation" / "v075-skill-review.csv")

    skills = manifest.get("skills", [])
    core_names = {skill.get("name") for skill in skills}
    handoff_ids = {handoff.get("id") for handoff in handoffs_document.get("handoffs", [])}
    eval_skills = eval_document.get("skills", [])

    if len(rows) != EXPECTED_SOURCE_COUNT:
        errors.append(f"source review has {len(rows)} rows; expected {EXPECTED_SOURCE_COUNT}")

    source_keys = [(row["source_phase"], row["source_skill"]) for row in rows]
    duplicates = [key for key, count in Counter(source_keys).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate source review rows: {duplicates}")

    decision_counts = Counter(row["decision"] for row in rows)
    if dict(decision_counts) != EXPECTED_DECISIONS:
        errors.append(
            f"decision counts are {dict(decision_counts)}; expected {EXPECTED_DECISIONS}"
        )

    for row in rows:
        decision = row["decision"]
        target = row["target"]
        source = f"{row['source_phase']}/{row['source_skill']}"
        if decision == "merge" and target not in core_names:
            errors.append(f"merged source targets unknown core skill: {source} -> {target}")
        elif decision == "handoff" and target not in handoff_ids:
            errors.append(f"source targets unknown handoff: {source} -> {target}")
        elif decision == "drop" and target not in {"workflow", "visual-adapter"}:
            errors.append(f"dropped source has unknown removal class: {source} -> {target}")
        elif decision not in EXPECTED_DECISIONS:
            errors.append(f"unknown decision for {source}: {decision}")

    merged_targets = {row["target"] for row in rows if row["decision"] == "merge"}
    missing_ownership = sorted(core_names - merged_targets)
    if missing_ownership:
        errors.append(f"core skills without source ownership: {missing_ownership}")

    if len(skills) != EXPECTED_CORE_COUNT:
        errors.append(f"manifest has {len(skills)} skills; expected {EXPECTED_CORE_COUNT}")
    if len(core_names) != len(skills):
        errors.append("manifest contains duplicate or missing skill names")

    eval_names = {entry.get("skill") for entry in eval_skills}
    if eval_names != core_names:
        errors.append(
            f"eval skill set differs from manifest: "
            f"missing={sorted(core_names - eval_names)}, extra={sorted(eval_names - core_names)}"
        )
    case_ids: list[str] = []
    for entry in eval_skills:
        name = entry.get("skill", "<missing-skill>")
        for case_type, minimum in (("positive", 3), ("negative", 3), ("adversarial", 1)):
            cases = entry.get(case_type, [])
            if len(cases) < minimum:
                errors.append(
                    f"{name} has {len(cases)} {case_type} cases; expected at least {minimum}"
                )
            for case in cases:
                case_id = case.get("id")
                if not case_id or not case.get("prompt"):
                    errors.append(f"{name} has incomplete {case_type} case: {case}")
                elif case_id:
                    case_ids.append(case_id)
    duplicate_case_ids = [
        case_id for case_id, count in Counter(case_ids).items() if count > 1
    ]
    if duplicate_case_ids:
        errors.append(f"duplicate eval case IDs: {duplicate_case_ids}")

    for skill in skills:
        name = skill.get("name", "<missing-name>")
        relative_path = skill.get("path")
        if not relative_path:
            errors.append(f"manifest skill has no path: {name}")
            continue
        skill_path = root / relative_path
        if not skill_path.is_file():
            errors.append(f"missing core skill body: {relative_path}")
            continue
        text = skill_path.read_text(encoding="utf-8")
        fields = frontmatter(text)
        if fields.get("name") != name:
            errors.append(
                f"frontmatter name mismatch in {relative_path}: {fields.get('name')!r}"
            )
        description = fields.get("description", "")
        if len(description) < 80:
            errors.append(f"frontmatter description is not trigger-specific: {relative_path}")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"missing {heading!r} in {relative_path}")
        if len(text.split()) < 250:
            errors.append(f"skill contract is too thin to inspect: {relative_path}")

    if source_root is not None:
        validate_source_bodies(source_root, rows, errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-root",
        type=Path,
        help="Optional path to v0.75 for source body and frontmatter checks.",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors = validate(root, args.source_root)

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    source_note = " including v0.75 bodies" if args.source_root else ""
    print(f"PASS: v0.76 deterministic package checks{source_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())