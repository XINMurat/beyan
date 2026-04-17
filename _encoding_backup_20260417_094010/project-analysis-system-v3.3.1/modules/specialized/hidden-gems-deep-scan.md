# Module: Hidden Gems & Silent Blockers (Deep Scan)

**Priority**: P1 (High - Reveals Unknown Unknowns)  
**Tokens**: ~2500  
**Analysis Time**: 15-20 minutes  

---

## Purpose

Uncover **invisible** problems and **hidden opportunities** that standard analysis misses:
- Abandoned features draining resources
- Zombie code consuming maintenance effort
- Silent blockers that "work on my machine"
- Bus factor risks (knowledge silos)
- Hidden utility gems that should be promoted
- Fragile scripts everyone fears touching

This module finds what you didn't know to look for.

---

## 1. Abandoned Features (Zombie Code)

### Detection Patterns

```yaml
half_implemented:
  indicators:
    - Feature flag always false
    - Entire component commented out
    - TODO older than 3 months
    - Unused exports (imported nowhere)
    - "WIP" or "Temporary" in comments from >6 months ago
  
  confidence: "medium_75%"  # Requires context

dormant_features:
  detection: |
    # Find commented-out blocks
    grep -r "\/\*.*TODO.*\*\/" src/ --include="*.ts" --include="*.tsx"
    
    # Find old TODOs
    git log --all --since="6 months ago" -S "TODO" --pretty=format:"%h %ad | %s" --date=short
    
    # Find unused exports
    ts-prune | grep "used in module"
```

### Analysis Examples

```typescript
// ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ZOMBIE: Feature flag never enabled
// Found in: src/features/premium-dashboard/
const ENABLE_PREMIUM_DASHBOARD = false;  // Added 8 months ago

if (ENABLE_PREMIUM_DASHBOARD) {
  // 400 lines of code here
  // Last modified: 8 months ago
  // Imported by: 0 files
}

// ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ RECOMMENDATION:
// DELETE or SHIP. This is:
// - 400 lines of untested code
// - Maintenance burden (refactors skip it)
// - Confusion for new developers
// - Sunk cost fallacy

// Decision:
// [ ] Delete (if no longer needed)
// [ ] Finish & ship (if still valuable)
// [ ] Document why kept (if temporary)
```

```tsx
// ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ZOMBIE: Entire component commented out
{/* 
<BetaFeature>
  // 200 lines of JSX
</BetaFeature>
*/}

// Last modified: 11 months ago
// No issue tracker reference
// No explanation of why commented

// ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ RECOMMENDATION:
// If keeping: Move to feature branch, not main
// If deleting: Git history preserves it
```

---

## 2. Hidden Potential (Promote to Shared Library)

### Detection Patterns

```yaml
utility_gems:
  indicators:
    - Function copied 3+ times across files
    - Utility used in 5+ different features
    - Generic helper in specific feature folder
    - High-quality code buried in random file
  
  confidence: "high_85%"  # Pattern-based

detection:
  duplication: |
    # Find duplicated functions
    jscpd src/ --min-tokens 50 --reporters json
    
    # Find widely-used utils
    grep -r "import.*from.*utils" src/ | cut -d: -f2 | sort | uniq -c | sort -rn
```

### Examples

```typescript
// ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã‚Â¸ HIDDEN GEM: Found in src/features/user/helpers.ts
// But used across 8 different features!

export function formatCurrency(amount: number, locale = 'tr-TR'): string {
  return new Intl.NumberFormat(locale, {
    style: 'currency',
    currency: 'TRY'
  }).format(amount);
}

// ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ RECOMMENDATION: Promote to shared library
// Current: src/features/user/helpers.ts
// Better:  src/shared/utils/currency.ts
// Impact:
// - Makes reuse easier
// - One place to fix bugs
// - Clear ownership
// - Better tested

// Usage shows value:
// - src/features/order/OrderSummary.tsx
// - src/features/invoice/InvoiceDetail.tsx
// - src/features/reports/SalesReport.tsx
// - src/features/admin/PaymentSettings.tsx
// - ... (8 total)
```

