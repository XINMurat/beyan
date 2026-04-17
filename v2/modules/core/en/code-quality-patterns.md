# Module: Code Quality Patterns

**Priority**: P1
**Tokens**: ~2000
**Analysis Time**: Always loaded

---

## Purpose
Evaluates code readability, maintainability, SOLID principle adherence, and common antipatterns that increase long-term maintenance cost.

---

## SOLID Principles Check

```yaml
solid_checks:
  single_responsibility: "Do classes/functions do one thing only? God classes with 1000+ lines?"
  open_closed: "Can behavior be extended without modifying existing code? (Strategy pattern, plugins)"
  dependency_inversion: "Do high-level modules depend on abstractions, not concrete implementations?"
```

## Common Antipatterns

```yaml
antipatterns:
  magic_numbers:
    bad: "if (status === 3)"
    good: "if (status === OrderStatus.SHIPPED)"
  deep_nesting:
    check: "More than 3 levels of if/else/for nesting — refactor with early returns"
  long_functions:
    check: "Functions exceeding 50 lines — candidate for decomposition"
  primitive_obsession:
    check: "Passing raw strings/ints where domain objects (UserId, Email) would be clearer"
```

## Scoring

```yaml
scoring:
  excellent: "SOLID followed, no magic numbers, functions < 30 lines, clear naming."
  good: "Mostly clean, some long functions, occasional magic numbers."
  attention: "God classes, deeply nested logic, inconsistent naming conventions."
  critical: "Spaghetti code, no discernible structure, untestable monolithic functions."
```

## Output Format
```markdown
## 🧹 Code Quality Report

### SOLID Assessment: X/10
- **SRP Violations:** [List of God classes]
- **Key Antipatterns:** [Magic numbers, deep nesting counts]

### Top Refactoring Targets
1. `[File:Line]` — [Reason and suggested fix]
```
