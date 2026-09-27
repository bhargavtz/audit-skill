# audit-skill Self-Review Checklist

Use this checklist when reviewing or changing the `audit-skill` package itself. It is not a client audit report.

## Contract
- [ ] `SKILL.md` clearly separates audit mode from post-change verification.
- [ ] Missing target/scope causes an intake request, not invented findings.
- [ ] Safety rules prohibit secrets, production writes, destructive commands and unapproved target edits.
- [ ] Every finding requires evidence level, confidence, location and limitation.
- [ ] Blocked checks are not reported as passed.

## References
- [ ] Codebase reference has safe scope/intake, baseline, build/run, security/privacy, UI, accessibility and report guidance.
- [ ] Prompt reference evaluates observable prompts/outputs, not hidden reasoning.
- [ ] JSON examples include verification, evidence, confidence and limitations.
- [ ] Examples contain no realistic secrets or personal data.
- [ ] Trigger fixture includes positive and negative cases.

## Verification
```bash
python3 -m unittest tests.test_audit_skill_contract -v
git diff --check
```

For changes to this package, record baseline, inspect the diff, run the self-tests, review documentation links, run a secret-pattern scan, and obtain an independent review before pushing.
