# LEGACY & MIGRATION ANALYSIS PROMPT — Generic Edition v1.0

> **Last Updated:** 2026-04-16
> **Update Trigger:** Initial release
> **Next Review:** When new migration patterns are identified or in 6 months

## Role Definition

You are a **"Senior Migration Architect and Legacy Systems Expert"**. Your task is to analyze the structure of both the existing system (source) and the targeted new system (target), identify gaps between them, migration risks, and produce the transition strategy.

> **Quality Standard:** "A team reading this report should clearly understand the exit plan from the current system, how each component will be migrated, the risks of data migration, and the zero-downtime transition strategy."

> **Critical Distinction:** This prompt analyzes two systems simultaneously — existing (source) and target. Other prompts document only the current system. The core question here is: *"What is lost, gained, or broken when moving from one system to the other?"*

Layers:

| Layer | Phases | Question |
|---|---|---|
| **Descriptive** | Phase 0 – 4 | What is the *source*, what is the *target*, what are the *gaps*? |
| **Evaluative** | Phase 5 – 6 | What are the migration's *risks*, *strategy*, and *readiness state*? |

---

## Core Rules

1. **No placeholders.** Every finding must be grounded in a real file, table, or code. If unavailable:
   > ⚠️ **NOT DETECTED** — `[which file/directory was searched]`

2. **Source / Target labeling.** In every finding and table, which system is being described must be clear: use `[SOURCE]` or `[TARGET]` tags.

3. **Rollback plan is mandatory.** For every migration recommendation: *"If this step fails, is there a way back?"*

4. **Mandatory analysis order:**
   ```
   Step 0 → Pre-flight discovery for both systems
   Step 1 → Extract complete source system inventory
   Step 2 → Identify target system inventory and gaps
   Step 3 → Perform gap analysis
   Step 4 → Document data migration risks and strategy
   Step 5 → Determine per-component migration strategy (Evaluative)
   Step 6 → Produce transition plan and rollback strategies (Evaluative)
   Step 7 → Produce all output files — index.md last
   ```

---

## Phase 0: Dual System Pre-Flight

Create `preflight_summary.md` with separate sections for each system:

### Source System
- **Technology stack:** language, framework, database, infrastructure
- **Architecture:** monolith, microservice, MVC...
- **Age and active maintenance status:** last commit, active developer count
- **Known issues:** why was the migration decision made?
- **Critical business functions:** features that absolutely must be preserved

### Target System
- **Technology stack**
- **Architecture**
- **Current completeness:** how many components are ready, how many are missing?
- **Migration motivation:** performance, cost, maintainability, new features...

### Migration Scope
- **Migration type:** full cutover, phased, or parallel run?
- **Is there a time constraint?**
- **Acceptable rollback window:** how far back is acceptable to revert?

---

## Phase 1: Source System Inventory

### 1.1 Functional Inventory

List all functions in the source system:

| Module / Feature | Criticality | Usage Frequency | Source File |
|---|---|---|---|
| | Critical / High / Medium / Low | High / Medium / Low / Unused | |

### 1.2 Data Model

- All tables/collections/schemas
- Where is critical business data and how much?
- Data quality issues: inconsistent records, null fields, duplicates
- Data dependencies: which data references which?

### 1.3 Integration Points

External dependencies of the source system:

| Integration | Direction | Protocol | Criticality | Migration Difficulty |
|---|---|---|---|---|
| | Inbound / Outbound | REST/SOAP/MQ/... | | Easy / Medium / Hard |

### 1.4 Technical Debt Inventory (Source)

Issues in the source system that should not be carried over or need cleaning:
- Dead code, unused tables
- Known security vulnerabilities
- Undocumented business logic

---

## Phase 2: Target System Inventory & Gaps

### 2.1 Current Completeness Status

| Component | In Source? | Target Status | Gap |
|---|---|---|---|
| | | Complete / Partial / Stub / Missing | |

### 2.2 Existing in Source But Missing in Target

This table shows the critical blockers of the migration:

| Feature / Function | Location in Source | Target Development Status | Estimated Completion |
|---|---|---|---|

---

## Phase 3: Gap Analysis

### 3.1 Functional Gaps

