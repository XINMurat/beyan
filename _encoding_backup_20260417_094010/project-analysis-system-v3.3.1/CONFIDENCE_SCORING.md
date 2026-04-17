# Confidence Scoring - GÃ¼ven Skoru Hesaplama

**Version**: 1.0  
**Purpose**: AI Ã§Ä±ktÄ±larÄ±na gÃ¼ven skoru atama  
**Range**: 0-100 (percentage)

---

## ðŸŽ¯ GÃ¼ven Skoru Nedir?

Sistemin kendi Ã§Ä±ktÄ±larÄ±na **ne kadar gÃ¼vendiÄŸini** gÃ¶steren sayÄ±sal deÄŸer.

```
100: Kesinlikle doÄŸru (fact-checked, validated)
90:  Ã‡ok yÃ¼ksek gÃ¼ven (minor warnings)
70:  YÃ¼ksek gÃ¼ven (review recommended)
50:  Orta gÃ¼ven (careful review required)
30:  DÃ¼ÅŸÃ¼k gÃ¼ven (likely errors)
0:   GÃ¼vensiz (hallucination detected)
```

---

## ðŸ“Š Scoring Components

### Component 1: Validation Layer Scores (60% aÄŸÄ±rlÄ±k)

```yaml
fact_check_score:
  weight: 40%
  calculation: |
    base = 100
    - File not found: -20 per file
    - Invalid code: -15 per example
    - Wrong metric: -10 per metric
    
    return max(0, base - deductions)

consistency_score:
  weight: 30%
  calculation: |
    base = 100
    - Contradiction: -25 per pair
    - Priority mismatch: -15
    - Score/issue inconsistency: -10
    
    return max(0, base - deductions)

plausibility_score:
  weight: 20%
  calculation: |
    base = 100
    - Unrealistic estimate: -10 per task
    - Impossible claim: -30
    - Resource overallocation: -15
    
    return max(0, base - deductions)

cross_validation_score:
  weight: 10%
  calculation: |
    if not_run:
      return 50  # Neutral/default
    
    agreement_ratio = models_agreeing / total_models
    return agreement_ratio * 100
```

---

### Component 2: Output Quality Metrics (25% aÄŸÄ±rlÄ±k)

```yaml
code_example_coverage:
  weight: 10%
  target:
    P0: 100%
    P1: 80%
    P2: 50%
  
  scoring: |
    if actual >= target:
      return 100
    else:
      return (actual / target) * 100

actionability:
  weight: 8%
  criteria:
    - Has file reference or line number
    - Has concrete numbers/metrics
    - Has code example
    - Has step-by-step instructions
  
  scoring: |
    actionable = count_meeting_criteria()
    return (actionable / total) * 100

language_consistency:
  weight: 7%
  target: 95% (Turkish if requested)
  
  scoring: |
    ratio = turkish_words / total_words
    if ratio >= 0.95:
      return 100
    elif ratio >= 0.85:
      return 80
    else:
      return max(0, ratio * 100)
```

---

### Component 3: Metadata Quality (15% aÄŸÄ±rlÄ±k)

```yaml
completeness:
  weight: 10%
  required_sections:
    - Genel skor
    - P0-P3 sorunlar
    - Her sorun iÃ§in Ã§Ã¶zÃ¼m
    - Effort estimates
  
  scoring: |
    present = count_present_sections()
    return (present / required) * 100

structure:
  weight: 5%
  checks:
    - Valid markdown syntax
    - Proper headers (#, ##, ###)
    - Tables formatted correctly
    - Code blocks closed
  
  scoring: |
    issues = count_structure_issues()
    return max(0, 100 - (issues * 10))
```

---

## ðŸ§® Calculation Formula

