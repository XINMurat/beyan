# Module: Testing Strategy

**Priority**: P1
**Tokens**: ~1800
**Analysis Time**: Always loaded

---

## Purpose
Evaluates the overall testing approach: test pyramid balance, CI integration, coverage targets, and test maintainability.

---

## The Testing Pyramid

```yaml
testing_pyramid:
  unit: "70% — Fast, isolated, cheap. Most tests should be here."
  integration: "20% — Services, DB connections, API contracts."
  e2e: "10% — Critical user journeys only. Slow, expensive, flaky if overused."

antipattern_ice_cream_cone:
  description: "Inverted pyramid — too many E2E, too few unit tests. Result: slow CI, flaky builds."
```

## CI/CD Integration

```yaml
ci_checks:
  pre_commit: "Linting and unit tests run on every commit?"
  pr_gate: "Tests must pass before merge? Coverage threshold enforced?"
  parallel_execution: "Tests parallelized to keep CI under 10 minutes?"
  test_reporting: "JUnit XML or similar reports for test result visualization?"
```

## Coverage Strategy

*   **Don't chase 100%:** Focus on business-critical paths, not trivial getters/setters.
*   **Branch coverage > Line coverage:** A line covered doesn't mean all conditions tested.
*   **Mutation testing:** Tools like Stryker (JS) or mutmut (Python) reveal tests that pass even when code is broken.

## Scoring

```yaml
scoring:
  excellent: "Pyramid balanced, CI gate enforced, >80% meaningful coverage, mutation testing present."
  good: "Tests exist, CI integration works, but pyramid is skewed toward E2E."
  attention: "Only happy-path tests, no CI gate, coverage < 50%."
  critical: "No tests or all tests are broken/skipped."
```