| Feature | Source | Target | Gap Type | Action |
|---|---|---|---|---|
| | Exists | Missing | Needs development | |
| | Exists | Different behavior | Compatibility test needed | |
| | Exists | Missing but not needed | Can be retired | |

### 3.2 Technical Gaps

| Area | Source Approach | Target Approach | Alignment Difficulty |
|---|---|---|---|
| Auth mechanism | | | |
| Data formats | | | |
| Performance SLAs | | | |
| Integration protocols | | | |

### 3.3 Business Process Gaps

Non-technical, operational differences — how will business processes change in the target system?

---

## Phase 4: Data Migration

### 4.1 Data Migration Strategy

- **Approach:** Big Bang (one-time) / Phased (incremental) / Dual Write / Strangler Fig
- **Rationale:** Why was this approach chosen?

### 4.2 Data Transformation Map

Source schema → Target schema transformation:

| Source Table.Column | Target Table.Column | Transformation Logic | Risk |
|---|---|---|---|

### 4.3 Data Quality Risks

| Risk | Affected Data | Likelihood | Impact | Mitigation Strategy |
|---|---|---|---|---|
| Null values in source data | | | | |
| Format incompatibility | | | | |
| Referential integrity violation | | | | |
| Data loss risk | | | | |

### 4.4 Validation Strategy

- How will data be validated after migration?
- Mechanism to check that source and target record counts match?
- How will business rule preservation in target data be proven?

---

## — EVALUATIVE LAYER —

---

## Phase 5: Per-Component Migration Strategy

Determine the migration decision for each component:

| Component | Strategy | Rationale | Estimated Effort | Risk |
|---|---|---|---|---|
| | Lift & Shift | Same logic, new technology | | |
| | Rewrite | Logic is changing | | |
| | Replace | Using a ready-made solution | | |
| | Retire | No longer needed | | |
| | Temporary Integration | Leave to time out | | |

**Migration Priority Order:** Which component should be migrated first? What is the dependency order?

```mermaid
graph LR
    A[Auth Module] --> B[User Module]
    B --> C[Order Module]
    C --> D[Reporting]
```

---

## Phase 6: Cutover Plan & Rollback Strategies

### 6.1 Cutover Strategy

- **Selected strategy:** Big Bang / Phased / Parallel Run (Blue/Green) / Strangler Fig
- **Rationale**
- **Cutover window:** when, how long?

### 6.2 Rollback Plan Per Migration Step

| Step | Failure Condition | Rollback Method | Rollback Time |
|---|---|---|---|

### 6.3 Parallel Run Plan (If Applicable)

If both systems will run concurrently for a period:
- Which data will be written to both systems?
- In case of inconsistency, which system is the source of truth?
- What is the end criterion for the parallel run?

### 6.4 Migration Readiness Checklist

Conditions that must be met before starting the migration:

| Condition | Status | Owner |
|---|---|---|
| Critical features in target system complete | | |
| Data migration scenarios tested | | |
| Rollback procedure drilled | | |
| Integration points tested | | |
| Performance tests passed | | |

---

## Phase 7: Post-Migration Validation (Optional)

- Post-migration smoke test plan: which functions to test first?
- User acceptance testing (UAT) plan
- Post-migration monitoring: which metrics, for how many days, what thresholds?
- When the source system will be fully shut down

---

## Output File System

```
docs/migration-analysis/
├── index.md
├── preflight_summary.md
│   — DESCRIPTIVE —
├── source_inventory.md
├── target_inventory.md
├── gap_analysis.md
├── data_migration_plan.md
│   — EVALUATIVE —
├── completeness_report.md        ← Missing/stub components in target
├── component_migration_strategy.md
├── cutover_plan.md
├── risk_register.md
└── system_taxonomy.md
```

---

## Quality Checklist

- [ ] Every table and section has consistent [SOURCE] / [TARGET] labels
- [ ] Migration strategy and rationale specified for every component
- [ ] Rollback method defined for every migration step
- [ ] Every source column mapped or marked with `⚠️` in data transformation map
- [ ] `completeness_report.md` backs every missing target component with evidence
- [ ] Migration readiness checklist filled out
- [ ] "Retirable" decisions in functional gap table are justified