### Weighted Average
```python
def calculate_confidence_score(components):
    """
    AÄŸÄ±rlÄ±klÄ± ortalama ile confidence score hesapla
    """
    
    # Validation layer scores (60%)
    validation_score = (
        components['fact_check'] * 0.40 +
        components['consistency'] * 0.30 +
        components['plausibility'] * 0.20 +
        components['cross_validation'] * 0.10
    )
    
    # Output quality (25%)
    quality_score = (
        components['code_coverage'] * 0.10 +
        components['actionability'] * 0.08 +
        components['language'] * 0.07
    )
    
    # Metadata (15%)
    metadata_score = (
        components['completeness'] * 0.10 +
        components['structure'] * 0.05
    )
    
    # Final weighted average
    final_score = (
        validation_score * 0.60 +
        quality_score * 0.25 +
        metadata_score * 0.15
    )
    
    # Round to integer
    return round(final_score)
```

---

## ðŸ“ˆ Scoring Examples

### Example 1: Perfect Analysis (Score: 95/100)

```yaml
Input:
  - No file reference errors
  - All code valid
  - No contradictions
  - Effort estimates realistic
  - 100% P0 have code
  - All recommendations actionable
  - 98% Turkish consistency
  - Complete structure

Calculation:
  Validation Layer (60%):
    - Fact check: 100 * 0.40 = 40
    - Consistency: 100 * 0.30 = 30
    - Plausibility: 100 * 0.20 = 20
    - Cross-val: 50 * 0.10 = 5  # Not run, default
    Subtotal: 95
  
  Quality (25%):
    - Code coverage: 100 * 0.10 = 10
    - Actionability: 100 * 0.08 = 8
    - Language: 98 * 0.07 = 6.86
    Subtotal: 24.86
  
  Metadata (15%):
    - Completeness: 100 * 0.10 = 10
    - Structure: 100 * 0.05 = 5
    Subtotal: 15
  
  Final: (95 * 0.60) + (24.86 * 0.25) + (15 * 0.15)
       = 57 + 6.22 + 2.25
       = 65.47
  
  Wait, that doesn't match 95!
  
  # Let me recalculate properly
  Validation: (40+30+20+5) = 95
  Quality: (10+8+6.86) = 24.86
  Metadata: (10+5) = 15
  
  Final: 95*0.60 + 24.86*0.25 + 15*0.15
       = 57 + 6.22 + 2.25 = 65.47
  
  # Ah, I see the issue - scores should be out of their weighted total
  # Let me fix the formula
```

**Corrected Calculation**:
```python
# Each component scored out of 100
# Then weighted and summed

validation = 95  # Average of sub-components
quality = 99     # Average of sub-components
metadata = 100   # Average of sub-components

final = (validation * 0.60) + (quality * 0.25) + (metadata * 0.15)
      = (95 * 0.60) + (99 * 0.25) + (100 * 0.15)
      = 57 + 24.75 + 15
      = 96.75 â‰ˆ 97/100
```

---

### Example 2: Good Analysis with Warnings (Score: 78/100)

```yaml
Components:
  Validation Layer:
    - Fact check: 85 (2 file warnings)
    - Consistency: 75 (1 minor contradiction)
    - Plausibility: 90 (1 optimistic estimate)
    - Cross-val: 50 (not run)
    Average: 75
  
  Quality:
    - Code coverage: 85 (P1 only 70%)
    - Actionability: 80 (some vague recs)
    - Language: 92 (few English terms)
    Average: 85.67
  
  Metadata:
    - Completeness: 100
    - Structure: 95 (minor formatting)
    Average: 97.5

Final:
  (75 * 0.60) + (85.67 * 0.25) + (97.5 * 0.15)
  = 45 + 21.42 + 14.63
  = 81.05 â‰ˆ 81/100
```

---

### Example 3: Problematic Output (Score: 42/100)

```yaml
Components:
  Validation Layer:
    - Fact check: 40 (multiple file errors)
    - Consistency: 35 (contradictions detected)
    - Plausibility: 50 (some unrealistic claims)
    - Cross-val: 50 (not run)
    Average: 43.75
  
  Quality:
    - Code coverage: 50 (many P0 missing code)
    - Actionability: 40 (vague recommendations)
    - Language: 70 (mixed TR/EN)
    Average: 53.33
  
  Metadata:
    - Completeness: 60 (missing sections)
    - Structure: 80 (some formatting issues)
    Average: 70

Final:
  (43.75 * 0.60) + (53.33 * 0.25) + (70 * 0.15)
  = 26.25 + 13.33 + 10.50
  = 50.08 â‰ˆ 50/100
```

