# Validation Rules - Detaylı Doğrulama Kuralları

**Version**: 1.0  
**Purpose**: Self-test suite için kapsamlı kural seti  
**Maintenance**: Her yeni pattern eklendiğinde güncellenir

---

## 📋 Rule Categories

### 1. SYNTAX RULES (Sözdizimi Kuralları)

#### Rule S-001: Markdown Headers
```yaml
id: S-001
name: "Markdown header syntax"
severity: medium
auto_fix: true

pattern: |
  Headers must have space after #
  
violations:
  - "#Header" ❌
  - "## Header" ❌ (should be "## ")
  
correct:
  - "# Header" ✅
  - "## Header" ✅

auto_fix_action: |
  Add space after # symbols
```

#### Rule S-002: Code Block Closure
```yaml
id: S-002
name: "Code blocks must close"
severity: high
auto_fix: true

pattern: |
  Every ``` must have matching closing ```
  
violations:
  ```
  ```python
  def foo():
      pass
  # Missing closing ```
  ```

auto_fix_action: |
  Add closing ``` at appropriate location
  (use indentation to guess)
```

#### Rule S-003: Table Formatting
```yaml
id: S-003
name: "Markdown table syntax"
severity: low
auto_fix: true

pattern: |
  Tables must have header separator
  Pipes must align (optional but nice)
  
violations:
  | Header 1 | Header 2 |
  | Value 1 | Value 2 |  # Missing separator
  
correct:
  | Header 1 | Header 2 |
  |----------|----------|
  | Value 1  | Value 2  |

auto_fix_action: |
  Insert separator row
  Optionally align pipes
```

#### Rule S-004: YAML Validity
```yaml
id: S-004
name: "YAML blocks must be valid"
severity: high
auto_fix: false

pattern: |
  ```yaml blocks must parse without errors
  
violations:
  ```yaml
  key: value
    invalid_indent: bad
  ```

validation: |
  import yaml
  try:
      yaml.safe_load(content)
  except yaml.YAMLError as e:
      return FAIL(str(e))
```

---

### 2. CONTENT RULES (İçerik Kuralları)

#### Rule C-001: Priority Distribution
```yaml
id: C-001
name: "P0 sorunlar makul sayıda"
severity: medium
auto_fix: false

rule: |
  P0 issues should be <15% of total
  P0 > 10 items is suspicious (priority inflation)
  
thresholds:
  max_p0_count: 10
  max_p0_ratio: 0.15
  
violations:
  - P0: 25 issues (total 30) → %83 → ❌ Inflation
  - P0: 15 issues (total 100) → %15 → ⚠️ Warning
  
explanation: |
  Too many P0 issues suggests:
  - AI is over-cautious
  - Project is in very bad state (unlikely)
  - Priority criteria too loose
  
action: |
  Review priorities manually
  Consider re-running with stricter P0 definition
```

#### Rule C-002: Score Boundaries
```yaml
id: C-002
name: "Scores must be 0-10"
severity: high
auto_fix: true

rule: |
  All scores must be in range [0, 10]
  
violations:
  - "Security: 12/10" → ❌ Invalid
  - "Performance: -2/10" → ❌ Invalid
  
auto_fix_action: |
  Clamp to [0, 10] range
  Log warning for manual review
```

#### Rule C-003: File Path Validity
```yaml
id: C-003
name: "Referenced files should exist"
severity: low
auto_fix: false

rule: |
  When analysis mentions file paths, verify existence
  
acceptable_missing:
  - "example-file.ts" (hypothetical examples OK)
  - Files in suggestions (future files)
  
violations:
  - "Found in: src/OrderService.cs:45" 
    but src/OrderService.cs doesn't exist → ⚠️
  
action: |
  If file mentioned as EXISTING but missing:
  - Add warning in report
  - Don't block, might be deleted recently
```

#### Rule C-004: Code Example Quality
```yaml
id: C-004
name: "Code examples must be syntactically valid"
severity: medium
auto_fix: false

rule: |
  Code examples in ``` blocks should compile/parse
  
languages_to_check:
  - typescript: "tsc --noEmit"
  - python: "python -m py_compile"
  - csharp: "dotnet build (dry run)"
  
violations:
  ```typescript
  const x = ;  // Syntax error
  ```

