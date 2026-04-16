# 🔍 Beyan — AI-Powered Systematic Project Analysis

<p align="center">
  <em>AI-Powered Systematic Project Analysis</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="version">
  <img src="https://img.shields.io/badge/prompts-15-green" alt="prompts">
  <img src="https://img.shields.io/badge/languages-TR%20%7C%20EN-orange" alt="languages">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="license">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README_TR.md">Türkçe</a>
</p>

---

A structured, battle-tested library of AI prompts for deep technical project analysis. Whether you're inheriting legacy code, conducting technical due diligence, or systematically documenting a system — Beyan gives you a complete analytical framework.

> **Core principle:** "If the engineer who built this system left tomorrow, a new developer should be able to reconstruct it entirely from the analysis output."

---

## Why Beyan?

Most prompt libraries are general-purpose. Beyan is different:

- **Type-aware:** Separate prompts for web apps, OS/firmware, AI/ML research, data pipelines, DevOps, blockchain, and more — applying the wrong prompt gives you wrong results
- **Systematic:** Every analysis follows a strict Descriptive → Evaluative two-layer structure, ending with a mandatory completeness audit
- **Hallucination-resistant:** The `NOT DETECTED` rule, the placeholder ban, and the requirement to back every finding with a real file path and line number form a constraint system that forces the LLM to flag gaps instead of filling them with invented content
- **Self-referential:** Beyan was designed, audited using its own Meta Audit prompt, improved based on the findings, and health-scored — all before the first public release. The library eats its own cooking.
- **Full pipeline:** Triage → Analysis → Remediation Plan → Health Score — every step produces structured output that feeds the next
- **Completeness detection:** Every prompt identifies stubs, orphaned components, and unfinished work — not just what's there, but what's *missing*
- **Calibrated scoring:** The Health Score prompt adapts dimension weights by project type — security weighs 25% for OS/firmware but 10% for a research model, because a single score card doesn't fit all systems

---

## Design Principles

### 1. Research Boundary ≠ Technical Debt

For research and AI/ML systems, an unimplemented component isn't always a bug — it might be an open research question deliberately left for later. Beyan distinguishes between the two with separate tables and explicit status labels (`Actively Researched` / `Deferred` / `Out of Scope`). Confusing the two produces misleading reports.

### 2. Two-Layer Analysis

Every prompt enforces a strict split:

| Layer | What It Does |
|---|---|
| **Descriptive** | Documents the system as-is — no judgment, no recommendations |
| **Evaluative** | Assesses quality, identifies gaps, produces recommendations |

The evaluative layer never begins until the descriptive layer is complete. This prevents premature conclusions from contaminating the factual record.

### 3. The NOT DETECTED Contract

If a piece of information cannot be found in the codebase, the output must say:
> ⚠️ **NOT DETECTED** — `[which file/directory was searched]`

Never guess. Never fabricate. This single rule is responsible for most of Beyan's hallucination resistance.

### 4. Self-Referential Development

Beyan v1.0 was not shipped before being analyzed by its own tools:

```
Initial design
      │
      ▼
Meta Audit prompt applied to the library itself
      │
      ▼
Findings → Remediation Plan Generator
      │
      ▼
All D-series (quick fixes) and G-series (medium improvements) applied
      │
      ▼
Health Score: 2.45 (before) → 4.75 (after)  [+71% improvement]
      │
      ▼
v1.0 shipped
```

The meta-analysis cycle is fully documented in [`tr/meta-analysis/`](tr/meta-analysis/).

---

## Prompt Family

### Entry Point
| Prompt | Purpose |
|---|---|
| [Triage & Routing](en/triage/triage_routing_prompt_v1.0.md) | Classify an unknown project and recommend which prompts to apply — always start here |

### Project-Type Prompts
| Prompt | When to Use |
|---|---|
| [Application Analysis](en/project-type/application_analysis_prompt_v2.3.md) | Web, mobile, desktop apps — includes microservice and mobile extensions |
| [OS / System Software](en/project-type/os_system_analysis_prompt_v1.0.md) | Kernels, firmware, embedded, hypervisors |
| [Research / AI-ML](en/project-type/research_ai_analysis_prompt_v1.0.md) | Experimental models, academic systems — math documentation with LaTeX + code mapping |
| [Data & Analytics](en/project-type/data_analytics_analysis_prompt_v1.0.md) | ETL, data warehouse, pipelines — silent failure detection built-in |
| [Infrastructure / DevOps](en/project-type/infrastructure_devops_prompt_v1.0.md) | IaC, CI/CD, platform engineering — drift awareness + FinOps |
| [Legacy / Migration](en/project-type/legacy_migration_prompt_v1.0.md) | Migrating from old to new systems — two-system simultaneous analysis |
| [Blockchain](en/project-type/blockchain_analysis_prompt_v1.0.md) | Smart contracts, DeFi, Web3 — immutability-aware, economic security included |

