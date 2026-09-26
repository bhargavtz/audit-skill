# audit-skill

**A Claude skill for structured codebase and AI system prompt audits.**

Use it to produce evidence-based reviews of:
- **Codebases** — build/runtime behavior, UI, accessibility, performance, security, privacy, and test coverage.
- **AI system prompts** — intent, prompt quality, bottlenecks, structural gaps, scaling risks, and durable recommendations.

Every audit should distinguish observed evidence from assumptions, state limitations, redact sensitive data, and avoid applying changes without explicit approval.

---

## What It Does

### Codebase Audit
Given a repo URL, ZIP, or pasted code, Claude will:
- Attempt to build and run the project
- Crawl all routes and execute critical user flows
- Find UI layout bugs across Desktop / Tablet / Mobile viewports
- Detect functional bugs with reproduction steps + HTTP logs
- Run WCAG 2.1 accessibility checks
- Identify performance bottlenecks (bundle size, LCP, FCP, etc.)
- Find security vulnerabilities (XSS, CSRF, secrets in repo, CVEs)
- Identify test coverage gaps and generate missing tests
- Produce copy-paste ready code patches for every Critical/High issue
- Generate a 2-week sprint plan

### System Prompt Audit
Given a set of AI agent system prompts, Claude will:
- Determine the system's **true functional intent** (not just stated purpose)
- Score every prompt out of 100 across 7 dimensions
- Identify bottlenecks causing quality failures or silent errors
- Find missing agent roles (Critic, Reconciler, Context Manager, etc.)
- Project future failure risks with timelines
- Recommend **permanent, structural fixes** (not wording tweaks)
- Produce machine-readable JSON summary for automation

---

## Installation

### Option 1: Claude.ai / Claude App (Recommended)

1. Download `audit-skill.skill` from [Releases](../../releases)
2. In Claude settings → Skills → Install from file
3. Upload `audit-skill.skill`

### Option 2: Manual Install (Claude Computer Use)

```bash
# Clone this repo
git clone https://github.com/bhargavtz/audit-skill.git

# Copy to your skills directory
cp -r audit-skill /path/to/your/skills/

# Structure should be:
# /your-skills/
#   audit-skill/
#     SKILL.md
#     docs/
#       references/
#       examples/
#       assets/
```

Then point your Claude Computer Use setup to your skills directory.

### Option 3: Claude Code

```bash
# Add to your Claude Code skills path
git clone https://github.com/bhargavtz/audit-skill.git ~/.claude/skills/audit-skill
```

---

## Usage

Once installed, just describe what you want audited:

### Codebase Audit
```
Audit this repo: https://github.com/example/my-app
Build command: npm install && npm run build
Start command: npm run dev
Critical flows: login, checkout, admin dashboard
Test at: Chrome desktop 1366×768, mobile 375×812
```

```
Here's my React component code, find all bugs and accessibility issues: [paste code]
```

### System Prompt Audit
```
Audit all my system prompts. Here are my agents: [paste prompts]
```

```
Review my AI pipeline system prompts and tell me what will break at scale
```

### Combined Audit
```
Do a full audit of my AI-powered code generation platform:
- Repo: https://github.com/example/codegen-platform
- System prompts: [paste or upload]
```

---

## Output Format

Every audit produces:

| Output | Description |
|--------|-------------|
| 📋 Executive Summary | Top 5 findings + business impact + remediation roadmap |
| 🔧 Technical Appendix | Per-issue detail with file refs, line numbers, reproduction steps |
| 🩹 Code Patches | Copy-paste ready diffs for Critical/High issues |
| 🤖 CI Config | GitHub Actions workflows to prevent regressions |
| 📅 Sprint Plan | 2-week remediation roadmap |
| 📊 JSON Summary | Machine-readable findings for automation |

---

## Skill Structure

```text
audit-skill/
├── SKILL.md                          # Main skill file (Claude reads this)
├── README.md                         # Project overview and usage
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── docs/
    ├── references/
    │   ├── codebase-audit.md            # Full codebase audit instructions
    │   ├── prompt-audit.md              # Full system prompt audit instructions
    │   └── json-schema.md               # JSON output schemas
    ├── examples/
    │   ├── codebase-report.md           # Example codebase audit output
    │   └── prompt-report.md             # Example system prompt audit output
    └── assets/
        └── trigger-eval.json            # Trigger evaluation queries
```

---

## Severity Levels

| Level | Definition |
|-------|-----------|
| 🔴 Critical | Data loss, security breach, system down, blocks all users |
| 🟠 High | Major feature broken, significant UX failure, exploitable vuln |
| 🟡 Medium | Degraded UX, minor data issue, non-critical bug |
| 🔵 Low | Polish, minor inconsistency, nice-to-have improvement |

---

## Prompt Quality Scoring (System Prompt Audits)

Each prompt scored out of 100:

| Dimension | Weight |
|-----------|--------|
| Instruction Clarity | 20% |
| Role Precision | 15% |
| Constraint Completeness | 15% |
| Output Schema Definition | 15% |
| Inter-Agent Alignment | 15% |
| Hallucination Resistance | 10% |
| Scalability | 10% |

---

## Requirements

- Claude Computer Use access (claude.ai Pro/Team/Enterprise, or Claude API with computer use)
- For live codebase audits: Node.js, Python, or relevant runtime in the computer use environment
- For static analysis: No additional requirements — Claude analyzes pasted/uploaded code directly

---

## Contributing

Issues and PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

No repository-wide open-source license is currently verified in this checkout. Do not assume the repository is licensed for reuse unless the maintainer confirms licensing authority and adds an appropriate license.
