# Implementation Guides

**Purpose**: Step-by-step guides to fix issues found by analysis modules.

---

## 📋 Available Guides

### 🔒 Security Fixes
**File**: `security-fixes.md` (12KB, 545 lines)  
**Related Module**: `security-analysis.md`

**Covers**:
- SQL Injection → Parameterized queries (5 steps)
- Exposed Secrets → Git cleanup + rotation (5 steps)
- Missing Authorization → `[Authorize]` attribute (4 steps)
- Vulnerable Dependencies → npm audit fix (5 steps)
- CORS Misconfiguration → Origin restriction (3 steps)
- Weak Password Hashing → Bcrypt migration (4 steps)

**Example**:
```csharp
// ❌ Before: SQL Injection risk
var sql = $"SELECT * FROM Orders WHERE CustomerId = {id}";

// ✅ After: Parameterized query
var orders = _context.Orders.Where(o => o.CustomerId == id).ToList();
```

---

### ⚡ Performance Optimization
**File**: `performance-optimization.md` (12KB, 400+ lines)  
**Related Module**: `performance-analysis.md`

**Covers**:
- Bundle size reduction: moment→date-fns (-65KB), lodash→native (-67KB)
- Image optimization: WebP/AVIF conversion (2.4MB → 340KB)
- N+1 Query fixes: Eager loading (2400ms → 85ms)
- Database indexing: CREATE INDEX (850ms → 8ms)
- Build optimization: Incremental compile (85s → 25s)
- API response caching: Redis (1200ms → 15ms)
- React lazy loading: Code splitting (847KB → 320KB)

**Example**:
```typescript
// ❌ Before: All in main bundle
import AdminDashboard from './AdminDashboard';

// ✅ After: Lazy load
const AdminDashboard = lazy(() => import('./AdminDashboard'));
```

---

### ♿ Accessibility Fixes
**File**: `accessibility-fixes.md` (1.2KB, 47 lines)  
**Related Module**: `accessibility-analysis.md`

**Covers**:
- Alt text for images (12 images)
- Color contrast fixes (WCAG AA compliance)
- Keyboard navigation (Tab, focus indicators)
- ARIA labels

**Example**:
```html
<!-- ❌ Before: No alt text -->
<img src="product.jpg" />

<!-- ✅ After: Descriptive alt text -->
<img src="product.jpg" alt="Blue denim jeans, slim fit, size 32" />
```

---

### 🗄️ Database Migration
**File**: `database-migration.md` (997 bytes, 40 lines)  
**Related Module**: `database-analysis.md`

**Covers**:
- Safe migration strategy (5 steps)
- Backup procedures
- Staging environment testing
- Rollback planning
- Production deployment

**Example**:
```bash
# 1. Backup
pg_dump production_db > backup_20241223.sql

# 2. Test on staging
dotnet ef database update --connection "[STAGING]"

# 3. Apply to production
dotnet ef database update --connection "[PROD]"
```

---

## 🔄 How to Use

### Typical Workflow

**1. Run Analysis**
```markdown
"SEC koduyla security analizi yap"

Output:
❌ SQL Injection in OrderController.cs:45
❌ Exposed secrets in .env
❌ Missing authorization on AdminController
```

**2. Consult Fix Guide**
```markdown
Open: implementation-guides/security-fixes.md
Find: Section 1 - SQL Injection
Read: 5-step fix procedure
```

**3. Apply Fix**
```bash
# Step 1: Find vulnerable code
git grep "ExecuteSqlRaw.*+" -r src/

# Step 2: Write test
# Step 3: Fix code (parameterized query)
# Step 4: Run tests
dotnet test

# Step 5: Commit
git commit -m "fix: SQL injection in OrderController"
```

---

## 📊 Guide Statistics

| Guide | Size | Steps | Code Examples | Time to Apply |
|-------|------|-------|---------------|---------------|
| security-fixes.md | 12KB | 27 steps | 20+ examples | 20-60 min |
| performance-optimization.md | 12KB | 25 steps | 15+ examples | 30-120 min |
| accessibility-fixes.md | 1.2KB | 9 steps | 5+ examples | 10-30 min |
| database-migration.md | 997B | 5 steps | 3+ examples | 15-45 min |

---

## 💡 Best Practices

### Before Applying Fixes

- [ ] Read entire guide section first
- [ ] Backup code/database
- [ ] Create feature branch
- [ ] Write tests first (TDD)
- [ ] Test on staging before production

### While Applying Fixes

- [ ] Follow steps in order
- [ ] Don't skip verification steps
- [ ] Keep changes small and focused
- [ ] Document what you changed
- [ ] Run all tests

### After Applying Fixes

- [ ] Verify the fix works
- [ ] Check for side effects
- [ ] Update documentation
- [ ] Create pull request
- [ ] Monitor production after deploy

---

## 🎯 Related Resources

- **Analysis Modules**: `modules/core/` - Find issues
- **MODULE_CODES.md**: Quick codes for analysis
- **USAGE_GUIDE.md**: How to use the system
- **TURKISH_PROMPTS.md**: Turkish usage examples

---

## 🔮 Future Guides (Planned)

- `refactoring-steps.md` - Code refactoring patterns
- `testing-implementation.md` - Test writing guide
- `deployment-checklist.md` - Safe deployment procedures
- `monitoring-setup.md` - Observability implementation

---

**Need help?** Check the main README.md or consult related analysis modules.

*Last Updated: December 23, 2024*
