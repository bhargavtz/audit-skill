# Contributing to audit-skill

Thanks for wanting to contribute! Here's how.

## Ways to Contribute

- **Bug reports**: Open an issue if the skill produces incorrect output or misses obvious issues
- **Audit checklist additions**: PRs adding new checks to `references/codebase-audit.md` or `references/prompt-audit.md`
- **New examples**: Add example audit reports to `examples/` for different project types
- **Better trigger eval queries**: Improve `assets/trigger-eval.json` with better edge cases

## Making Changes

1. Fork the repo
2. Create a branch: `git checkout -b my-improvement`
3. Make your changes
4. Test by using the skill on a sample codebase or set of prompts
5. Submit a PR with a clear description of what you changed and why

## Skill File Guidelines

- `SKILL.md` should stay under 500 lines
- Reference files (`references/`) can be longer — they're loaded on demand
- Every new check added to the audit references must include:
  - What to check for
  - How to check it (command, tool, or manual step)
  - What to report (format/template)
  - An example of a finding

## Reporting Issues

Please include:
- What you asked Claude to audit
- What the skill produced
- What you expected instead
- Claude model version (if known)
