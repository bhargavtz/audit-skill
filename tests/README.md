# audit-skill Self-Validation

The repository now validates its own skill contract with a dependency-free unittest module. This checks:

- frontmatter and core safety/change-loop sections;
- required references and examples;
- trigger fixture shape and positive/negative balance;
- documentation schema examples for obvious secret literals;
- evidence, redaction and limitation requirements.

Run:

```bash
python3 -m unittest tests.test_audit_skill_contract -v
```

These tests validate the skill package itself. They do not claim that a target repository is secure, accessible, performant, or bug-free.
