# Module: Performance Analysis

**Priority**: P0 (Critical for Web/Mobile)  
**Tokens**: ~2500  
**Analysis Time**: 10-15 minutes  

---

## Purpose

Measure and optimize application performance using Core Web Vitals, bundle analysis, database query efficiency, and runtime performance. Identifies bottlenecks and provides specific optimization recommendations.

---

## Core Web Vitals (Google)

```yaml
metrics:
  LCP (Largest Contentful Paint):
    good: "< 2.5s"
    needs_improvement: "2.5s - 4.0s"
    poor: "> 4.0s"
    measures: "Loading performance"
    weight: "Critical for SEO"
    
  FID (First Input Delay):
    good: "< 100ms"
    needs_improvement: "100ms - 300ms"
    poor: "> 300ms"
    measures: "Interactivity"
    weight: "User frustration indicator"
    
  CLS (Cumulative Layout Shift):
    good: "< 0.1"
    needs_improvement: "0.1 - 0.25"
    poor: "> 0.25"
    measures: "Visual stability"
    weight: "Prevents misclicks"

scoring:
  excellent: "All 3 metrics in 'good' range"
  good: "2 metrics 'good', 1 'needs improvement'"
  attention: "1 metric 'good', 2 'needs improvement'"
  critical: "Any metric in 'poor' range"
```

### Measurement Tools

```bash
# Lighthouse Performance Audit
lighthouse https://your-app.com --only-categories=performance --output=json

# WebPageTest (Real user conditions)
# https://www.webpagetest.org/

# Chrome DevTools Performance Tab
# 1. Open DevTools
# 2. Performance tab
# 3. Click Record → Interact → Stop
# 4. Analyze flame graph
```

---

## Bundle Size Analysis

```yaml
thresholds:
  initial_bundle:
    excellent: "< 100 KB gzipped"
    good: "100-200 KB gzipped"
    attention: "200-400 KB gzipped"
    critical: "> 400 KB gzipped"
    
  total_js:
    excellent: "< 300 KB gzipped"
    good: "300-600 KB gzipped"
    attention: "600-1 MB gzipped"
    critical: "> 1 MB gzipped"
    
  total_css:
    excellent: "< 50 KB gzipped"
    good: "50-100 KB gzipped"
    attention: "100-200 KB gzipped"
    critical: "> 200 KB gzipped"

confidence: "high_95%"  # Measurable
```

### Analysis Commands

```bash
# Webpack Bundle Analyzer
npx webpack-bundle-analyzer build/bundle-stats.json

# Vite Build Analysis
vite build --sourcemap
npx vite-bundle-visualizer

# Check gzipped sizes
du -sh build/static/js/* | sort -hr
gzip -c build/static/js/main.js | wc -c
```

**Expected Output**:
```
Total JS: 687 KB (243 KB gzipped) 🟡
├── main.js: 456 KB (162 KB gzipped)
├── vendor.js: 198 KB (71 KB gzipped)
└── async chunks: 33 KB (10 KB gzipped)

Largest dependencies:
1. moment.js: 67 KB (use date-fns instead, saves 50 KB)
2. lodash: 45 KB (import specific functions, saves 40 KB)
3. react-icons: 38 KB (tree-shake or use specific pack)
```

---

## Frontend Performance

### 1. Lazy Loading Strategy

```yaml
code_splitting:
  routes: "Split by route (React.lazy)"
  components: "Heavy components (modals, charts)"
  libraries: "Dynamic imports for heavy libs"
  
  confidence: "high_90%"

check:
  present: "Look for React.lazy or dynamic import()"
  count: "Should see multiple chunks in build output"
  
recommendation:
  if_single_bundle: "Split critical routes immediately"
  effort: "2-4 hours"
  impact: "30-50% faster initial load"
```

**Example Detection**:
```tsx
// ❌ Bad: Everything in one bundle
import Dashboard from './Dashboard';
import Analytics from './Analytics';
import Settings from './Settings';

// ✅ Good: Route-level code splitting
const Dashboard = lazy(() => import('./Dashboard'));
const Analytics = lazy(() => import('./Analytics'));
const Settings = lazy(() => import('./Settings'));
```

