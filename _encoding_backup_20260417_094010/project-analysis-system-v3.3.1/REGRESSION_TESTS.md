# Regression Tests - Geri DÃƒÂ¶nen Bug Tespiti

**Version**: 1.0  
**Purpose**: Daha ÃƒÂ¶nce dÃƒÂ¼zeltilen buglarÃ„Â±n tekrar ortaya ÃƒÂ§Ã„Â±kmasÃ„Â±nÃ„Â± ÃƒÂ¶nleme  
**Run Frequency**: Her release ÃƒÂ¶ncesi + CI/CD pipeline

---

## Ã°Å¸Å½Â¯ Regression Test Philosophy

> "Once bitten, twice shy" - Bir kez karÃ…Å¸Ã„Â±laÃ…Å¸Ã„Â±lan bug bir daha olmamalÃ„Â±

**Prensip**: Her dÃƒÂ¼zeltilen bug bir test senaryosu olarak kayÃ„Â±t edilir ve sÃƒÂ¼rekli ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±rÃ„Â±lÃ„Â±r.

---

## Ã°Å¸Ââ€º Known Fixed Bugs Registry

### BUG-001: Priority Inflation
```yaml
bug_id: BUG-001
title: "Too many P0 issues marked"
discovered: 2024-11-15
fixed_in: v3.1.0
severity: high
reporter: User feedback

description: |
  Early versions marked almost everything as P0
  Even minor issues became "critical"
  Example: Missing alt text Ã¢â€ â€™ P0 (should be P2)

root_cause: |
  Priority logic was too aggressive:
  if (security_related) Ã¢â€ â€™ P0
  if (performance_impact) Ã¢â€ â€™ P0
  
  No distinction between severity levels

fix_applied: |
  Updated priority matrix:
  - P0: Only critical security + data loss + show-stopper performance
  - P1: High security + significant performance
  - P2: Medium issues
  - P3: Nice-to-have

regression_test: |
  Test on known project:
  - Before fix: 45 P0 issues (90%)
  - After fix: 5 P0 issues (10%)
  
  If P0 > 20% Ã¢â€ â€™ REGRESSION DETECTED

test_data:
  project: sample-ecommerce-app
  expected_p0_count: 3-7
  expected_p0_ratio: 0.05-0.15
  
  assertions:
    - p0_count <= 10
    - p0_ratio <= 0.20
    - distribution_balanced == true
```

**Test Implementation**:
```python
def test_BUG_001_priority_inflation():
    """Verify priority inflation bug is fixed"""
    
    # Run analysis on reference project
    result = analyze_project("sample-ecommerce-app")
    
    # Count priorities
    p0 = len(result['findings']['P0'])
    total = sum(len(result['findings'][p]) for p in ['P0','P1','P2','P3'])
    p0_ratio = p0 / total
    
    # Assertions
    assert p0 <= 10, f"P0 count {p0} exceeds limit (10)"
    assert p0_ratio <= 0.20, f"P0 ratio {p0_ratio:.1%} exceeds 20%"
    
    # Check distribution balance
    assert len(result['findings']['P1']) > p0, "More P1 than P0 expected"
    
    print(f"Ã¢Å“â€¦ BUG-001: Priority inflation still fixed")
    print(f"   P0: {p0} ({p0_ratio:.1%})")
```

---

### BUG-002: Missing Code Examples
```yaml
bug_id: BUG-002
title: "P0 issues missing code examples"
discovered: 2024-11-20
fixed_in: v3.0.0
severity: medium
reporter: Internal testing

description: |
  Critical issues had good descriptions
  But no code examples showing how to fix
  Users couldn't implement recommendations

root_cause: |
  Code example generation was optional
  Not enforced for P0/P1 priorities

fix_applied: |
  Made code examples mandatory:
  - P0 issues: 100% must have before/after code
  - P1 issues: 80% should have code
  - P2/P3: Optional but encouraged

regression_test: |
  Count code examples in P0/P1 issues
  If P0 coverage < 100% Ã¢â€ â€™ REGRESSION
  If P1 coverage < 75% Ã¢â€ â€™ WARNING

test_data:
  project: sample-vulnerable-app
  expected_p0_with_code: 100%
  expected_p1_with_code: 80%+
```