```typescript
// ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã‚Â¸ DUPLICATED GEM: Same validation logic in 4 places
// src/features/user/validation.ts
// src/features/order/validation.ts
// src/features/invoice/validation.ts
// src/features/admin/validation.ts

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function isValidEmail(email: string): boolean {
  return EMAIL_REGEX.test(email);
}

// ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ RECOMMENDATION: DRY violation
// Extract to: src/shared/validation/email.ts
// Effort: 30 minutes
// Benefit: Single source of truth, easier to improve
```

---

## 3. Silent Blockers ("Works on My Machine")

### Undocumented Environment Dependencies

```yaml
detection:
  missing_in_readme:
    - Required environment variables
    - System dependencies (Redis, PostgreSQL version)
    - Global npm packages
    - OS-specific quirks
  
  symptoms:
    - "Setup failed" issues from new devs
    - Works locally, fails in CI/CD
    - "It works for me" responses
  
  confidence: "medium_70%"  # Requires investigation
```

### Examples

```yaml
# ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ SILENT BLOCKER: Undocumented dependency
# Found in: package.json scripts

"scripts": {
  "build": "node build.js"
}

# build.js line 15:
const sharp = require('sharp');  # Requires libvips system library!

# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Problem:
# - Not in README
# - Not in package.json (missing native dep)
# - New devs get cryptic error: "Cannot find module 'sharp'"
# - Works for original dev (they installed libvips months ago)

# ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ FIX:
# 1. Document in README:
#    ## Prerequisites
#    - Node.js 18+
#    - libvips (image processing)
#      - Mac: brew install vips
#      - Ubuntu: apt-get install libvips-dev
#
# 2. Add to Dockerfile if using containers
# 3. Check in CI/CD setup script
```

```yaml
# ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ SILENT BLOCKER: Hidden global dependency
# Found in: .github/workflows/deploy.yml

- name: Deploy
  run: ./deploy.sh

# deploy.sh line 5:
vercel deploy --prod

# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Problem:
# - Assumes `vercel` CLI installed globally
# - Works for devs who ran `npm install -g vercel`
# - Fails for new devs or CI/CD
# - No version pinning

# ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ FIX:
# 1. Add to devDependencies:
#    npm install --save-dev vercel
#
# 2. Use npx:
#    npx vercel deploy --prod
#
# 3. Document in README:
#    ## Deployment
#    Requires Vercel CLI (installed automatically)
```

---

## 4. Hardcoded Configuration (Magic Numbers & Paths)

```yaml
detection:
  magic_numbers:
    pattern: "Unexplained constants in code"
    examples:
      - "if (retries > 5)"  # Why 5?
      - "sleep(3000)"  # Why 3 seconds?
      - "maxItems = 100"  # Why 100?
  
  hardcoded_paths:
    pattern: "Absolute or environment-specific paths"
    examples:
      - "C:\\Users\\dev\\project"
      - "/home/user/uploads"
      - "localhost:3000"
  
  hardcoded_secrets:
    pattern: "API endpoints, DB hosts in code"
    examples:
      - "https://api.production.com"  # Should be env var
      - "db.company.local:5432"  # Should be config

confidence: "high_90%"
```

### Examples

```typescript
// ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ MAGIC NUMBER: No explanation
// Found in: src/services/retry.ts

async function fetchWithRetry(url: string) {
  for (let i = 0; i < 5; i++) {  // ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Why 5?
    try {
      return await fetch(url);
    } catch (error) {
      await sleep(3000);  // ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Why 3 seconds?
    }
  }
  throw new Error('Max retries exceeded');
}

// ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ FIX:
const MAX_RETRIES = 5;  // ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Reasonable default for transient network errors
const RETRY_DELAY_MS = 3000;  // ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ AWS Lambda cold start typically < 3s

async function fetchWithRetry(
  url: string, 
  maxRetries = MAX_RETRIES,
  delayMs = RETRY_DELAY_MS
) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fetch(url);
    } catch (error) {
      if (i < maxRetries - 1) {
        await sleep(delayMs * Math.pow(2, i));  // Exponential backoff
      }
    }
  }
  throw new Error(`Max retries (${maxRetries}) exceeded`);
}
```

