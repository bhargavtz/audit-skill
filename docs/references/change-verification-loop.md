# Change Verification Loop

Use this checklist after **every file change** in an audited target project. It is designed to catch regressions introduced by the change, not to imply that every possible defect has been ruled out.

## Before changing files

- [ ] Record the target revision and clean/dirty working-tree state.
- [ ] Capture the exact proposed diff and files in scope.
- [ ] Run and record the relevant baseline checks (tests, typecheck, lint, build, security scan).
- [ ] Identify callers, dependents, routes, schemas, configuration, persistence and external integrations that may be affected.
- [ ] Confirm the user authorized modifications; otherwise provide a patch proposal only.

## After each change

1. **Review diff:** inspect the complete patch; confirm only intended files/lines changed.
2. **Static checks:** format/lint/typecheck as available; scan changed lines for secrets, unsafe deserialization, injection, unsafe shell execution and insecure defaults.
3. **Focused regression test:** add or update a test for the reported defect; run that test first.
4. **Impact tests:** run tests for affected callers/routes/schemas and related failure paths.
5. **Project checks:** run the project test suite, build, typecheck and dependency/secret checks where the environment supports them.
6. **Manual flow:** reproduce the original user flow and relevant edge/error state when the test environment allows.
7. **Compare:** baseline vs post-change, including test counts and new warnings.
8. **Report:** mark each check `Passed`, `Failed`, `Blocked`, or `Not applicable`, with command/evidence. Do not mark unavailable checks as passed.

## Stop conditions

Stop and report if:
- a new Critical/High issue or regression appears;
- a secret is found (report path/type only; never output the value);
- the fix requires production credentials, external writes, migration, deployment, or destructive actions without authorization;
- the test environment cannot distinguish the proposed fix from an existing failure.

## Completion record

```markdown
| Check | Baseline | After change | Evidence | Status |
|---|---|---|---|---|
| Focused regression test | [result] | [result] | [command/id] | Passed/Failed/Blocked |
| Related tests | [result] | [result] | [command/id] | Passed/Failed/Blocked |
| Build/type/lint | [result] | [result] | [command/id] | Passed/Failed/Blocked |
| Security checks | [result] | [result] | [tool/scope] | Passed/Findings/Blocked |
| Manual flow | [result] | [result] | [steps] | Passed/Failed/Blocked |
```
