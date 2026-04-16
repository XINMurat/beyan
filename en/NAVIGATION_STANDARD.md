# Beyan — Navigation & Directory Standard

> **Last Updated:** 2026-04-16

---

## Output Directory Reference Card

Each prompt writes to its own subdirectory. When multiple prompts are run on the same project, these directories sit side by side under the project's `docs/` folder:

| Prompt | Output Directory |
|---|---|
| Application, OS, Research, Data, DevOps Analysis | `docs/analysis/` |
| Security Audit | `docs/security-audit/` |
| API Design Audit | `docs/api-audit/` |
| Legacy / Migration | `docs/migration-analysis/` |
| Performance Audit | `docs/performance-audit/` |
| Compliance Audit | `docs/compliance-audit/` |
| Blockchain Audit | `docs/blockchain-audit/` |
| Meta Audit | `docs/meta-analysis/` |
| Triage | `docs/triage/` |
| Remediation Plan | `docs/remediation/` |
| Health Score | `docs/health-score/` |

---

## Multi-Prompt Project Structure

When multiple prompts are run on the same project, create a top-level `docs/index.md` to tie everything together:

```
your-project/
└── docs/
    ├── index.md                    ← Master navigation (create manually)
    ├── triage/
    │   └── triage_report.md
    ├── analysis/
    │   └── index.md  ...
    ├── security-audit/
    │   └── index.md  ...
    ├── performance-audit/
    │   └── index.md  ...
    ├── remediation/
    │   └── ...
    └── health-score/
        └── ...
```

### Top-Level `docs/index.md` Template

```markdown
# [Project Name] — Analysis Hub
**Last Updated:** [Date]
**Prompts Applied:** [Which prompts were run]

---

## Triage
- [Triage Report](triage/triage_report.md)

## Descriptive Analyses
- [Technical Analysis](analysis/index.md)
- [Security Audit](security-audit/index.md) *(if applicable)*
- [Performance Audit](performance-audit/index.md) *(if applicable)*
- [API Audit](api-audit/index.md) *(if applicable)*
- [Compliance Audit](compliance-audit/index.md) *(if applicable)*

## Evaluative Synthesis
- [Remediation Plan](remediation/index.md)
- [Health Score](health-score/index.md)
```

---

## Remediation Plan Feed Guide

The Remediation Plan Generator expects outputs from various prompts. Mapping:

| Source Prompt | Key Output File | Feed to Remediation Plan |
|---|---|---|
| All analysis prompts | `completeness_report.md` | ✅ Always |
| Security Audit | `risk_matrix.md` | ✅ |
| All analysis prompts | `fragility_report.md` | ✅ If present |
| Legacy / Migration | `gap_analysis.md` | ✅ |
| Meta Audit | `gap_and_conflict_analysis.md` | ✅ |
| All prompts | `tech_debt_audit.md` | ✅ If present |