```csharp
// ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ HARDCODED PATH: Fails outside Windows
// Found in: FileService.cs

public void SaveUpload(IFormFile file) {
    var path = @"C:\inetpub\uploads\" + file.FileName;  // ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Windows-only
    using var stream = File.Create(path);
    file.CopyTo(stream);
}

// ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ FIX:
// appsettings.json
{
  "FileStorage": {
    "UploadPath": "/var/uploads"  // Or Azure Blob, S3
  }
}

// FileService.cs
private readonly string _uploadPath;

public FileService(IConfiguration config) {
    _uploadPath = config["FileStorage:UploadPath"];
}

public void SaveUpload(IFormFile file) {
    var safeName = Path.GetFileName(file.FileName);  // Sanitize
    var path = Path.Combine(_uploadPath, safeName);  // OS-agnostic
    
    Directory.CreateDirectory(_uploadPath);  // Ensure exists
    using var stream = File.Create(path);
    file.CopyTo(stream);
}
```

---

## 5. Complex Manual Workflows (Automation Opportunities)

```yaml
detection:
  indicators:
    - "How to deploy" docs with 20+ steps
    - Scripts with "TODO: Automate this"
    - Repetitive copy-paste in changelogs
    - Manual database migration tracking
    - Release notes compiled by hand
  
  confidence: "medium_75%"  # Requires workflow understanding
```

### Examples

```yaml
# ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ MANUAL WORKFLOW: Deployment nightmare
# Found in: DEPLOYMENT.md

## How to Deploy (30 steps, 45 minutes)

1. Pull latest from main
2. Run tests locally (hope they pass)
3. Update version in package.json
4. Update version in Dockerfile
5. Update version in helm chart
6. Build Docker image
7. Tag image with version
8. Push to registry
9. Update staging deployment
10. Wait 5 minutes
11. Smoke test staging
... (20 more steps)

# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Problem:
# - Error-prone (easy to skip step)
# - Time-consuming (45 minutes)
# - Bus factor (only 2 people know all steps)
# - No rollback plan

# ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ AUTOMATION OPPORTUNITY:
# GitHub Actions workflow: 1 click, 5 minutes

name: Deploy
on:
  push:
    tags: ['v*']

jobs:
  deploy:
    steps:
      - Checkout code
      - Run tests
      - Build & push Docker
      - Deploy to staging
      - Smoke test
      - Deploy to production
      - Rollback on failure
      
# Effort: 4 hours to setup
# ROI: Save 45 min ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 2 deploys/week ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 52 weeks = 78 hours/year
```

---

## 6. Dependency Graph Issues

```yaml
circular_dependencies:
  detection: "madge --circular src/"
  
god_objects:
  definition: "Class/module imported by >20 others"
  detection: |
    # Find most-imported files
    grep -rh "^import.*from" src/ | \
      sed "s/.*from ['\"]//;s/['\"].*//" | \
      sort | uniq -c | sort -rn | head -20

tight_coupling:
  detection: "Changes in A always require changes in B"
  tool: "Git log analysis"
  
confidence: "high_88%"
```

### Examples

```typescript
// ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ GOD OBJECT: utils/helpers.ts
// Imported by: 73 files
// Lines: 2,847
// Problem: Central point of failure

// ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ RECOMMENDATION: Split by domain
utils/
  string-helpers.ts    (imported by 23 files)
  date-helpers.ts      (imported by 18 files)
  validation-helpers.ts (imported by 15 files)
  array-helpers.ts     (imported by 17 files)

// Benefit:
// - Changes isolated to relevant domain
// - Easier to test individual helpers
// - Reduced merge conflicts
// - Clear ownership
```

---

## 7. Bus Factor Analysis (Knowledge Silos)

```yaml
detection:
  single_author_modules:
    command: |
      # Files touched by only 1 person
      git log --all --format='%an' --name-only | \
        sort | uniq -c | awk '$1 == 1'
  
  inactive_maintainers:
    definition: "Last commit >6 months ago"
    risk: "Knowledge lost if they leave"
  
  critical_modules:
    examples:
      - Authentication
      - Payment processing
      - Database migrations
      - Deployment scripts

confidence: "medium_70%"  # Git-based, may miss context
```

### Examples