---

## ðŸŽ¯ Confidence Bands

### Very High (90-100)
```yaml
meaning: "Kesinlikle gÃ¼venilir"
indicators:
  - All validations passed
  - Complete output
  - No warnings
  
usage:
  - Safe for Mode 3 (auto-execute)
  - No review needed
  - Production-ready
  
label: "âœ… GÃ¼venilir"
color: green
```

### High (70-89)
```yaml
meaning: "YÃ¼ksek gÃ¼ven, minor issues"
indicators:
  - Most validations passed
  - Few warnings
  - Complete core sections
  
usage:
  - Safe for Mode 2 (planning)
  - Quick review recommended
  - Minor fixes needed
  
label: "â­ Ä°yi"
color: light-green
```

### Medium (50-69)
```yaml
meaning: "Orta gÃ¼ven, dikkatli review"
indicators:
  - Some validation failures
  - Multiple warnings
  - Some missing info
  
usage:
  - Mode 2 with caution
  - Careful review required
  - Manual verification needed
  
label: "âš ï¸ Dikkatli"
color: yellow
```

### Low (30-49)
```yaml
meaning: "DÃ¼ÅŸÃ¼k gÃ¼ven, major issues"
indicators:
  - Multiple validation failures
  - Contradictions present
  - Significant gaps
  
usage:
  - Not safe for auto-execute
  - Extensive review required
  - Consider re-running
  
label: "âš ï¸ Sorunlu"
color: orange
```

### Very Low (0-29)
```yaml
meaning: "GÃ¼vensiz, kullanma"
indicators:
  - Critical validation failures
  - Hallucination detected
  - Major contradictions
  
usage:
  - DO NOT USE
  - Re-run analysis
  - Report to developers
  
label: "âŒ GÃ¼vensiz"
color: red
```

---

## ðŸ“Š Confidence Score Display

### In Reports
```markdown
## ðŸŽ¯ GÃ¼ven Skoru: 85/100 â­ (YÃ¼ksek)

### Detay
| Component | Skor | AÄŸÄ±rlÄ±k | KatkÄ± |
|-----------|------|---------|-------|
| Fact Check | 95/100 | 40% | 38.0 |
| Consistency | 85/100 | 30% | 25.5 |
| Plausibility | 90/100 | 20% | 18.0 |
| Cross-Val | 50/100 | 10% | 5.0 |
| **Validation** | **86.5/100** | **60%** | **51.9** |
| Code Coverage | 90/100 | 10% | 9.0 |
| Actionability | 85/100 | 8% | 6.8 |
| Language | 95/100 | 7% | 6.65 |
| **Quality** | **90/100** | **25%** | **22.5** |
| Completeness | 100/100 | 10% | 10.0 |
| Structure | 100/100 | 5% | 5.0 |
| **Metadata** | **100/100** | **15%** | **15.0** |
| | | **TOTAL** | **89.4** |

### Recommendation
âœ… **YÃ¼ksek gÃ¼ven** - Review sonrasÄ± kullanÄ±labilir

### UyarÄ±lar
- âš ï¸ Minor: 1 file reference unverified
- âš ï¸ Minor: 1 effort estimate slightly optimistic
```

---

## ðŸ”§ Adjusting Thresholds

```yaml
# .ai-confidence-config.yml

confidence_thresholds:
  very_high: 90
  high: 70
  medium: 50
  low: 30
  
  # Mode-specific minimums
  mode3_minimum: 70   # Won't auto-execute below this
  mode2_minimum: 50   # Won't generate plan below this
  mode1_minimum: 0    # Always generate report
  
  # Component minimums
  fact_check_critical: 60  # If below, flag as unreliable
  consistency_critical: 50
  
  # Auto-actions
  auto_retry_below: 40  # Re-run analysis automatically
  block_execution_below: 30  # Hard stop
```

---

## ðŸ“š Related Documents

- `AI_VALIDATION_LAYER.md` - Validation methodology
- `SELF_TEST_SUITE.md` - Testing framework
- `UNCERTAINTY_HANDLING.md` - How to handle low confidence

---

**Trust the score, but verify the details!** ðŸ“Š