**Test Implementation**:
```python
def test_BUG_002_missing_code_examples():
    """Verify P0/P1 issues have code examples"""
    
    result = analyze_project("sample-vulnerable-app")
    
    # Check P0 code coverage
    p0_issues = result['findings']['P0']
    p0_with_code = [i for i in p0_issues if 'code' in i and i['code']]
    p0_coverage = len(p0_with_code) / len(p0_issues)
    
    # Check P1 code coverage  
    p1_issues = result['findings']['P1']
    p1_with_code = [i for i in p1_issues if 'code' in i and i['code']]
    p1_coverage = len(p1_with_code) / len(p1_issues)
    
    # Assertions
    assert p0_coverage == 1.0, f"P0 code coverage {p0_coverage:.0%} < 100%"
    assert p1_coverage >= 0.75, f"P1 code coverage {p1_coverage:.0%} < 75%"
    
    print(f"Ã¢Å“â€¦ BUG-002: Code examples still present")
    print(f"   P0: {p0_coverage:.0%}, P1: {p1_coverage:.0%}")
```

---

### BUG-003: Invalid File References
```yaml
bug_id: BUG-003
title: "Analysis references non-existent files"
discovered: 2024-11-25
fixed_in: v3.1.2
severity: high
reporter: User report

description: |
  Analysis claimed issues in files that don't exist
  Example: "Found in: src/DeletedFile.ts:45"
  But DeletedFile.ts was removed months ago

root_cause: |
  AI hallucination or stale cache
  File scanning not verifying existence
  Copy-paste from old analysis

fix_applied: |
  Added file existence verification:
  - Before reporting issue: verify file exists
  - If file missing: skip or mark as "historical"
  - Add warning if many missing files

regression_test: |
  Analyze project, extract file references
  Verify each referenced file exists
  If >10% missing Ã¢â€ â€™ REGRESSION

test_data:
  project: sample-project-with-deletions
  known_deleted: ["src/old-service.ts", "legacy/utils.js"]
  
  assertions:
    - no_references_to_deleted_files
    - all_current_references_valid
```

**Test Implementation**:
```python
def test_BUG_003_invalid_file_references():
    """Verify no references to non-existent files"""
    
    result = analyze_project("sample-project-with-deletions")
    
    # Extract all file references
    file_refs = extract_file_references(result)
    
    # Check each file exists
    invalid_refs = []
    for file_path in file_refs:
        if not os.path.exists(file_path):
            invalid_refs.append(file_path)
    
    # Assertions
    assert len(invalid_refs) == 0, \
        f"Found {len(invalid_refs)} invalid file references: {invalid_refs}"
    
    print(f"Ã¢Å“â€¦ BUG-003: All file references valid")
    print(f"   Checked {len(file_refs)} file references")
```

---

### BUG-004: Contradictory Recommendations
```yaml
bug_id: BUG-004
title: "System suggests contradicting actions"
discovered: 2024-12-01
fixed_in: v3.2.0
severity: medium
reporter: Code review

description: |
  Recommendation #1: "Remove lodash to reduce bundle"
  Recommendation #5: "Add lodash.debounce for better UX"
  
  Both can't be true!

root_cause: |
  Each recommendation generated independently
  No cross-validation between recommendations
  No contradiction detection

fix_applied: |
  Added contradiction detection layer:
  - Check for opposing actions (add/remove same lib)
  - Verify bundle optimization doesn't conflict with features
  - Flag suspicious patterns

regression_test: |
  Analyze project known to trigger contradictions
  Count contradictions detected
  If contradictions = 0 Ã¢â€ â€™ Good
  If contradictions > 0 Ã¢â€ â€™ Check if properly flagged

test_data:
  project: bundle-optimization-project
  known_contradiction: "lodash removal vs feature requiring lodash"
```

