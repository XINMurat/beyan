# Module: Scoring Criteria and Formulas

**Priority**: P0 (Core System Module)
**Tokens**: ~1500
**Analysis Time**: Automatic (after all modules complete)

---

## Purpose
Aggregates sub-scores from all analysis modules to compute the overall project health score (0–10) using a weighted average formula. Weights vary by project type, ensuring each dimension is evaluated in the appropriate context.

---

## Weight Table (By Project Type)

```yaml
weights_by_project_type:
  web_app:
    architecture: 0.20
    code_quality:  0.20
    security:      0.20
    performance:   0.15
    testing:       0.15
    documentation: 0.10

  api_backend:
    architecture: 0.25
    code_quality:  0.20
    security:      0.25
    performance:   0.15
    testing:       0.15
    documentation: 0.00

  mobile_app:
    architecture: 0.20
    code_quality:  0.20
    security:      0.15
    performance:   0.20
    testing:       0.15
    documentation: 0.10

  data_pipeline:
    architecture: 0.15
    code_quality:  0.15
    security:      0.10
    performance:   0.30
    testing:       0.20
    documentation: 0.10
```

## Calculation Formula

```
Overall Score (O) = Σ (dimension_score × dimension_weight)
Final Score       = min(10, max(0, O))
```

**Example:**
- Architecture: 8.0 × 0.20 = 1.60
- Code Quality:  7.0 × 0.20 = 1.40
- Security:      6.0 × 0.20 = 1.20
- Performance:   8.5 × 0.15 = 1.28
- Testing:       5.0 × 0.15 = 0.75
- Documentation: 7.0 × 0.10 = 0.70
- **Total: 6.93 / 10**

---

## Score Ranges and Meanings

```yaml
score_ranges:
  9.0 - 10.0:
    status: "🟢 Excellent"
    meaning: "Production-ready, minimal risk"
    action: "Periodic monitoring is sufficient"

  7.0 - 8.9:
    status: "🟡 Good"
    meaning: "A few improvement areas exist"
    action: "Address P1 issues this sprint"

  5.0 - 6.9:
    status: "🟠 Fair"
    meaning: "Issues requiring attention present"
    action: "Resolve P0 and P1 issues urgently"

  0.0 - 4.9:
    status: "🔴 Critical"
    meaning: "High risk of production issues"
    action: "Emergency intervention required, halt deployment"
```

---

## Critical Override Rules

Regardless of the overall score, the following conditions automatically cap the score:

```yaml
critical_overrides:
  any_p0_finding:
    description: "Any P0 finding present"
    cap_score_at: 6.0
    reason: "P0 = production outage or security breach risk"

  security_score_below_5:
    description: "Security score below 5"
    cap_score_at: 5.5
    reason: "Security vulnerability threatens the entire system"

  test_coverage_below_20:
    description: "Test coverage below 20%"
    deduct: 1.0
    reason: "Blind spot risk is too high"

  no_readme:
    description: "No README.md present"
    deduct: 0.5
    reason: "Onboarding is impossible"
```

---

## Output Format

```markdown
## Project Health Score: X.X / 10 [STATUS_EMOJI]

| Dimension | Score | Weight | Contribution |
|-----------|-------|--------|--------------|
| Architecture | X.X | 20% | X.XX |
| Code Quality | X.X | 20% | X.XX |
| Security | X.X | 20% | X.XX |
| Performance | X.X | 15% | X.XX |
| Testing | X.X | 15% | X.XX |
| Documentation | X.X | 10% | X.XX |
| **TOTAL** | | | **X.XX** |

[Override explanations if applicable]
```
