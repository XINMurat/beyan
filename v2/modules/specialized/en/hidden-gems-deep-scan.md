# Module: Hidden Gems & Deep Scan

**Priority**: P1 (Code Maintenance & Tech Debt)
**Tokens**: ~2500
**Analysis Time**: Autonomous (runs when full file tree is scanned)

---

## Purpose
Surfaces zombie (unused) code, high bus factor knowledge silo risks, hidden technical debt, and brilliantly written code (hidden gems) that even the developers may have forgotten about.

---

## Zombie Code Detection

As projects grow, forgotten code accumulates:

1. **Never-called functions:** Files that are exported but never imported.
2. **Dead imports:** Libraries imported at the top but never used in the file.
3. **Feature flag graveyard:** Dead code blocks hidden behind disabled feature toggles.

**Detection Tools:** `ts-prune` (TypeScript), `deadcode` (Go), `vulture` (Python), uncovered areas in coverage reports.

---

## Bus Factor Analysis

The bus factor measures: "If the one person who knows this code gets hit by a bus (or resigns), can the project survive?"

```yaml
bus_factor:
  critical: "1 — A single person holds all knowledge of a critical module. Departure = crisis."
  low: "2-3 — Risk exists but is manageable with knowledge shared across a few people."
  healthy: "4+ — Knowledge is distributed across the team."

how_to_measure:
  - "git log --author analysis to find commit concentration"
  - "Files touched by only 1 contributor in the past 6 months"
  - "Who last modified the most complex/critical files?"
```

---

## Technical Debt Detection

Technical debt is not just "bad code" — it's hidden future cost:

1. **Comment Density:** How prevalent are `TODO`, `FIXME`, `HACK` comments?
2. **Cyclomatic Complexity:** Deep if-else pyramids and nested loops (spaghetti code).
3. **Duplicate Code:** Copy-paste violations of the DRY principle.

---

## Hidden Dependencies

1. **Circular Dependencies:** Module A calls B, B calls C, C calls A.
2. **Implicit Global State:** Multiple functions mutating the same global variable silently.
3. **Undocumented Side Effects:** A function named `getAmount` that also updates the database.

---

## Hidden Gems

The AI should not only find problems — it should also recognize brilliance. If there is an elegantly written, cleverly optimized, or unusually robust section of code, it should be flagged as a "Gem" and marked for documentation.

---

## Scoring

```yaml
scoring:
  excellent: "No zombie code, bus factor > 3, minimal tech debt, dependencies isolated."
  good: "Minor TODOs, some files owned by one person but overall structure is solid."
  attention: "Excessive copy-paste, HACK comments everywhere, circular dependency signals."
  critical: ">30% of code is dead, bus factor 1 (entire project depends on one person)."
```

---

## Output Format

```markdown
## 🕵️‍♂️ Deep Scan & Technical Debt Report

### 🧟 Zombie Code
*   `[File Path]`: [Unused function or import]

### 🚌 Bus Factor Analysis
*   **Current Status:** [Critical / Low / Healthy]
*   **High-Risk Files:** [Critical files touched by only 1 person]

### ⚠️ Hidden Tech Debt & Dependencies
*   [TODO/FIXME list or side effect warnings]

### 💎 Hidden Gems (Brilliantly Written Code)
*   `[Function or File]`: [Why this code deserves recognition]
```