**Test Implementation**:
```python
def test_BUG_004_contradictory_recommendations():
    """Verify contradictions are detected"""
    
    result = analyze_project("bundle-optimization-project")
    
    # Run contradiction detection
    contradictions = detect_contradictions(result['recommendations'])
    
    # This project has known contradiction
    # System should detect it
    assert len(contradictions) > 0, "Known contradiction not detected!"
    
    # Check contradiction is properly flagged
    lodash_contradiction = [c for c in contradictions 
                           if 'lodash' in c['description'].lower()]
    
    assert len(lodash_contradiction) > 0, \
        "Lodash contradiction not detected"
    
    print(f"Ã¢Å“â€¦ BUG-004: Contradictions properly detected")
    print(f"   Found {len(contradictions)} contradictions")
```

---

### BUG-005: Unrealistic Time Estimates
```yaml
bug_id: BUG-005
title: "Wildly unrealistic effort estimates"
discovered: 2024-12-05
fixed_in: v3.2.1
severity: medium
reporter: Sprint planning feedback

description: |
  Sprint plan suggested:
  - "Database migration: 15 minutes"
  - "Microservices refactor: 2 hours"
  - "Fix typo: 3 days"
  
  All clearly wrong!

root_cause: |
  No benchmark data for effort estimation
  AI guessing based on task name only
  No sanity checks

fix_applied: |
  Added benchmark database:
  - Common tasks with typical effort ranges
  - Sanity checking against benchmarks
  - Flag if estimate outside 2x benchmark

regression_test: |
  Generate sprint plan for known tasks
  Verify estimates within reasonable range
  
test_data:
  project: typical-web-app
  tasks:
    - sql_injection_fix: 30min-2h
    - database_migration: 2h-2days
    - typo_fix: 5min-30min
```

**Test Implementation**:
```python
def test_BUG_005_unrealistic_estimates():
    """Verify effort estimates are reasonable"""
    
    result = plan_sprint("typical-web-app")
    
    # Define benchmarks
    benchmarks = {
        'sql_injection': (30, 120),  # 30min - 2h
        'db_migration': (120, 2880),  # 2h - 2days
        'typo_fix': (5, 30)           # 5min - 30min
    }
    
    # Check each task
    unrealistic = []
    for task in result['tasks']:
        task_type = classify_task(task['description'])
        if task_type in benchmarks:
            min_time, max_time = benchmarks[task_type]
            estimate = task['effort_minutes']
            
            # Check if wildly off (>5x or <1/5)
            if estimate > max_time * 5 or estimate < min_time / 5:
                unrealistic.append({
                    'task': task['description'],
                    'estimate': estimate,
                    'benchmark': (min_time, max_time)
                })
    
    assert len(unrealistic) == 0, \
        f"Found {len(unrealistic)} unrealistic estimates: {unrealistic}"
    
    print(f"Ã¢Å“â€¦ BUG-005: Effort estimates reasonable")
```

---

## Ã°Å¸â€â€ž Regression Test Suite Runner

### Full Suite Execution
```python
def run_full_regression_suite():
    """Run all regression tests"""
    
    tests = [
        test_BUG_001_priority_inflation,
        test_BUG_002_missing_code_examples,
        test_BUG_003_invalid_file_references,
        test_BUG_004_contradictory_recommendations,
        test_BUG_005_unrealistic_estimates
    ]
    
    results = {
        'total': len(tests),
        'passed': 0,
        'failed': 0,
        'failures': []
    }
    
    for test_func in tests:
        try:
            test_func()
            results['passed'] += 1
            print(f"Ã¢Å“â€¦ {test_func.__name__}")
        except AssertionError as e:
            results['failed'] += 1
            results['failures'].append({
                'test': test_func.__name__,
                'error': str(e)
            })
            print(f"Ã¢ÂÅ’ {test_func.__name__}: {e}")
    
    # Print summary
    print("\n" + "="*50)
    print("REGRESSION TEST SUMMARY")
    print("="*50)
    print(f"Total: {results['total']}")
    print(f"Passed: {results['passed']} Ã¢Å“â€¦")
    print(f"Failed: {results['failed']} Ã¢ÂÅ’")
    
    if results['failed'] > 0:
        print("\nFAILURES:")
        for failure in results['failures']:
            print(f"  - {failure['test']}")
            print(f"    {failure['error']}")
        
        raise Exception("REGRESSION DETECTED! Old bugs have returned.")
    
    print("\nÃ¢Å“â€¦ All regression tests passed!")
    return results
```

