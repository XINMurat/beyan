# Test Scenarios - GerÃ§ek DÃ¼nya Test SenaryolarÄ±

**Version**: 1.0  
**Purpose**: Self-test suite iÃ§in Ã¶rnek test durumlarÄ±  
**Test Coverage**: Edge cases, happy paths, failure modes

---

## ðŸŽ¯ Test Scenario Types

1. **Happy Path** - Her ÅŸey doÄŸru
2. **Edge Cases** - SÄ±nÄ±r durumlarÄ±
3. **Failure Modes** - Hatalar ve kurtarma
4. **Regression** - Daha Ã¶nce dÃ¼zeltilen buglar

---

## âœ… HAPPY PATH SCENARIOS

### Scenario H-001: Perfect Analysis Report
```yaml
scenario_id: H-001
name: "MÃ¼kemmel analiz raporu"
input: perfect-analysis.md
expected_outcome: "All tests pass, confidence 95+"

test_data: |
  # Proje SaÄŸlÄ±k Raporu
  **Genel Skor**: 8.5/10 ðŸŸ¢
  
  ## P0 - Kritik Sorunlar
  
  ### 1. SQL Injection (OrderService.cs:45)
  **Risk**: YÃ¼ksek  
  **Etki**: Database security
  
  âŒ **Mevcut Kod**:
  ```csharp
  var sql = $"SELECT * FROM Orders WHERE Id = {id}";
  ```
  
  âœ… **Ã–neri**:
  ```csharp
  var order = _context.Orders.Find(id);
  ```
  
  **SÃ¼re**: 30 dakika  
  **Sorumlu**: Backend Team

validation_checks:
  - âœ… Syntax: Valid markdown
  - âœ… Content: Score in range (8.5/10)
  - âœ… Content: P0 count reasonable (1 issue)
  - âœ… Content: File reference valid
  - âœ… Logic: Concrete recommendation
  - âœ… Logic: Realistic time estimate (30min)
  - âœ… Quality: Code examples present
  - âœ… Quality: TÃ¼rkÃ§e consistent (98%)

confidence_score: 96/100
```

### Scenario H-002: Sprint Plan Generation
```yaml
scenario_id: H-002
name: "Ä°yi tasarlanmÄ±ÅŸ sprint planÄ±"
input: sprint-plan.md
expected_outcome: "No contradictions, proper ordering"

test_data: |
  # Sprint 1 Plan
  
  ## Sprint Hedefi
  P0 gÃ¼venlik sorunlarÄ±nÄ± Ã§Ã¶z
  
  | # | Task | Depends On | Effort | Owner |
  |---|------|------------|--------|-------|
  | 1 | Backup database | - | 30m | DevOps |
  | 2 | Fix SQL injection | 1 | 2h | Ali |
  | 3 | Write tests | 2 | 1h | Ali |
  | 4 | Code review | 3 | 30m | AyÅŸe |
  | 5 | Deploy to staging | 4 | 15m | DevOps |
  
  **Total**: 4h 15m

validation_checks:
  - âœ… Logic: Dependency order correct (1â†’2â†’3â†’4â†’5)
  - âœ… Logic: Backup before risky changes
  - âœ… Logic: Tests after code
  - âœ… Logic: Review before deploy
  - âœ… Resource: Ali not overallocated (3h)
  - âœ… Effort: Estimates realistic

confidence_score: 92/100
```

---

## âš ï¸ EDGE CASE SCENARIOS

### Scenario E-001: Very Large Project
```yaml
scenario_id: E-001
name: "Ã‡ok bÃ¼yÃ¼k proje (50K+ LOC)"
challenge: "Ã‡ok fazla sorun bulunabilir, priority inflation riski"

test_data: |
  Analysis Results:
  - Total Issues: 342
  - P0: 18 (5%)
  - P1: 67 (20%)
  - P2: 198 (58%)
  - P3: 59 (17%)

validation_checks:
  - âš ï¸ Content: P0 count high (18) but ratio OK (5%)
  - âœ… Content: Priority distribution reasonable
  - âš ï¸ Logic: Resource allocation check critical
  
expected_warnings:
  - "P0 count (18) above average, review priorities"
  - "Large project: Consider phased approach"

action: |
  PASS with warnings
  Suggest: Break into multiple sprints
  
confidence_score: 78/100 (warnings reduce score)
```

