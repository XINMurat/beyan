# Module: File & Directory Structure Analysis

**Priority**: P0 (Critical - Always Load)  
**Tokens**: ~2000  
**Analysis Time**: 5-10 minutes  

---

## Purpose

Analyze project organization, naming conventions, modularity, and detect structural anti-patterns that impact maintainability, onboarding, and development velocity.

---

## Automated Checks

### 1. Directory Depth Analysis

```yaml
scoring:
  excellent (9-10):
    max_depth: 4 levels
    example: "src/features/user/components/UserCard.tsx"
    
  good (7-8):
    max_depth: 6 levels
    example: "src/app/modules/admin/views/settings/UserSettings.tsx"
    
  attention (5-6):
    max_depth: 8 levels
    concern: "Hard to navigate, long imports"
    
  critical (0-4):
    max_depth: 9+ levels
    concern: "Architectural smell, refactor needed"

trigger:
  condition: "depth > 7"
  action: "ALERT: Flatten structure or modularize"
  confidence: "high_90%"
```

**Analysis Command**:
```bash
# Detect deepest path
find . -type d -not -path "*/node_modules/*" -not -path "*/.git/*" | \
  awk -F/ 'NF > max {max = NF; path = $0} END {print max-1, path}'
```

### 2. File Size Distribution

```yaml
healthy_distribution:
  small (<200 lines): "70%"
  medium (200-500 lines): "25%"
  large (500-1000 lines): "4%"
  god_files (>1000 lines): "1% (ideally 0%)"

thresholds:
  warning: "> 800 lines"
  critical: "> 1500 lines"
  refactor_immediately: "> 2500 lines"

confidence:
  file_size: "high_95%"  # Measurable
  refactoring_impact: "medium_70%"  # Depends on complexity
```

**Detection**:
```bash
# Find god files
find src -name "*.ts" -o -name "*.tsx" -o -name "*.cs" | \
  xargs wc -l | sort -rn | head -20
```

**Output Format**:
```markdown
🔴 God Files Detected:
1. src/utils/helpers.ts - 2,847 lines
   Confidence: High (95%)
   Impact: High (single point of failure)
   Recommendation: Split into:
   - StringHelpers.ts (lines 1-450)
   - DateHelpers.ts (lines 451-890)
   - ValidationHelpers.ts (lines 891-1,340)
   - ArrayHelpers.ts (lines 1,341-2,847)
   Effort: 4 hours, Medium risk
```

### 3. Naming Convention Consistency

```yaml
check_patterns:
  typescript_react:
    files: "PascalCase for components (UserCard.tsx)"
    directories: "kebab-case or camelCase"
    functions: "camelCase"
    constants: "UPPER_SNAKE_CASE"
    
  dotnet_csharp:
    files: "PascalCase (UserService.cs)"
    directories: "PascalCase"
    methods: "PascalCase"
    private_fields: "_camelCase"

inconsistency_threshold:
  excellent: "< 5% violations"
  good: "5-10% violations"
  attention: "10-20% violations"
  critical: "> 20% violations"
```

**Detection**:
```bash
# Check React component naming
find src -name "*.tsx" | grep -v "^[A-Z]" | wc -l
```

### 4. Circular Dependency Detection

```yaml
severity:
  0_circular: "✅ Excellent"
  1-2_circular: "🟡 Monitor"
  3-5_circular: "🟠 Address soon"
  6+_circular: "🔴 Critical architectural issue"

analysis:
  tool: "madge (npm) or manual inspection"
  command: "madge --circular --extensions ts,tsx src/"
  
confidence:
  detection: "high_90%"
  impact: "high_90%"  # Circular deps always problematic
```

### 5. Dead Code / Unused Files

```yaml
detection_methods:
  unused_exports:
    tool: "ts-prune or eslint-plugin-unused-imports"
    confidence: "high_85%"
    
  orphaned_files:
    definition: "Files not imported anywhere"
    check: "grep -r 'import.*FileN ame' src/"
    confidence: "medium_75%"
    
  commented_out_files:
    pattern: "Entire file is commented out"
    confidence: "high_95%"

action:
  if_unused_90_days: "Move to archive/ directory"
  if_unused_180_days: "Safe to delete"
```

### 6. Module Cohesion Analysis

```yaml
feature_based_structure:  # Preferred
  example: |
    src/features/
      user/
        components/
        hooks/
        services/
        types/
        index.ts
  score: 9/10
  
layer_based_structure:  # Traditional but ok
  example: |
    src/
      components/
      services/
      utils/
      types/
  score: 7/10
  concern: "Can become monolithic"

mixed_structure:  # Red flag
  example: "Inconsistent grouping"
  score: 4/10
  concern: "Hard to navigate, unclear ownership"
```