### 2. Image Optimization

```yaml
checks:
  format:
    webp: "Modern, 25-35% smaller than JPEG/PNG"
    avif: "Newer, 50% smaller (if supported)"
    fallback: "JPEG/PNG for old browsers"
    
  sizing:
    responsive: "srcset with multiple sizes"
    lazy_load: "loading='lazy' attribute"
    dimensions: "Explicit width/height (prevents CLS)"
    
  compression:
    photos: "JPEG/WebP quality 80-85"
    graphics: "PNG/WebP lossless"
    tool: "ImageOptim, Sharp, Squoosh"

confidence: "high_92%"
```

**Detection Script**:
```bash
# Find large unoptimized images
find public -type f \( -name "*.jpg" -o -name "*.png" \) -size +500k

# Check if WebP used
grep -r "\.webp" src/ | wc -l

# Check lazy loading
grep -r 'loading="lazy"' src/ | wc -l
```

### 3. Caching Strategy

```yaml
http_caching:
  static_assets: "Cache-Control: public, max-age=31536000 (1 year)"
  html: "Cache-Control: no-cache (always revalidate)"
  api_responses: "Cache-Control: max-age=300 (5 min)"
  
  confidence: "high_90%"

service_worker:
  pwa: "Offline support, background sync"
  workbox: "Simplified service worker setup"
  confidence: "medium_75%"

client_storage:
  localStorage: "User preferences, theme"
  sessionStorage: "Temp data (current session)"
  indexedDB: "Large datasets"
  confidence: "high_88%"
```

### 4. Third-Party Scripts

```yaml
analysis:
  identify: "Google Analytics, Intercom, Facebook Pixel, etc."
  measure: "Blocking time, bytes transferred"
  strategy: "Lazy load, defer, or remove"
  
  confidence: "high_92%"

common_offenders:
  google_tag_manager: "~50 KB, defer loading"
  facebook_pixel: "~40 KB, load after interaction"
  intercom: "~70 KB, lazy load chat widget"
  
recommendations:
  - Load after page interactive (not in <head>)
  - Use async or defer attributes
  - Consider self-hosting (avoid external requests)
```

---

## Backend Performance

### 1. Database Query Analysis

```yaml
n_plus_one:
  detection: "Multiple queries in loop"
  tool: "Django Debug Toolbar, Entity Framework Profiler"
  fix: "Eager loading (include, prefetch)"
  impact: "100x speedup possible"
  confidence: "high_95%"

missing_indexes:
  symptom: "Slow queries (>100ms)"
  detection: "EXPLAIN query, execution plan"
  fix: "Add index on commonly filtered/sorted columns"
  impact: "10-1000x speedup"
  confidence: "high_92%"

full_table_scans:
  symptom: "Query time proportional to table size"
  detection: "EXPLAIN shows 'Seq Scan'"
  fix: "Add WHERE clause index"
  confidence: "high_95%"
```