### Scenario E-002: No Issues Found
```yaml
scenario_id: E-002
name: "HiÃ§ sorun bulunamadÄ±"
challenge: "Suspicious - might be scanning error or perfect project"

test_data: |
  # Proje Analizi
  **Genel Skor**: 10/10 âœ…
  
  ## Bulgular
  HiÃ§bir sorun tespit edilmedi.

validation_checks:
  - âš ï¸ Content: Zero issues suspicious
  - âš ï¸ Logic: Perfect score (10/10) rare
  
expected_warnings:
  - "No issues found - verify scan completed"
  - "Consider deeper analysis with more modules"

action: |
  PASS but request verification
  Suggest: Re-run with stricter criteria
  
confidence_score: 65/100 (low confidence due to suspicion)
```

### Scenario E-003: Mixed Language Code
```yaml
scenario_id: E-003
name: "KarÄ±ÅŸÄ±k dil kullanÄ±mÄ± (TR/EN)"
challenge: "Raporun hangi dilde olmasÄ± gerektiÄŸi belirsiz"

test_data: |
  # Project Health Report
  **Overall Score**: 7.2/10
  
  ## Kritik Sorunlar
  Security issue detected in authentication...
  
  SQL Injection tespit edildi...

validation_checks:
  - âŒ Quality: Language inconsistent (50% TR, 50% EN)
  
expected_errors:
  - "Language mixing detected"
  - "Report should be consistent (Turkish or English)"

action: |
  FAIL - request re-generation
  User must specify language preference
  
confidence_score: 40/100
```

---

## âŒ FAILURE MODE SCENARIOS

### Scenario F-001: Contradictory Recommendations
```yaml
scenario_id: F-001
name: "Ã‡eliÅŸen Ã¶neriler"
input: contradictions.md
expected_outcome: "Contradiction detected, test fails"

test_data: |
  ## Ã–neriler
  
  1. **Bundle Size Azalt**
     - Lodash'Ä± kaldÄ±r
     - Moment.js'i kaldÄ±r
     - Hedef: <300KB
  
  2. **Date Handling Ä°yileÅŸtir**
     - Moment.js ekle
     - Day.js ekle
     - Timezone desteÄŸi

validation_checks:
  - âŒ Logic: Contradiction detected
    - Rec #1: Remove moment.js
    - Rec #2: Add moment.js + day.js
  
  - âŒ Logic: Adds 200KB+ while trying to reduce bundle

expected_errors:
  - "Recommendations #1 and #2 contradict"
  - "Cannot both remove and add same library"

action: |
  FAIL - block execution
  Suggest: Choose one approach (native Date or lib)
  
confidence_score: 25/100
```

### Scenario F-002: Invalid File References
```yaml
scenario_id: F-002
name: "Olmayan dosyalara referans"
input: broken-refs.md

test_data: |
  ## Sorunlar
  
  ### SQL Injection
  **Konum**: src/services/NonExistentFile.cs:45
  
  ### Missing Import
  **Konum**: src/deleted-file.tsx:12

validation_checks:
  - âŒ Content: File not found (NonExistentFile.cs)
  - âŒ Content: File not found (deleted-file.tsx)

expected_errors:
  - "Referenced file does not exist: NonExistentFile.cs"
  - "Referenced file does not exist: deleted-file.tsx"

action: |
  FAIL - analysis likely incorrect
  Suggest: Re-scan project files
  
confidence_score: 20/100
```

### Scenario F-003: Impossible Time Estimates
```yaml
scenario_id: F-003
name: "SaÃ§ma sÃ¼re tahminleri"

test_data: |
  ## Sprint Plan
  
  | Task | Effort |
  |------|--------|
  | Database migration (100K rows) | 5 minutes |
  | Microservices refactor | 1 hour |
  | Fix typo | 3 days |

validation_checks:
  - âŒ Effort: DB migration unrealistic (5min)
  - âŒ Effort: Architecture change unrealistic (1h)
  - âŒ Effort: Typo fix way too long (3d)

expected_errors:
  - "DB migration: 5min is unrealistic (benchmark: 2h-2d)"
  - "Microservices refactor: 1h is unrealistic (benchmark: 2w-3m)"
  - "Typo fix: 3d is excessive (benchmark: 5m)"

action: |
  FAIL - estimates completely off
  Suggest: Use benchmark data for estimates
  
confidence_score: 15/100
```