### 7. Import Path Length

```yaml
healthy:
  relative: "import { X } from './components'"
  max_depth: "../../.."  # 3 levels up max
  
problematic:
  deep_relative: "import { X } from '../../../../../utils'"
  fix: "Use path aliases (@/utils)"
  
configuration:
  tsconfig: |
    {
      "compilerOptions": {
        "baseUrl": ".",
        "paths": {
          "@/*": ["src/*"],
          "@components/*": ["src/components/*"],
          "@utils/*": ["src/utils/*"]
        }
      }
    }
```

---

## Analysis Protocol

### Step 1: Quick Scan (2 min)

```bash
#!/bin/bash
# Quick project structure assessment

echo "=== Directory Depth ==="
find . -type d -not -path "*/node_modules/*" -not -path "*/.git/*" | \
  awk -F/ '{print NF-1}' | sort -rn | head -1

echo "=== File Count by Type ==="
find src -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn

echo "=== Top 10 Largest Files ==="
find src -type f -name "*.ts" -o -name "*.tsx" -o -name "*.cs" | \
  xargs wc -l | sort -rn | head -10

echo "=== Directory Count ==="
find src -type d | wc -l
```

**Expected Output**:
```
Directory Depth: 6
File Types: 
  142 tsx
  89 ts
  34 css
  12 json

Largest Files:
  2847 src/utils/helpers.ts
  1342 src/components/UserDashboard.tsx
  986 src/services/ApiService.ts

Directory Count: 47
```

### Step 2: Deep Analysis (5 min)

```yaml
analyze:
  1. Module boundaries
     - Are features self-contained?
     - Do features import from each other? (code smell)
     
  2. Naming conventions
     - Count violations per pattern
     - Generate rename script if >10% inconsistent
     
  3. File organization
     - Feature-based or layer-based?
     - Consistency score
     
  4. Import analysis
     - Circular dependencies
     - Deep import paths
     - Cross-module coupling
     
  5. Code distribution
     - Business logic in services?
     - Components focused on UI?
     - Utilities truly generic?
```

### Step 3: Generate Report

```markdown
# File Structure Analysis

## Overall Score: 7.5/10 🟡

### Summary
- ✅ Good: Feature-based organization
- ✅ Good: Consistent naming (92%)
- 🟡 Attention: 3 god files detected
- 🔴 Critical: 2 circular dependencies

---

## Detailed Findings

### 1. Directory Structure: 8/10 ✅
**Depth**: Max 5 levels (healthy)
**Organization**: Feature-based (excellent)
**Consistency**: 90% (good)

**Example**:
```
src/features/
  user/
    components/     ✅ Clear boundaries
    hooks/          ✅ Co-located
    services/       ✅ Single responsibility
    types/          ✅ Type safety
    __tests__/      ✅ Test co-location