```yaml
# ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ BUS FACTOR: Critical module, single maintainer
# Found in: src/services/PaymentService.ts

git log --oneline src/services/PaymentService.ts | \
  awk '{print $2}' | sort | uniq -c

# Output:
# 47 john.doe
#  2 jane.smith
#  1 bob.jones

# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Problem:
# - 94% of commits by John
# - Critical payment logic
# - John on vacation = no one can fix payment bugs
# - High risk

# ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ MITIGATION:
# 1. Pair programming sessions
# 2. Document payment logic (architecture doc)
# 3. Code review required from 2+ people
# 4. Knowledge transfer session
# 5. Add comprehensive tests (reduce need for John)

# Bus Factor Score: 1 (CRITICAL)
# Target: 3+ people familiar with payment code
```

---

## 8. Fragile Tooling (Brittle Scripts)

```yaml
detection:
  indicators:
    - Scripts that fail if run from wrong directory
    - Missing error handling
    - Assumes specific environment
    - No idempotency (can't run twice)
    - Hardcoded paths
  
  confidence: "medium_75%"
```

### Examples

```bash
#!/bin/bash
# ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ FRAGILE: deploy.sh

# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Breaks if run from subdirectory
cd src/
npm run build

# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ No error handling - continues on failure
docker build -t myapp .
docker push myapp:latest

# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Assumes docker login already done
# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ No rollback on failure
# ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Not idempotent (re-run breaks)

kubectl apply -f k8s/
```

```bash
#!/bin/bash
# ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ ROBUST: deploy.sh

set -euo pipefail  # Exit on error, undefined var

# Work from script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

# Verify prerequisites
command -v docker >/dev/null || { echo "Docker not installed"; exit 1; }
command -v kubectl >/dev/null || { echo "kubectl not installed"; exit 1; }

# Environment-specific config
ENV="${1:-staging}"
IMAGE="myapp:${ENV}-$(git rev-parse --short HEAD)"

# Build with error handling
echo "Building..."
npm run build || { echo "Build failed"; exit 1; }

echo "Creating Docker image..."
docker build -t "$IMAGE" . || { echo "Docker build failed"; exit 1; }

# Login if needed
if ! docker info | grep -q "Username"; then
    echo "Docker not logged in"
    docker login || { echo "Docker login failed"; exit 1; }
fi

echo "Pushing image..."
docker push "$IMAGE" || { echo "Docker push failed"; exit 1; }

# Idempotent deployment
echo "Deploying to $ENV..."
kubectl apply -f "k8s/${ENV}/" || {
    echo "Deployment failed, rolling back..."
    kubectl rollout undo deployment/myapp
    exit 1
}

echo "Deployment successful!"
echo "Image: $IMAGE"
```

---

## Analysis Protocol

### Step 1: Automated Scans (5 min)

```bash
#!/bin/bash
# Deep scan for hidden issues

echo "=== Abandoned Features ==="
# Old TODOs
git log --since="6 months ago" --all -S "TODO" --oneline

# Unused exports
ts-prune | wc -l

# Commented blocks
grep -r "\/\*" src/ --include="*.ts" | wc -l

echo "=== Hidden Gems ==="
# Duplicated code
jscpd src/ --min-tokens 50 --reporters console

# Widely-used utils in feature folders
find src/features -name "*utils*" -o -name "*helpers*"

echo "=== Circular Dependencies ==="
madge --circular --extensions ts,tsx src/

echo "=== Bus Factor ==="
# Files with single author
git log --all --format='%an' --name-only | \
  sort | uniq -c | awk '$1 == 1' | wc -l

echo "=== Fragile Scripts ==="
# Scripts without error handling
grep -L "set -e" scripts/*.sh
```

### Step 2: Manual Analysis (10 min)

```yaml
review:
  - [ ] Check README for missing prerequisites
  - [ ] Review deploy scripts for fragility
  - [ ] Examine feature flags (any always false?)
  - [ ] Check for hardcoded configs
  - [ ] Identify manual workflows
  - [ ] Map knowledge silos (critical modules)
```

### Step 3: Generate Report