**Example (Entity Framework C#)**:
```csharp
// ❌ Bad: N+1 query problem
var users = _context.Users.ToList();
foreach (var user in users) {
    var orders = _context.Orders.Where(o => o.UserId == user.Id).ToList();
    // 1 query for users + N queries for orders = N+1
}

// ✅ Good: Eager loading
var users = _context.Users
    .Include(u => u.Orders)  // Single query with JOIN
    .ToList();
```

### 2. API Response Time

```yaml
thresholds:
  excellent: "< 100ms"
  good: "100-300ms"
  attention: "300-1000ms"
  critical: "> 1000ms (1s)"

optimization_tactics:
  caching: "Redis, in-memory cache"
  pagination: "Limit result set (max 100 items)"
  compression: "gzip, brotli"
  cdn: "Static asset delivery"
  
  confidence: "high_90%"
```

### 3. Caching Layers

```yaml
strategies:
  database_query_cache:
    redis: "Cache expensive queries"
    ttl: "5 min - 1 hour (depends on data volatility)"
    
  response_cache:
    http: "Cache GET responses"
    etag: "Conditional requests (304 Not Modified)"
    
  computed_data:
    background_job: "Pre-compute heavy aggregations"
    materialized_view: "Pre-joined database views"

confidence: "high_88%"
```

---

## Analysis Protocol

### Step 1: Quick Performance Scan (3 min)

```bash
#!/bin/bash
# Quick performance assessment

echo "=== Bundle Sizes ==="
du -sh build/static/js/*.js | sort -hr | head -5

echo "=== Lighthouse Performance ==="
lighthouse https://localhost:3000 --only-categories=performance --output=json \
  | jq '.categories.performance.score * 100'

echo "=== Image Optimization ==="
find public -type f \( -name "*.jpg" -o -name "*.png" \) -size +500k

echo "=== Lazy Loading Check ==="
grep -r "React.lazy\|import()" src/ | wc -l
```

### Step 2: Deep Performance Dive (10 min)

```yaml
1. Core Web Vitals
   - Run Lighthouse (mobile + desktop)
   - Check LCP, FID, CLS scores
   - Identify specific elements causing issues

2. Bundle Analysis
   - Generate webpack/vite bundle report
   - Identify largest dependencies
   - Check for duplicate packages

3. Network Waterfall
   - Chrome DevTools Network tab
   - Identify blocking resources
   - Check request parallelization

4. Database Queries (Backend)
   - Enable query logging
   - Identify N+1 problems
   - Check missing indexes

5. Runtime Performance
   - Chrome DevTools Performance tab
   - Record user interaction
   - Identify long tasks (>50ms)
```

### Step 3: Generate Report

```markdown
# Performance Analysis Report

## Overall Score: 68/100 🟡

### Core Web Vitals
| Metric | Score | Status | Target |
|--------|-------|--------|--------|
| LCP | 3.2s | 🟡 Needs Improvement | <2.5s |
| FID | 85ms | ✅ Good | <100ms |
| CLS | 0.18 | 🟡 Needs Improvement | <0.1 |

**Performance Score**: 68/100 (Lighthouse)
- Desktop: 74/100
- Mobile: 62/100 (more critical)

---

## Detailed Findings

### 1. Bundle Size: 🔴 Critical

**Current**:
- Total JS: 847 KB (302 KB gzipped)
- Initial bundle: 456 KB (162 KB gzipped)
- Total CSS: 89 KB (31 KB gzipped)

**Issues**:

#### 🔴 P0: Moment.js in bundle (67 KB)
```javascript
// Found in: src/utils/dateHelper.ts
import moment from 'moment';

// Replace with date-fns (saves 50 KB)
import { format, parseISO } from 'date-fns';
```
- **Impact**: 50 KB savings (19% reduction)
- **Effort**: 2 hours (refactor 12 usages)
- **Confidence**: High (95%)

#### 🔴 P0: Entire Lodash imported (72 KB)
```javascript
// Bad: Imports entire library
import _ from 'lodash';

// Good: Import specific functions
import debounce from 'lodash/debounce';
import throttle from 'lodash/throttle';
```
- **Impact**: 60 KB savings (22% reduction)
- **Effort**: 3 hours (refactor 23 usages)
- **Confidence**: High (92%)

#### 🟡 P1: No code splitting (456 KB initial)
```jsx
// Current: Everything in one bundle
import Dashboard from './pages/Dashboard';
import Analytics from './pages/Analytics';

// Better: Route-level splitting
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Analytics = lazy(() => import('./pages/Analytics'));
```
- **Impact**: 70% reduction in initial load (456 KB → ~130 KB)
- **Effort**: 4 hours
- **Confidence**: High (90%)

**After Optimizations**:
- Total JS: 540 KB (192 KB gzipped) ✅ -36%
- Initial bundle: 130 KB (46 KB gzipped) ✅ -72%

---

### 2. Images: 🟡 Attention

**Issues**:

#### 🟡 P1: Large unoptimized images (4 files)
```
public/hero.jpg: 2.4 MB (should be <500 KB)
public/banner.png: 1.8 MB (should be <500 KB)
```

**Optimization**:
```bash
# Convert to WebP with quality 85
cwebp -q 85 hero.jpg -o hero.webp  # 2.4 MB → 340 KB
cwebp -q 85 banner.png -o banner.webp  # 1.8 MB → 280 KB
```

```html
<!-- Responsive + WebP with fallback -->
<picture>
  <source type="image/webp" srcset="hero.webp">
  <img src="hero.jpg" alt="Hero image" loading="lazy" width="1200" height="600">
</picture>
```
- **Impact**: 4.2 MB → 620 KB (85% reduction)
- **Effort**: 1 hour
- **Confidence**: High (95%)

#### 🟢 P2: No lazy loading (23 images)
```html
<!-- Current -->
<img src="product1.jpg" alt="Product" />

<!-- Better -->
<img src="product1.jpg" alt="Product" loading="lazy" />
```
- **Impact**: Faster initial page load
- **Effort**: 30 min (add loading="lazy" to 23 images)
- **Confidence**: High (95%)

---

### 3. LCP (Largest Contentful Paint): 🟡 3.2s

**Target**: <2.5s  
**Current**: 3.2s  
**Gap**: 0.7s to fix  

**Root Causes**:

1. **Large hero image blocks render** (2.4 MB) 🔴
   - Fix: Optimize image (see above)
   - Impact: -1.2s LCP

2. **CSS blocks rendering** (89 KB) 🟡
   - Current: CSS in <link> (render-blocking)
   - Fix: Inline critical CSS, defer non-critical
   ```html
   <style>/* Critical CSS inline */</style>
   <link rel="preload" href="main.css" as="style" onload="this.rel='stylesheet'">
   ```
   - Impact: -0.3s LCP
   - Effort: 3 hours

3. **Font loading delay** 🟡
   - Current: Fonts loaded from Google Fonts
   - Fix: Self-host + font-display: swap
   ```css
   @font-face {
     font-family: 'Roboto';
     src: url('/fonts/roboto.woff2');
     font-display: swap;  /* Show text immediately */
   }
   ```
   - Impact: -0.2s LCP
   - Effort: 1 hour

**After Fixes**: LCP = 1.7s ✅ (3.2s → 1.7s)

---

### 4. CLS (Cumulative Layout Shift): 🟡 0.18

**Target**: <0.1  
**Current**: 0.18  
**Issue**: Content jumps during load  

**Causes**:

1. **Images without dimensions** 🔴
   ```html
   <!-- Bad: No dimensions, causes layout shift -->
   <img src="hero.jpg" alt="Hero" />
   
   <!-- Good: Explicit dimensions, space reserved -->
   <img src="hero.jpg" alt="Hero" width="1200" height="600" />
   ```
   - Impact: -0.08 CLS
   - Effort: 1 hour (add dimensions to 23 images)
   - Confidence: High (95%)

2. **Dynamic content insertion** 🟡
   ```tsx
   // Bad: Banner added after API call, pushes content down
   {showBanner && <Banner />}
   
   // Good: Reserve space with min-height
   <div style={{ minHeight: showBanner ? '80px' : '0' }}>
     {showBanner && <Banner />}
   </div>
   ```
   - Impact: -0.05 CLS
   - Effort: 2 hours
   - Confidence: Medium (75%)

**After Fixes**: CLS = 0.05 ✅ (0.18 → 0.05)

---

### 5. API Performance: ✅ Good

**Average Response Time**: 180ms (Target: <300ms)

**No Critical Issues**, but opportunities:

1. **Add Redis caching** 🟢 P2
   ```csharp
   // Cache expensive user dashboard data
   var cachedData = await _cache.GetAsync<DashboardData>($"dashboard:{userId}");
   if (cachedData != null) return cachedData;
   
   var data = await _db.GetDashboardData(userId);
   await _cache.SetAsync($"dashboard:{userId}", data, TimeSpan.FromMinutes(5));
   ```
   - Impact: 180ms → 15ms (92% faster)
   - Effort: 4 hours (setup Redis + 5 endpoints)
   - Confidence: High (90%)

2. **N+1 Query in Orders endpoint** 🟡 P1
   ```csharp
   // Bad: 1 query + N queries
   var orders = _db.Orders.Where(o => o.UserId == userId).ToList();
   foreach (var order in orders) {
       order.Customer = _db.Customers.Find(order.CustomerId);
   }
   
   // Good: Single query with JOIN
   var orders = _db.Orders
       .Where(o => o.UserId == userId)
       .Include(o => o.Customer)
       .ToList();
   ```
   - Impact: 450ms → 85ms (81% faster)
   - Effort: 1 hour
   - Confidence: High (95%)

---

## Prioritized Recommendations

### 🔴 P0 - Critical (This Week)

1. **Replace Moment.js with date-fns** (2 hours)
   - Saves 50 KB (19% bundle reduction)
   - Low risk, high impact

2. **Optimize 4 large images** (1 hour)
   - 4.2 MB → 620 KB (85% reduction)
   - LCP: 3.2s → 2.0s

3. **Fix N+1 query in Orders API** (1 hour)
   - 450ms → 85ms (81% faster)
   - Affects 40% of users

### 🟡 P1 - High (This Sprint)

4. **Implement code splitting** (4 hours)
   - Initial bundle: 456 KB → 130 KB (72% reduction)
   - LCP: 2.0s → 1.7s

5. **Add image dimensions** (1 hour)
   - CLS: 0.18 → 0.10
   - Prevents layout shifts

6. **Lazy load 23 images** (30 min)
   - Faster initial render
   - Better mobile experience

### 🟢 P2 - Medium (This Month)

7. **Setup Redis caching** (4 hours)
   - 5 API endpoints: 180ms → 15ms
   - 92% faster for cached requests

8. **Inline critical CSS** (3 hours)
   - LCP: 1.7s → 1.4s
   - Eliminate render-blocking CSS

---

## Expected Impact

```yaml
before:
  lighthouse_score: 68/100
  lcp: 3.2s
  cls: 0.18
  bundle_size: 847 KB (302 KB gzipped)
  api_avg: 180ms

after_all_fixes:
  lighthouse_score: 92/100 ✅ +24 points
  lcp: 1.4s ✅ -1.8s (56% faster)
  cls: 0.05 ✅ -0.13 (72% better)
  bundle_size: 540 KB (192 KB gzipped) ✅ -36%
  api_avg: 45ms ✅ -75% (with caching)

user_impact:
  - Bounce rate: -25% (faster = less abandonment)
  - SEO ranking: +15% (Core Web Vitals factor)
  - User satisfaction: +30%
```

---

## Monitoring & Alerts

```yaml
setup:
  lighthouse_ci:
    command: "lhci autorun"
    thresholds:
      performance: ">= 90"
      lcp: "< 2.5s"
      cls: "< 0.1"
    action: "Fail CI if thresholds not met"
    
  real_user_monitoring:
    tool: "Google Analytics, Sentry Performance"
    metrics: "LCP, FID, CLS from real users"
    alerts:
      - "LCP > 3s for 5% of users"
      - "CLS > 0.15 for 10% of users"

  api_monitoring:
    tool: "Application Insights, New Relic"
    alerts:
      - "Endpoint response > 1s"
      - "Error rate > 1%"
```

---

## Testing Checklist

```yaml
before_deployment:
  - [ ] Run Lighthouse on staging (mobile + desktop)
  - [ ] Verify bundle sizes (< targets)
  - [ ] Test on slow 3G network (Chrome DevTools)
  - [ ] Check Core Web Vitals in PageSpeed Insights
  - [ ] Profile critical user flows (DevTools Performance tab)
  
after_deployment:
  - [ ] Monitor RUM for 48 hours
  - [ ] Check for regressions (Lighthouse CI)
  - [ ] Verify caching working (check Redis hits)
```

---

## Confidence Summary

```yaml
measurements:
  bundle_size: "high_95%"  # Exact numbers
  core_web_vitals: "high_92%"  # Lighthouse reliable
  image_optimization: "high_95%"  # Measurable
  
recommendations:
  bundle_optimization: "high_92%"  # Proven techniques
  image_optimization: "high_95%"  # Low risk
  code_splitting: "high_90%"  # Standard practice
  api_caching: "high_88%"  # Infrastructure dependent
  inline_css: "medium_75%"  # Requires careful testing
```

---

**Analysis Complete** | Performance Score: 68 → 92 (projected) | Next Review: 1 week
