# Module: Feature Gap Analysis

**Priority**: P2
**Tokens**: ~2000
**Analysis Time**: Manual trigger or when competitor/roadmap keywords detected

---

## Purpose
Systematically identifies missing features compared to competitors or market standards, prioritized using the RICE scoring framework.

---

## Competitor Feature Matrix

```yaml
evaluation_criteria:
  - "Core Feature (Essential functionality)"
  - "UX Quality"
  - "API / Integration Capability"
  - "Pricing Model"
  - "Support & Documentation"
scoring: "1 (Missing) — 5 (Superior)"
```

## RICE Prioritization Score

```
RICE Score = (Reach × Impact × Confidence) / Effort

Reach:      How many users does this affect? (1-1000)
Impact:     How much will it matter? (0.25 / 0.5 / 1 / 2 / 3)
Confidence: How sure are we? (100% / 80% / 50%)
Effort:     Development time in person-months
```

## Output Format

```markdown
## 📊 Feature Gap Analysis

### Competitor Comparison Matrix
| Feature | This Project | Competitor A | Competitor B | Priority |
|---------|-------------|-------------|-------------|---------|
| [Feature] | ❌ | ✅ | ✅ | HIGH |

### Critical Gaps (Address Immediately)
- **[Feature name]:** [Competitor has it, we don't — RICE: X]

### Roadmap Recommendation
- Q1: [Highest RICE score feature]
- Q2: [Second priority]
```
