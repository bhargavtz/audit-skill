"""Dependency-free contract tests for audit-skill documentation and fixtures."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AuditSkillContractTests(unittest.TestCase):
    def test_skill_safety_loop_and_references(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertIn("## Safety contract", skill)
        self.assertIn("## Change-verification loop", skill)
        self.assertIn("Evidence levels", skill)
        for relative in (
            "docs/references/codebase-audit.md",
            "docs/references/prompt-audit.md",
            "docs/references/change-verification-loop.md",
            "docs/references/json-schema.md",
            "docs/examples/codebase-report.md",
            "docs/examples/prompt-report.md",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_trigger_fixture_shape_and_balance(self):
        data = json.loads((ROOT / "docs/assets/trigger-eval.json").read_text(encoding="utf-8"))
        self.assertIsInstance(data, list)
        self.assertTrue(data)
        self.assertTrue(all(set(item) == {"query", "should_trigger"} for item in data))
        positives = sum(bool(item["should_trigger"]) for item in data)
        negatives = len(data) - positives
        self.assertGreaterEqual(positives, 5)
        self.assertGreaterEqual(negatives, 5)

    def test_documented_json_examples_are_secret_free(self):
        text = (ROOT / "docs/references/json-schema.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(text.count("```json"), 2)
        self.assertIsNone(re.search(r"AIza[0-9A-Za-z_-]{20,}", text))
        self.assertIsNone(re.search(r"(?:sk|ghp)_[A-Za-z0-9]{20,}", text))

    def test_references_require_evidence_redaction_and_uncertainty(self):
        codebase = (ROOT / "docs/references/codebase-audit.md").read_text(encoding="utf-8").lower()
        prompts = (ROOT / "docs/references/prompt-audit.md").read_text(encoding="utf-8").lower()
        for term in ("redact", "limitation", "evidence"):
            self.assertIn(term, codebase)
        self.assertIn("limitation", prompts)
        self.assertIn("confidence", prompts)


if __name__ == "__main__":
    unittest.main(verbosity=2)
