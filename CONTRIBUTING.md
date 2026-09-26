# Contributing to audit-skill

Thanks for improving audit-skill. Contributions should make audit results more accurate, reproducible, safe, or easier to consume.

## Good contributions

- Fix inaccurate or ambiguous audit guidance.
- Add checks with commands or manual steps that can be independently verified.
- Improve the JSON schema or examples without breaking existing fields.
- Add representative trigger-evaluation cases, including non-triggering cases.
- Improve documentation, accessibility, or safety guidance.

## Workflow

1. Fork the repository and create a focused branch.
2. Make the smallest change that addresses the issue.
3. Update related references or examples when behavior or output changes.
4. Validate JSON and Markdown links/structure locally.
5. Open a pull request describing the problem, the change, and validation performed.

## Content guidelines

- Do not include secrets, credentials, personal data, or proprietary audit material.
- Do not present an unverified claim as an observed finding.
- Keep recommendations actionable and distinguish evidence, assumptions, and limitations.
- For new audit checks, document what to check, how to check it, what to report, and an example finding.
- Preserve the existing JSON field names unless a compatibility impact is explicitly documented.

## Pull requests

A useful pull request includes:

- a concise problem statement;
- the files and behavior affected;
- examples when output changes; and
- validation commands and their results.

Maintainers may request revisions to improve evidence, scope, safety, or compatibility.

## Reporting issues

For general bugs or documentation issues, open a GitHub issue with:

- the request or input that exposed the problem;
- the relevant output, with sensitive values removed;
- the expected behavior; and
- the model/runtime context when it materially affects the result.

For suspected security vulnerabilities, follow [`SECURITY.md`](SECURITY.md) instead of posting details publicly.