---

## ðŸ”„ REGRESSION SCENARIOS

### Scenario R-001: Priority Inflation Bug
```yaml
scenario_id: R-001
name: "Priority inflation bug (fixed in v3.1)"
regression_test: true
bug_id: BUG-2024-12
fixed_in: v3.1.0

description: |
  Early versions marked too many issues as P0
  Everything security-related became P0
  
bug_behavior: |
  Analysis found:
  - P0: 45 issues (90% of all issues)
  - P1: 3 issues
  - P2-P3: 2 issues

expected_current_behavior: |
  Analysis should find:
  - P0: <15% of issues
  - Balanced distribution
  
test: |
  Run analysis on same project
  Verify P0 count is reasonable
  If P0 >20%: REGRESSION DETECTED

validation: |
  âœ… P0: 5 issues (10%)
  âœ… Distribution balanced
  âœ… Bug did not regress
```

### Scenario R-002: Code Example Missing Bug
```yaml
scenario_id: R-002
name: "Code examples not generated (fixed in v3.0)"
regression_test: true
bug_id: BUG-2024-11
fixed_in: v3.0.0

bug_behavior: |
  P0 issues had descriptions but no code
  Users couldn't implement fixes
  
expected_current_behavior: |
  P0 issues: 100% should have code examples
  P1 issues: 80%+ should have code examples

test: |
  Verify code example coverage
  P0 issues without code: 0 expected

validation: |
  âœ… P0 code coverage: 100%
  âœ… P1 code coverage: 85%
  âœ… Bug did not regress
```

---

## ðŸŽ¯ SCENARIO COVERAGE MATRIX

| Category | Scenarios | Pass Criteria |
|----------|-----------|---------------|
| Happy Path | 5 | All validations pass |
| Edge Cases | 8 | Graceful handling |
| Failures | 6 | Proper error detection |
| Regression | 4 | No old bugs return |

---

## ðŸ”§ Running Scenarios

### Manual Test
```bash
# Run single scenario
$ ai-test run H-001

# Run category
$ ai-test run --category happy-path

# Run all
$ ai-test run --all

# Regression only
$ ai-test run --regression
```

### Automated CI/CD
```yaml
# .github/workflows/test.yml
name: Self-Test Suite

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Happy Path Tests
        run: ai-test run --category happy-path
        
      - name: Run Regression Tests
        run: ai-test run --regression
        
      - name: Check Coverage
        run: |
          if [ $PASS_RATE -lt 95 ]; then
            echo "Test pass rate below 95%"
            exit 1
          fi
```

---

## ðŸ“Š Test Results Format

```markdown
# Test Run Results
**Date**: 2024-12-20  
**Version**: v3.2  
**Scenarios Run**: 23

## Summary
âœ… Passed: 21 (91%)
âš ï¸  Warnings: 1 (4%)
âŒ Failed: 1 (4%)

## Failed Tests
- F-001: Contradiction detection âŒ
  - Expected: Contradiction found
  - Actual: False negative (missed contradiction)
  - Action: Update contradiction patterns

## Warnings
- E-001: Large project handling âš ï¸
  - P0 count within limits but high
  - User notified, proceeded safely

## Regression Tests
âœ… All 4 regression tests passed
No previously fixed bugs have returned
```

---

## ðŸš€ Extending Scenarios

To add new test scenario:

```yaml
# custom-scenario.yml

scenario_id: CUSTOM-001
name: "Your scenario name"
category: edge-case
priority: high

test_data: |
  # Your test input here

validation_checks:
  - Check 1
  - Check 2

expected_outcome: "What should happen"
confidence_threshold: 70
```

---

## ðŸ“š Related Documents

- `SELF_TEST_SUITE.md` - Framework overview
- `VALIDATION_RULES.md` - Rule definitions
- `REGRESSION_TESTS.md` - Regression test suite

---

**Remember**: Good tests prevent bugs from reaching users. Test early, test often! ðŸ›¡ï¸
