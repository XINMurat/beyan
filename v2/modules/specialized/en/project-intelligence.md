# Module: Project Intelligence

**Priority**: P0 (Meta-Orchestrator Module)
**Tokens**: ~5000
**Analysis Time**: First phase (Discovery Phase)

---

## Purpose
This module serves as the "brain" of the system. It analyzes the overall structure, technology stack, maturity level, and architectural drift of the target project, and guides which specialized modules should be loaded for the analysis.

---

## Project Type and Tech Stack Detection

```yaml
project_type_heuristics:
  web_frontend:
    indicators: ["package.json", "src/App.js", "src/App.tsx", "index.html", "next.config.js", "vite.config.js"]
    confidence: High
  api_backend:
    indicators: ["requirements.txt", "Pipfile", "pom.xml", "build.gradle", "go.mod", "src/main.rs", ".csproj"]
    confidence: High
  mobile_app:
    indicators: ["android/app/build.gradle", "ios/Podfile", "pubspec.yaml", "app.json"]
    confidence: High
  data_ml_pipeline:
    indicators: ["jupyter", ".ipynb", "dbt_project.yml", "airflow", "dag", "mlflow"]
    confidence: Medium
  devops_infra:
    indicators: ["Dockerfile", "docker-compose.yml", "kubernetes", ".tf", "terraform", "ansible"]
    confidence: High
  blockchain_web3:
    indicators: ["hardhat.config.js", "truffle-config.js", "*.sol", "Anchor.toml"]
    confidence: High
```

### Maturity Level Detection

```yaml
maturity_levels:
  Early_Stage:
    characteristics: "No or very minimal README, test files (0-10% coverage), single branch, no CI/CD."
    recommendation: "Recommend basic file structure, linting, and minimal test infrastructure."
  Growing:
    characteristics: "README present, basic CI (e.g. GitHub Actions lint/build), some tests (10-40% coverage)."
    recommendation: "Advanced testing, CI/CD optimization, and architectural pattern consolidation."
  Mature:
    characteristics: "Detailed documentation, Semantic Versioning, full CI/CD, high test coverage (>70%), staging environments."
    recommendation: "Performance audits, security reviews, and edge case scenario analysis."
  Production_Ready:
    characteristics: "Monitoring/Observability, SLA/SLO documentation, Incident Management processes."
    recommendation: "Focus on resilience, load testing, and cost optimization."
```

---

## Module Recommendation Matrix

```yaml
recommendation_matrix:
  web_frontend + mature:
    always: [file_structure, security_analysis, performance_analysis, ui_ux_analysis]
    likely: [accessibility_analysis, api_design_analysis, i18n]
    optional: [seo, analytics]

  api_backend + production:
    always: [security_analysis, api_design_analysis, database_analysis, performance_analysis]
    likely: [testing_strategy, resilience_analysis]
    optional: [developer_experience, monitoring_observability]

  blockchain_web3 + early:
    always: [smart_contract_security, gas_optimization]
    likely: [file_structure]
    optional: []
```

---

## Special Case Detection

When any of the following conditions are detected, actions beyond normal module selection are required:

```yaml
special_cases:
  migration_in_progress:
    signal: "Both old and new system present in the same repository"
    action: "Mandatory: load legacy-migration module"

  security_critical:
    signal: "Health, finance, authentication, or cryptography components"
    action: "Load security-audit module at P0 priority"

  public_api:
    signal: "API exposed to multiple external consumers"
    action: "Add api-audit module"

  docs_only_system:
    signal: "Repository contains only .md files"
    action: "Load meta-analysis module"

  research_plus_production:
    signal: "Both research and production components in the same repo"
    action: "Load ai-research + web-mobile modules in parallel"

  very_early_stage:
    signal: "No README or fewer than 5 lines, no test files"
    action: "Run scoring-criteria first for overall health score, deep analysis after"

  monorepo:
    signal: "Multiple independent projects in a single repository"
    action: "Apply the Monorepo Decision Tree below"
```

---

## Monorepo Decision Tree

When a single Git repository contains multiple independent projects or services:

```
How many independent projects are in this repo?
│
├── 2-3 projects
│     → Generate a separate triage report for each
│     → Select modules separately for each sub-project
│     → Output: docs/triage/[project-name]_report.md (one per project)
│
├── 4+ projects
│     → First define scope: which sub-projects are the target of this analysis?
│     │
│     ├── All  → Separate triage report for each
│     │         → Shared top-level navigation: docs/index.md
│     │
│     └── Selected  → Triage only the targeted ones
│                   → Document the others as "out of scope"
│
└── Shared library / infrastructure component present?
      Yes → Document this shared component separately
           → Reference it in dependent project analyses
           → Evaluate the impact of shared component changes on all dependent projects
```

**Monorepo Special Scoring:**
- Each sub-project receives its own health score
- A P0 finding in a shared component → all dependent project scores are **automatically capped at 6.5**
- `docs/monorepo_summary.md` aggregates all sub-project scores

---

## Drift Detection (Vision vs. Reality)

If the developer has documented their intended architecture (in `ARCHITECTURE.md` or README), the AI should compare it against what is actually in the code and compute a "Drift Score."

*   **Example Drift:** README claims "Microservices" but the code is a single monolith.
*   **Example Drift:** "Clean Architecture" targeted but database SQL calls are made directly inside UI components.

---

## Scoring

```yaml
scoring:
  excellent: "Project type is clear, maturity is production-level, drift score 0-5% (plan and code aligned)."
  good: "Project is understandable, growing/mature maturity, minor architectural deviations."
  attention: "Multiple tech stacks mixed together, early maturity, obvious gap between vision and code."
  critical: "No discernible tech pattern in codebase, zero documentation, drift score >50%."
```

---

## Output Format

```markdown
## 🧠 Project Intelligence & Discovery

- **Project Type:** [e.g., React/Node.js Fullstack Web App]
- **Maturity Level:** [e.g., Growing]
- **Estimated Bus Factor Risk:** [Low / Medium / High]

### 🎯 Drift Analysis
- **Vision:** [Architecture claimed in documentation]
- **Reality:** [Actual state in the code]
- **Drift Estimate:** % [Estimated] - [Findings]

### 📦 Recommended Next Analysis Modules
*   `[Module 1]`: [Why it was recommended]
*   `[Module 2]`: [Why it was recommended]
```