```markdown
# Hidden Gems & Silent Blockers Report

## Discovery Summary
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¹ Zombie code: 1,200 lines (3 files)
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€¦Ã‚Â½ Hidden gems: 4 functions to promote
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ Silent blockers: 2 undocumented dependencies
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â§ Manual workflows: 1 prime for automation
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€¦Ã¢â‚¬â„¢ Bus factor: 3 critical single-maintainer modules

---

## Zombie Code (1,200 lines to delete)

### 1. Premium Dashboard (400 lines) ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¹
**Location**: `src/features/premium-dashboard/`
**Status**: Feature flag disabled for 8 months
**Last Modified**: 2024-03-15
**Decision Needed**: Delete or ship?

**Analysis**:
- No issue tracker reference
- Imports: 0 (completely unused)
- Tests: 0
- Maintenance cost: Refactors skip it, confuses new devs

**Recommendation**: 
```bash
git rm -r src/features/premium-dashboard/
# Save to branch if might revive:
git checkout -b archive/premium-dashboard
git cherry-pick <commits>
```

**Effort**: 30 minutes  
**Impact**: Cleaner codebase, less confusion  
**Confidence**: High (85%)

---

## Hidden Gems (Promote to Shared)

### 1. Currency Formatter ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€¦Ã‚Â½
**Current**: `src/features/user/helpers.ts`
**Used By**: 8 different features
**Lines**: 15

```typescript
export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('tr-TR', {
    style: 'currency',
    currency: 'TRY'
  }).format(amount);
}
```

**Recommendation**: 
```
Move to: src/shared/utils/currency.ts
Update imports in 8 files
Add unit tests (currently 0)
Add JSDoc comments
```

**Effort**: 1 hour  
**Impact**: 
- Single source of truth
- Easier to enhance (add EUR support)
- Better tested
**Confidence**: High (90%)

---

## Silent Blockers

### 1. Undocumented libvips Dependency ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨
**Found In**: `build.js` line 15
**Impact**: New devs can't build project

```javascript
const sharp = require('sharp');  // Requires libvips!
```

**Problem**:
- Not in README
- Only original dev has libvips installed
- Cryptic error for new devs

**Fix**:
```markdown
# README.md

## Prerequisites
- Node.js 18+
- **libvips** (image processing)
  - Mac: `brew install vips`
  - Ubuntu: `apt-get install libvips-dev`
  - Windows: [Download installer](...)
```

**Effort**: 15 minutes  
**Impact**: Onboarding time -2 hours  
**Confidence**: High (95%)

---

## Automation Opportunities

### 1. Manual Deployment (30 steps ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ 1 click) ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â§
**Current**: 45-minute manual process
**Found In**: `DEPLOYMENT.md`

**ROI Calculation**:
- Current: 45 min ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 2 deployments/week = 90 min/week
- Annual: 90 min ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 52 weeks = 78 hours
- Automation effort: 4 hours
- Break-even: 3 weeks

**Recommendation**: GitHub Actions workflow

**Effort**: 4 hours  
**Annual Savings**: 78 hours  
**ROI**: 1,850%  
**Confidence**: High (90%)

---

## Bus Factor Risks

### 1. Payment Service (Bus Factor: 1) ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€¦Ã¢â‚¬â„¢
**Location**: `src/services/PaymentService.ts`
**Primary Author**: John (94% of commits)
**Risk**: High - critical for revenue

**Mitigation**:
1. Pair programming session (4 hours)
2. Document architecture (2 hours)
3. Require 2+ reviewers on payment PRs
4. Add comprehensive tests (reduce dependency)

**Effort**: 6 hours  
**Risk Reduction**: Bus factor 1 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ 3  
**Confidence**: Medium (75%)

---

## Summary & Priorities

### Quick Wins (< 2 hours)
1. Delete zombie code (30 min)
2. Document libvips dependency (15 min)
3. Promote currency formatter (1 hour)

**Total**: 1 hour 45 min  
**Impact**: Cleaner codebase, easier onboarding

### High ROI (4-6 hours)
4. Automate deployment (4 hours)
   - ROI: 1,850%
   - Annual savings: 78 hours

### Risk Mitigation (6 hours)
5. Payment service knowledge transfer (6 hours)
   - Reduces critical bus factor

---

## Monitoring

```yaml
ongoing:
  - Review feature flags monthly (delete if unused)
  - Track bus factor for critical modules
  - Document new prerequisites immediately
  - Automate repetitive workflows (>30 min/month)
  
metrics:
  - Zombie code: 0 lines (target)
  - Bus factor: 3+ for critical modules
  - Undocumented deps: 0
  - Manual deployments: 0
```

---

**Analysis Complete** | Hidden Issues Found: 11 | Opportunities: 5 | Confidence: Medium (78%)
