# audit-skill

**A Claude skill for structured codebase and AI system prompt audits.**

Use it to produce evidence-based reviews of:
- **Codebase Audit** — With a supplied repository and authorized tools, attempt builds, run tests, inspect routes/flows, review UI/accessibility/performance/security, and report what was actually tested. Browser, network, live-server, and dependency checks may be **Blocked** when the environment lacks access.
- **System Prompt Audit** — Analyze supplied prompts and observable outputs/traces for intent, quality, bottlenecks, structural gaps, and risks. It does not request hidden reasoning or invent behavioral metrics.

The skill produces findings and proposed remediation. It does not silently edit the target project.

---

## What It Does

### Codebase Audit
Given a repo URL, ZIP, or pasted code, and subject to environment/access limits, the skill can:
- Attempt authorized builds and tests in a safe environment
- Inventory routes and execute user-approved critical flows
- Inspect UI layout across Desktop / Tablet / Mobile viewports when browser tooling is available
- Report functional bugs with safe reproduction steps and redacted evidence
- Review accessibility, performance, dependencies, security/privacy and test coverage
- Propose missing tests and patches for Critical/High issues; apply nothing silently
- Produce a prioritized remediation plan when the evidence supports one

Unavailable browser, network, credentials, dependency, or runtime checks are reported as Blocked—not passed.

### System Prompt Audit
Given a set of AI agent system prompts and, when available, observable outputs/traces, the skill can:
- Determine stated vs. observable functional intent
- Score prompts with evidence and limitations
- Identify bottlenecks, missing roles, fallback gaps and schema risks
- Project qualitative future-risk scenarios with assumptions and validation signals
- Recommend structural fixes and produce machine-readable JSON
- Avoid hidden-reasoning requests and invented metrics

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

Every audit produces an evidence-labeled report, not an automatic promise of a patch:

| Output | Requirement |
|--------|-------------|
| Executive Summary | Top findings, impact, severity, confidence, and evidence level |
| Scope and Limitations | Target revision, tools/commands, unavailable or unauthorized checks |
| Baseline/Verification | Before-vs-after table when files changed; Passed/Failed/Blocked status |
| Technical Findings | Location, safe reproduction, evidence, impact, fix, regression test |
| Remediation Plan | Containment, minimal fix, hardening, tradeoffs; do not apply silently |
| JSON Summary | Follow `docs/references/json-schema.md`; redact sensitive data |

For a file-change or fix request, also follow [`docs/references/change-verification-loop.md`](docs/references/change-verification-loop.md).

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