action: |
  Parse code with language parser
  If fail: Add warning, suggest review
```

---

### 3. LOGIC RULES (Mantık Kuralları)

#### Rule L-001: No Contradictions
```yaml
id: L-001
name: "Recommendations must not contradict"
severity: high
auto_fix: false

contradiction_patterns:
  - pattern: "reduce bundle" + "add library"
    reason: "Adding libs increases bundle"
    
  - pattern: "delete X.ts" + "modify X.ts"
    reason: "Can't modify deleted file"
    
  - pattern: "increase performance" + "add logging everywhere"
    reason: "Excessive logging hurts performance"
    
  - pattern: "improve security" + "disable authentication"
    reason: "Obvious security reduction"

detection: |
  For each pair of recommendations:
    Extract keywords
    Check against contradiction_patterns
    If match: FLAG

example_violation:
  recommendation_1: "Remove lodash to reduce bundle size"
  recommendation_2: "Add moment.js for date handling"
  contradiction: "Adding large library contradicts bundle reduction"
  severity: "medium"
```

#### Rule L-002: Dependency Order
```yaml
id: L-002
name: "Task dependencies must be ordered"
severity: high
auto_fix: true

rule: |
  If Task B depends on Task A, then A must come first
  
dependency_keywords:
  implies_dependency:
    - "after" → requires previous task
    - "then" → sequential dependency
    - "once X is done" → explicit dependency
  
  blocking_keywords:
    - "test" requires "code written"
    - "deploy" requires "test passed"
    - "migrate" requires "backup"

violations:
  Sprint Plan:
    Task 1: "Write tests" ❌
    Task 2: "Write code" ❌
    # Test can't be before code!

auto_fix_action: |
  Topological sort of tasks
  Respect explicit dependencies
  Put setup tasks first
```

#### Rule L-003: Effort Estimation Sanity
```yaml
id: L-003
name: "Time estimates must be realistic"
severity: medium
auto_fix: false

suspicious_patterns:
  very_fast:
    - "database migration: 5 min" → ⚠️ Risky
    - "architecture change: 1 hour" → ⚠️ Unlikely
    - "refactor god class: 30 min" → ⚠️ Too fast
  
  very_slow:
    - "fix typo: 2 days" → ⚠️ Too slow
    - "add console.log: 4 hours" → ⚠️ Overkill

benchmarks:
  sql_injection_fix: "30min - 2h"
  eslint_fix: "5min - 30min"
  database_migration: "2h - 2 days"
  api_versioning: "1 week - 1 month"

action: |
  Compare estimate against benchmarks
  If outside range: Flag for review
  Suggest benchmark range
```

#### Rule L-004: Resource Allocation
```yaml
id: L-004
name: "No person overallocated"
severity: high
auto_fix: true

rule: |
  No person should have >40h/week assigned
  Team total should match capacity
  
violations:
  Ali: 80h/week → ❌ Impossible
  Team (5 people): 250h/week → ⚠️ Overcommitted (max 200h)

auto_fix_action: |
  Distribute tasks more evenly
  Suggest hiring if consistently overallocated
  Flag critical path bottlenecks
```

---

### 4. QUALITY RULES (Kalite Kuralları)

#### Rule Q-001: Language Consistency
```yaml
id: Q-001
name: "Report language must be consistent"
severity: low
auto_fix: true

rule: |
  If Turkish report requested:
  - Turkish content should be >90%
  - Technical terms in English OK
  - Code in original language OK
  
acceptable_english:
  - Technical terms: "API", "SQL", "JWT"
  - Code: "const", "function", "if"
  - Proper nouns: "React", "TypeScript"
  
violations:
  # Turkish report with English paragraphs
  "The project has security issues..." → ❌

detection: |
  Count words by language
  If mismatch >10%: Flag

auto_fix_action: |
  Cannot auto-translate
  Flag for manual review
  Suggest re-running with language hint
```

#### Rule Q-002: Actionable Recommendations
```yaml
id: Q-002
name: "Recommendations must be concrete"
severity: medium
auto_fix: false

vague_patterns:
  - "improve performance" ❌
  - "enhance security" ❌
  - "optimize code" ❌
  - "better UX" ❌