---

## Ã°Å¸â€œÅ  Test Coverage Dashboard

```markdown
# Regression Test Coverage

| Bug ID | Title | Fixed In | Test Status |
|--------|-------|----------|-------------|
| BUG-001 | Priority Inflation | v3.1.0 | Ã¢Å“â€¦ Passing |
| BUG-002 | Missing Code | v3.0.0 | Ã¢Å“â€¦ Passing |
| BUG-003 | Invalid Files | v3.1.2 | Ã¢Å“â€¦ Passing |
| BUG-004 | Contradictions | v3.2.0 | Ã¢Å“â€¦ Passing |
| BUG-005 | Time Estimates | v3.2.1 | Ã¢Å“â€¦ Passing |

**Last Run**: 2024-12-20 14:30  
**Pass Rate**: 100% (5/5)  
**Next Run**: Before v3.3 release
```

---

## Ã°Å¸Å¡Â¨ CI/CD Integration

```yaml
# .github/workflows/regression.yml
name: Regression Tests

on:
  push:
    branches: [main, develop]
  pull_request:
  schedule:
    - cron: '0 0 * * *'  # Daily

jobs:
  regression:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup environment
        run: |
          pip install -r requirements.txt
          
      - name: Run regression suite
        run: |
          python regression_tests.py
          
      - name: Upload results
        if: always()
        uses: actions/upload-artifact@v2
        with:
          name: regression-results
          path: regression-report.json
          
      - name: Notify on failure
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          webhook-url: ${{ secrets.SLACK_WEBHOOK }}
          payload: |
            {
              "text": "Ã°Å¸Å¡Â¨ REGRESSION DETECTED! Old bugs have returned.",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Regression Test Failed*\nCheck logs for details."
                  }
                }
              ]
            }
```

---

## Ã°Å¸â€œÂ Adding New Regression Tests

When a new bug is fixed:

1. **Document the bug**:
```yaml
bug_id: BUG-XXX
title: "Bug description"
discovered: YYYY-MM-DD
fixed_in: vX.Y.Z
severity: high/medium/low
```

2. **Write regression test**:
```python
def test_BUG_XXX_description():
    """Verify bug XXX is fixed"""
    # Test implementation
    pass
```

3. **Add to suite**:
```python
# Add to run_full_regression_suite()
tests.append(test_BUG_XXX_description)
```

4. **Run and verify**:
```bash
$ python regression_tests.py
Ã¢Å“â€¦ BUG-XXX test passes
```

---

## Ã°Å¸Å½Â¯ Regression Prevention Strategy

### Level 1: Immediate (Post-Fix)
- Write regression test
- Add to CI/CD
- Verify in next release

### Level 2: Continuous
- Run daily in CI/CD
- Monitor pass rate
- Alert on failure

### Level 3: Preventive
- Code review checklist
- Static analysis rules
- Architecture safeguards

---

## Ã°Å¸â€œÅ¡ Related Documents

- `SELF_TEST_SUITE.md` - Overall testing framework
- `TEST_SCENARIOS.md` - General test scenarios
- `VALIDATION_RULES.md` - Validation rules applied

---

**Motto**: "Test today, sleep tonight, smile tomorrow" Ã°Å¸â€ºÂ¡Ã¯Â¸Â

_Never forget a bug. Never repeat a mistake._
