#!/usr/bin/env python3
"""Deterministic structural checks for the FDE design toolkit."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


EXPECTED_CORE_COUNT = 12
EXPECTED_HANDOFF_COUNT = 6
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


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    manifest = load_json(root / "manifest.json")
    handoffs_document = load_json(root / "external-handoffs.json")
    eval_document = load_json(root / "validation" / "eval-cases.json")
    index_text = (root / "index.md").read_text(encoding="utf-8")
    scope_text = (root / "SCOPE.md").read_text(encoding="utf-8")

    workflow_path = manifest.get("workflow")
    if not workflow_path or not (root / workflow_path).is_file():
        errors.append(f"missing workflow file: {workflow_path}")

    skills = manifest.get("skills", [])
    core_names = {skill.get("name") for skill in skills}
    handoffs = handoffs_document.get("handoffs", [])
    handoff_ids = {handoff.get("id") for handoff in handoffs}
    eval_skills = eval_document.get("skills", [])

    if len(skills) != EXPECTED_CORE_COUNT:
        errors.append(f"manifest has {len(skills)} skills; expected {EXPECTED_CORE_COUNT}")
    if len(core_names) != len(skills):
        errors.append("manifest contains duplicate or missing skill names")

    if len(handoffs) != EXPECTED_HANDOFF_COUNT or len(handoff_ids) != EXPECTED_HANDOFF_COUNT:
        errors.append(
            f"external-handoffs.json has {len(handoffs)} handoffs; expected {EXPECTED_HANDOFF_COUNT}"
        )
    for handoff in handoffs:
        hid = handoff.get("id", "<missing-id>")
        if not handoff.get("when"):
            errors.append(f"handoff {hid} missing 'when'")
        if not handoff.get("requestMustInclude"):
            errors.append(f"handoff {hid} missing 'requestMustInclude'")
        if not handoff.get("returnMustInclude"):
            errors.append(f"handoff {hid} missing 'returnMustInclude'")

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
        if relative_path not in index_text:
            errors.append(f"index.md missing skill path: {relative_path}")
        if f"`{name}`" not in scope_text:
            errors.append(f"SCOPE.md missing skill reference: {name}")
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

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: deterministic package checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())