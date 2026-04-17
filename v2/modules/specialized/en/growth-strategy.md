# Module: Growth Strategy & Module Governance

**Priority**: P3 (Framework Governance)
**Tokens**: ~2000
**Analysis Time**: Manual trigger — when adding new modules or during periodic review

---

## Purpose
This module defines how Beyan v2.0 grows and governs itself. It standardizes when and how new analysis modules are added, how existing modules are updated, and how the system is periodically reviewed for health and coverage.

---

## Current System Structure

```
CORE MODULES (23)                  DOMAIN MODULES (7)
├── security-analysis              ├── web-mobile
├── performance-analysis           ├── ai-research
├── file-structure-analysis        ├── devops-infra
├── code-quality-patterns          ├── os-firmware
├── database-analysis              ├── blockchain-web3
├── scoring-criteria               ├── data-pipeline
└── ... (17 more)                  └── legacy-migration

FOCUS MODULES (4)                 SPECIALIZED MODULES (10)
├── api-audit                      ├── project-intelligence
├── security-audit                 ├── react-typescript
├── performance-audit              ├── dotnet-core
└── compliance-audit               └── ... (7 more)

TESTING MODULES (3)               GUIDE MODULES (4)
├── test-generation                ├── accessibility-fixes
├── collaboration-test             ├── security-fixes
└── ui-interaction-test            └── ... (2 more)
```

---

## When to Add a New Module?

Before adding a module, answer these three questions:

**1. Is this genuinely a new domain?**
If it doesn't fit any existing module's scope, a new module is needed.
- *Example:* "Game engine analysis" → Doesn't fit existing modules → add `game-engine.md`.

**2. Or is adding a section to an existing module sufficient?**
If the scope is small, add a sub-section to the existing module.
- *Example:* "CLI tool support" → A note in `developer-experience.md` is enough.

**3. Or is this a horizontal focus lens?**
Applicable to all project types, not tied to one domain?
- *Example:* "Accessibility audit" → Belongs in the `focus/` category.

---

## New Module Writing Standard

Every new module must include this structure:

```markdown
# Module: [Module Name]

**Priority**: [P0/P1/P2/P3]
**Tokens**: [Estimated token count]
**Analysis Time**: [When it loads]

---

## Purpose
[Single paragraph describing what it does]

---

## [Main Content Sections]
...

---

## Scoring
[excellent/good/attention/critical levels]

---

## Output Format
[Expected report format from the AI]
```

### Mandatory Rules
- ❌ No placeholder content — every example must be real and filled
- ❌ No project name or person name in the module title
- ✅ Both `tr/` and `en/` versions must be written simultaneously
- ✅ Module must be added to `MANIFEST.yaml` before it's available to the system

---

## Existing Module Update Rules

### When to Update?
- Ecosystem change (e.g., React 19 new Hook rules)
- Regulation change (e.g., GDPR/KVKK update)
- Gap or error discovered in real-world usage
- Periodic review (6-month cycle)

### Update Procedure
1. Open the relevant module file
2. Make changes
3. Run `verify_integrity.ps1` to confirm system integrity
4. Update MANIFEST version note if it's a structural change

---

## Periodic Review Cycle

### Triggers
- After 5+ new modules added
- When a significant gap is found in real project analysis
- 6 months have elapsed (time-based)

### Review Steps
```yaml
review_steps:
  1: "Inspect MANIFEST.yaml — any stubs remaining?"
  2: "Run verify_integrity.ps1 — zero errors target"
  3: "Check token budget — any module combinations exceed 35,000?"
  4: "Update 'Known Gaps' table in this module"
```

---

## Known Gaps and Future Modules

The following areas are intentionally deferred:

| Missing Area | Priority | Trigger Condition |
|---|---|---|
| Game / Game Engine Analysis Module | Low | Game project analysis request |
| Hardware / FPGA Analysis Module | Low | Hardware project analysis request |
| Microservices-specific Module | Medium | Existing modules found insufficient |
| Accessibility Focus Audit Module | Low | Public sector or healthcare project |
| GraphQL API Design Module | Medium | GraphQL project analysis request |

---

## Scoring

```yaml
scoring:
  excellent: "MANIFEST in sync, zero stubs, all modules have EN/TR, token budget efficient."
  good: "Most modules complete, 1-2 stubs, budget manageable."
  attention: "5+ stubs, MANIFEST drifting from physical files."
  critical: "MANIFEST fully desynchronized, half of modules are stubs, system produces unreliable output."
```