### Focus-Based Prompts (Project-Type Independent)
| Prompt | When to Use |
|---|---|
| [Security Audit](en/focus/security_audit_prompt_v1.0.md) | Deep security review, OWASP Top 10, threat modeling |
| [Performance Audit](en/focus/performance_audit_prompt_v1.0.md) | Bottleneck analysis, critical path waterfall, scalability limits |
| [API Design Audit](en/focus/api_design_audit_prompt_v1.0.md) | Contract quality, breaking change management, consumer impact |
| [Compliance Audit](en/focus/compliance_audit_prompt_v1.0.md) | GDPR, KVKK, PCI-DSS, HIPAA — personal data inventory + risk matrix |

### Cross-Cutting Tools
| Prompt | When to Use |
|---|---|
| [Remediation Plan Generator](en/cross-cutting/remediation_plan_prompt_v1.0.md) | Turn analysis findings into impact-effort matrix + sprint-ready action cards |
| [Project Health Score](en/cross-cutting/health_score_prompt_v1.0.md) | Quantify overall project health (1–5, calibrated by project type) |

### Special
| Prompt | When to Use |
|---|---|
| [Meta Audit](en/special/meta_audit_prompt_v1.0.md) | Audit the Beyan library itself — or any `.md`-based knowledge system |

---

## How It Works

```
Unknown Project
      │
      ▼
  [Triage Prompt]  ──►  triage_report.md  ──►  "Apply these prompts in this order"
      │
      ▼
[Project-Type Prompt(s)]  +  [Focus Prompt(s)]
      │
      ▼
 Structured output:
   completeness_report.md   ← what's missing
   fragility_report.md      ← what could break
   risk_matrix.md           ← what's dangerous
   ...
      │
      ├──►  [Remediation Plan]  ──►  Impact-effort matrix + sprint action cards
      └──►  [Health Score]      ──►  Calibrated 1–5 scorecard per dimension
```

---

## Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/beyan.git
   ```

2. **Open the Triage prompt** and paste it to your AI assistant along with your project's file tree / README / key files.

3. **Follow the triage output** — it tells you exactly which prompts to apply and in what order.

4. **Run the recommended prompts** and save outputs to `docs/` within your project.

5. **Optionally run** Remediation Plan + Health Score on the collected outputs.

> Works with Claude, GPT-4, Gemini, or any capable LLM.

---

## Output Structure

Each prompt produces a standardized `docs/` directory. Multiple prompts compose cleanly:

```
your-project/
└── docs/
    ├── index.md                    ← Master navigation (create manually after all prompts run)
    ├── triage/
    ├── analysis/                   ← Project-type prompts share this dir
    ├── security-audit/
    ├── performance-audit/
    ├── compliance-audit/
    ├── api-audit/
    ├── migration-analysis/
    ├── blockchain-audit/
    ├── remediation/
    └── health-score/
```

See [Navigation Standard](en/NAVIGATION_STANDARD.md) for the full multi-prompt output guide and Remediation Plan feed mapping.

---

## Languages

| Language | Status | Directory |
|---|---|---|
| 🇹🇷 Türkçe | ✅ Complete | [`tr/`](tr/) |
| 🇺🇸 English | ✅ Complete | [`en/`](en/) |

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick ways to contribute:**
- 🐛 Found an issue in a prompt? Open a bug report
- 💡 Missing a project type? Request a new prompt
- 🌍 Improve the translations
- ⭐ Star the repo to support the project

---

## License

[MIT](LICENSE) — free to use, modify, and distribute.

---

## Acknowledgements

Beyan was developed through an iterative self-referential process: designed, then audited using its own Meta Audit prompt, improved based on findings, and health-scored before release. The complete meta-analysis cycle — including all findings, the remediation plan, and the before/after health scores — is documented in [`tr/meta-analysis/`](tr/meta-analysis/).