actionable_patterns:
  - "Reduce bundle from 847KB to <300KB by replacing lodash with lodash-es" ✅
  - "Fix SQL injection in OrderService.cs:45 by using parameterized queries" ✅
  - "Add [Authorize] attribute to AdminController:DeleteUser method" ✅

criteria:
  must_have_at_least_2_of:
    - Specific file/line number
    - Concrete metric (numbers)
    - Code example
    - Step-by-step instructions

violation_example:
  ❌ "Optimize database queries"
  ✅ "Add index on Orders.CustomerId (currently N+1 query)"
```

#### Rule Q-003: Code Example Coverage
```yaml
id: Q-003
name: "P0/P1 issues need code examples"
severity: medium
auto_fix: false

rule: |
  P0 issues: 100% must have before/after code
  P1 issues: 80% should have code examples
  P2 issues: 50% recommended
  P3 issues: Optional

violations:
  P0 Issue: "SQL Injection vulnerability"
  Description: "Use parameterized queries"
  Code: (none) → ❌ Missing

  P1 Issue: "N+1 query"
  Code: (present) → ✅

action: |
  Count code examples per priority
  If below threshold: FLAG
  Suggest re-run with "add code examples" hint
```

#### Rule Q-004: Readability Score
```yaml
id: Q-004
name: "Report must be readable"
severity: low
auto_fix: false

metrics:
  flesch_reading_ease:
    target: ">60" (easy to read)
    acceptable: "50-60" (moderate)
    poor: "<50" (difficult)
  
  sentence_length:
    target: "<25 words/sentence"
    max: "40 words"
  
  paragraph_length:
    target: "3-5 sentences"
    max: "8 sentences"

tools:
  - textstat (Python)
  - readability-score (npm)

action: |
  Calculate readability metrics
  If poor: Suggest simplification
  Cannot auto-fix (meaning may change)
```

---

## 🎯 Rule Priority Matrix

| Priority | When to Apply | Auto-Fix | Blocker |
|----------|---------------|----------|---------|
| **HIGH** | Always | If safe | Mode 3 |
| **MEDIUM** | Default mode | Sometimes | Warning only |
| **LOW** | Quality focus | Often | No |

---

## 🔧 Custom Rules

Users can add custom validation rules:

```yaml
# .ai-validation-custom.yml

custom_rules:
  - id: CUSTOM-001
    name: "Our company coding standard"
    severity: medium
    
    pattern: |
      All API endpoints must have OpenAPI documentation
    
    check: |
      For each endpoint in code:
        Find corresponding OpenAPI spec
        If missing: FLAG
    
    auto_fix: false
    message: "Add OpenAPI spec for {endpoint}"
```

---

## 📊 Rule Coverage Report

After validation, generate coverage report:

```markdown
## Validation Coverage

**Rules Applied**: 18/24
**Rules Passed**: 16/18
**Warnings**: 2
**Errors**: 0

### Not Checked (Why?)
- S-004 (YAML): No YAML blocks in output
- L-004 (Resource): No sprint plan generated
- Q-004 (Readability): Disabled by user

### Failed Rules
(none)

### Warnings
- C-003: 2 files referenced but not found
- L-003: 1 task estimate seems optimistic
```

---

## 🔄 Rule Evolution

Rules are **versioned** and can be updated:

```yaml
rule_version: 1.0

updates:
  1.1:
    - "Added L-005: API versioning check"
    - "Improved Q-002: Better vague pattern detection"
  
  1.0:
    - "Initial release"
```

---

## 🚨 Emergency Override

In special cases, rules can be disabled:

```yaml
# Emergency: Disable validation
validation:
  enabled: false
  reason: "Emergency production fix"
  
# OR selective disable
validation:
  disabled_rules:
    - L-003  # Time estimate check
    - Q-004  # Readability
  reason: "Quick draft needed"
```

**Warning**: Only use in emergencies! Validation protects quality.

---

## 📚 Related Documents

- `SELF_TEST_SUITE.md` - Overall framework
- `TEST_SCENARIOS.md` - Example test cases
- `CONFIDENCE_SCORING.md` - How rules affect confidence

---

**Philosophy**: Rules are **guidelines**, not prison. They help maintain quality while allowing flexibility when needed. 🎯