```

### 2. File Size Distribution: 6/10 🟡

| Category | Count | Percentage | Status |
|----------|-------|------------|--------|
| Small (<200) | 142 | 68% | ✅ Healthy |
| Medium (200-500) | 54 | 26% | ✅ Good |
| Large (500-1000) | 9 | 4% | 🟡 Monitor |
| God Files (>1000) | 3 | 1.4% | 🔴 Fix |

**God Files Requiring Immediate Attention**:

#### 1. src/utils/helpers.ts (2,847 lines) 🔴
- **Confidence**: High (95%)
- **Impact**: High (imported by 73 files)
- **Risk**: Single point of failure, merge conflicts
- **Recommendation**: Split into 4 files
  ```
  StringHelpers.ts (lines 1-450)
  DateHelpers.ts (lines 451-890)
  ValidationHelpers.ts (lines 891-1340)
  ArrayHelpers.ts (lines 1341-2847)
  ```
- **Effort**: 4-6 hours
- **Test Impact**: 127 tests affected, update imports

#### 2. src/components/UserDashboard.tsx (1,342 lines) 🔴
- **Confidence**: High (90%)
- **Impact**: Medium (complex component)
- **Recommendation**: Extract sub-components
  ```
  UserDashboard.tsx (main, 200 lines)
  ├── ProfileSection.tsx
  ├── ActivityFeed.tsx
  ├── SettingsPanel.tsx
  └── StatsWidgets.tsx
  ```
- **Effort**: 6-8 hours
- **Benefit**: 3x easier testing, better reusability

### 3. Circular Dependencies: 🔴 Critical

**Detected**: 2 circular chains

#### Circle 1:
```
UserService.ts → OrderService.ts → UserService.ts
```
- **Impact**: Difficult to test, tight coupling
- **Fix**: Introduce UserRepository.ts as mediator
- **Effort**: 2 hours
- **Confidence**: High (92%)

#### Circle 2:
```
AuthContext.tsx → useAuth.ts → AuthContext.tsx
```
- **Impact**: Hook/Context anti-pattern
- **Fix**: Move logic to useAuth, Context only stores
- **Effort**: 1 hour
- **Confidence**: High (95%)

### 4. Naming Consistency: 8/10 ✅

| Pattern | Expected | Actual | Score |
|---------|----------|--------|-------|
| Components | PascalCase | 92% | ✅ |
| Files | kebab-case | 88% | ✅ |
| Hooks | use* prefix | 100% | ✅ |
| Constants | UPPER_SNAKE | 75% | 🟡 |

**Violations** (18 files):
```bash
# Fix script
mv src/components/userCard.tsx src/components/UserCard.tsx
mv src/utils/string_helper.ts src/utils/stringHelper.ts
# ... (16 more)
```

### 5. Dead Code: 5/10 🟡

**Unused Exports**: 23 found
- Confidence: Medium (75%)
- Recommendation: Review with team before deletion

**Orphaned Files**: 4 found
```
src/legacy/OldUserService.ts (last modified: 8 months ago)
src/utils/deprecatedHelpers.ts (last modified: 11 months ago)
```
- Action: Move to archive/ directory
- Effort: 30 min

---

## Prioritized Recommendations

### 🔴 P0 - Critical (Do This Week)

1. **Split src/utils/helpers.ts** (6 hours)
   - Prevents merge conflicts
   - Reduces blast radius of changes
   - Success metric: Max file size < 500 lines

2. **Break Circle 1: UserService ↔ OrderService** (2 hours)
   - Introduce UserRepository.ts
   - Success metric: `madge --circular` returns 0

### 🟡 P1 - High (Do This Sprint)

3. **Refactor UserDashboard.tsx** (8 hours)
   - Extract 4 sub-components
   - Success metric: Component < 300 lines

4. **Fix naming violations** (2 hours)
   - Run automated rename script
   - Update imports (automated)
   - Success metric: 100% naming consistency

### 🟢 P2 - Medium (This Quarter)

5. **Archive dead code** (1 hour)
   - Move 4 orphaned files to archive/
   - Document why (historical reference)
   - Success metric: 0 unused files in src/

6. **Setup path aliases** (1 hour)
   - Configure tsconfig.json
   - Replace deep relative imports
   - Success metric: No import path > 3 levels

---

## Success Metrics

```yaml
immediate (1 week):
  - God files: 3 → 0
  - Circular deps: 2 → 0
  
short_term (1 month):
  - Max file size: < 800 lines
  - Naming consistency: 100%
  
long_term (3 months):
  - Avg file size: < 250 lines
  - Directory depth: < 5
  - Dead code: 0%
```

---

## Tool Recommendations

```yaml
automated_checks:
  circular_deps:
    - madge (npm package)
    - command: "madge --circular --extensions ts,tsx src/"
    
  unused_exports:
    - ts-prune (npm package)
    - command: "ts-prune"
    
  file_size:
    - custom script (provided above)
    
  naming:
    - eslint with naming rules
    - custom script for batch rename

ci_cd_integration:
  - Run on every PR
  - Fail if circular deps introduced
  - Warn if file > 500 lines
  - Block if file > 1500 lines
```

---

## Confidence Levels

```yaml
findings:
  god_files: "high_95%"  # Measurable
  circular_deps: "high_92%"  # Tool-detected
  naming: "high_90%"  # Pattern-based
  dead_code: "medium_75%"  # Requires human verification
  
recommendations:
  splitting_files: "high_88%"  # Clear benefit
  fixing_circles: "high_92%"  # Proven solution
  renaming: "high_95%"  # Automated, low risk
```

---

## Anti-Patterns Detected

### ❌ The "utils" Graveyard
```
src/utils/helpers.ts (2,847 lines of everything)
```
- **Why Bad**: No clear purpose, hard to find functions
- **Fix**: Domain-specific utility files

### ❌ Feature Coupling
```
features/user → features/order → features/user
```
- **Why Bad**: Can't extract features independently
- **Fix**: Shared domain layer or events

### ❌ Deep Nesting
```
src/app/modules/admin/dashboard/components/widgets/UserWidget.tsx
```
- **Why Bad**: Hard to navigate, long imports
- **Fix**: Flatten or use path aliases

---

**Analysis Complete** | Confidence: High (88%) | Next Review: 2 weeks
