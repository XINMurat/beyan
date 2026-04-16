# Beyan — Growth Strategy & Contribution Standards

> **Last Updated:** 2026-04-16

## Current Family Structure

```
PROJECT-TYPE BASED (7)          FOCUS-BASED (4)
├── application_analysis         ├── security_audit
├── os_system_analysis           ├── performance_audit
├── research_ai_analysis         ├── api_design_audit
├── data_analytics_analysis      └── compliance_audit
├── infrastructure_devops
├── legacy_migration             SPECIAL (1)
└── blockchain_analysis          └── meta_audit

CROSS-CUTTING TOOLS (2)         ENTRY POINT (1)
├── remediation_plan             └── triage_routing
└── health_score
```

**Total: 15 active prompts + 3 archived**

## When to Add a New Prompt?

1. **Is it truly a new type?** If it doesn't fit into any existing prompt scope, a new prompt is needed.
2. **Or is it a focus-based addition?** If it requires a specific lens independent of project type, use a focus-based prompt.
3. **Or is adding a section to an existing prompt enough?** If scope is small, add a subsection rather than a new file.

## New Prompt Writing Standards

Every new prompt must include:

1. Title + update tracking header (`Last Updated`, `Update Trigger`, `Next Review`)
2. Role Definition
3. Descriptive/Evaluative layer table (if applicable)
4. Core Rules (no-placeholder rule, language standard, analysis order)
5. Phase 0: Pre-Flight Scan
6. Descriptive phases (system-specific)
7. `— EVALUATIVE LAYER —` section break
8. Evaluative phases (**completeness audit mandatory**)
9. Output File System (with `docs/[directory]/` path)
10. Quality Checklist (minimum 6 items)

**Mandatory output files** for every project-type prompt:
- `completeness_report.md`
- `system_taxonomy.md`
- `index.md` (always last)

**Forbidden patterns:**
- Project names, person names, or proprietary technology names in titles
- Placeholder content without `[fill for your system]` notes
- "Optional" label except on the final phase

## Version Management

- **Minor update** (content added, no structural change): update `Last Updated` field only
- **Patch** (wording fix, table addition): update `Last Updated`, keep version number
- **Major version** (structural change, new phases, new output files): increment version (`v1.0 → v2.0`)

On major version change: keep old file with `DEPRECATED` warning, don't delete.

## Review Cycle Triggers

- New project type need emerges
- Regulation or ecosystem major change
- After 5+ new prompts added
- Structural issue detected during real-world application
