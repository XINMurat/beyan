# Performans Ä°yileÅŸtirme Rehberi

Bu dosya, performans analizi sonucu bulunan sorunlarÄ± nasÄ±l optimize edeceÄŸinizi adÄ±m adÄ±m aÃ§Ä±klar.

---

## 1. Bundle Size KÃ¼Ã§Ã¼ltme

### âŒ Sorun

Bundle size Ã§ok bÃ¼yÃ¼k: 847 KB (hedef: <200 KB)

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Bundle Analizi

```bash
# Webpack bundle analyzer
npm install --save-dev webpack-bundle-analyzer

# package.json'a ekle
"scripts": {
  "analyze": "webpack-bundle-analyzer build/stats.json"
}

# Ã‡alÄ±ÅŸtÄ±r
npm run build -- --stats
npm run analyze
```

#### AdÄ±m 2: En BÃ¼yÃ¼k Package'larÄ± Belirle

Analyzer'da gÃ¶receksin:
- `moment.js`: 67 KB
- `lodash`: 72 KB  
- KullanÄ±lmayan dependencies

#### AdÄ±m 3: Moment.js â†’ date-fns

```bash
# Moment.js'i kaldÄ±r
npm uninstall moment

# date-fns ekle (2 KB modÃ¼ler)
npm install date-fns
```

```typescript
// âŒ Ã–ncesi: Moment.js
import moment from 'moment';
const formatted = moment(date).format('DD.MM.YYYY');

// âœ… SonrasÄ±: date-fns
import { format } from 'date-fns';
import { tr } from 'date-fns/locale';
const formatted = format(date, 'dd.MM.yyyy', { locale: tr });
```

**Tasarruf**: 67 KB â†’ 2 KB = -65 KB

#### AdÄ±m 4: Lodash â†’ Native JS / Lodash-es

```bash
# EÄŸer tÃ¼m lodash kullanÄ±lÄ±yorsa
npm uninstall lodash
npm install lodash-es  # Tree-shakeable
```

```typescript
// âŒ Ã–ncesi: TÃ¼m lodash import
import _ from 'lodash';
_.uniq([1,2,2,3]);

// âœ… SonrasÄ±: Sadece gerekli fonksiyon
import uniq from 'lodash-es/uniq';
uniq([1,2,2,3]);

// VEYA Native JS
[...new Set([1,2,2,3])];
```

**Tasarruf**: 72 KB â†’ 5 KB = -67 KB

#### AdÄ±m 5: Code Splitting

```typescript
// React lazy loading
import { lazy, Suspense } from 'react';

// âŒ Ã–ncesi: Hepsi main bundle'da
import AdminDashboard from './AdminDashboard';

// âœ… SonrasÄ±: Lazy load
const AdminDashboard = lazy(() => import('./AdminDashboard'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <AdminDashboard />
    </Suspense>
  );
}
```

#### AdÄ±m 6: Ã–lÃ§ & DoÄŸrula

```bash
npm run build
# Bundle size kontrol
ls -lh build/static/js/*.js
```

**Checklist**:
- [ ] Bundle analizi yapÄ±ldÄ±
- [ ] BÃ¼yÃ¼k dependencies deÄŸiÅŸtirildi
- [ ] Code splitting eklendi
- [ ] Bundle size <200 KB

---

## 2. Image Optimization

### âŒ Sorun

Hero image 2.4 MB â†’ LCP 3.2 saniye

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: WebP/AVIF'e DÃ¶nÃ¼ÅŸtÃ¼r

```bash
# ImageMagick ile
convert hero.jpg -quality 80 hero.webp
convert hero.jpg -quality 80 hero.avif

# Veya online tool: squoosh.app
```

**Boyut**: 2.4 MB â†’ 340 KB (WebP) = -86%

#### AdÄ±m 2: Responsive Images

```html
<!-- âŒ Ã–ncesi: Tek boyut -->
<img src="hero.jpg" alt="Hero" />

<!-- âœ… SonrasÄ±: Responsive + modern format -->
<picture>
  <source
    srcset="hero-small.avif 400w, hero-large.avif 1200w"
    type="image/avif"
    sizes="(max-width: 768px) 400px, 1200px"
  />
  <source
    srcset="hero-small.webp 400w, hero-large.webp 1200w"
    type="image/webp"
    sizes="(max-width: 768px) 400px, 1200px"
  />
  <img
    src="hero.jpg"
    alt="Hero image"
    loading="lazy"
  />
</picture>
```

#### AdÄ±m 3: Lazy Loading

```html
<!-- Native lazy loading -->
<img src="product.jpg" alt="Product" loading="lazy" />
```

**Checklist**:
- [ ] BÃ¼yÃ¼k gÃ¶rseller WebP/AVIF'e dÃ¶nÃ¼ÅŸtÃ¼rÃ¼ldÃ¼
- [ ] Responsive srcset eklendi
- [ ] Lazy loading eklendi
- [ ] LCP <2.5s

---

## 3. N+1 Query DÃ¼zeltme

### âŒ Sorun

Orders endpoint'te 347 query (1+N pattern)

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: N+1 Tespit Et

```bash
# EF Core query log'larÄ±nÄ± aÃ§
# appsettings.Development.json
{
  "Logging": {
    "LogLevel": {
      "Microsoft.EntityFrameworkCore.Database.Command": "Information"
    }
  }
}
```

Log'da gÃ¶receksin:
```
SELECT * FROM Users
SELECT * FROM Orders WHERE UserId = 1
SELECT * FROM Orders WHERE UserId = 2
SELECT * FROM Orders WHERE UserId = 3
...
```

#### AdÄ±m 2: Eager Loading Ekle

```csharp
// âŒ Ã–ncesi: N+1
var users = _context.Users.ToList();
foreach (var user in users)
{
    user.Orders = _context.Orders
        .Where(o => o.UserId == user.Id)
        .ToList();
}

// âœ… SonrasÄ±: 1 query
var users = _context.Users
    .Include(u => u.Orders)
        .ThenInclude(o => o.OrderItems)
    .ToList();
```

#### AdÄ±m 3: Performans Ã–lÃ§Ã¼mÃ¼

```csharp
// Ã–nce
var stopwatch = Stopwatch.StartNew();
var users = GetUsersOld();
stopwatch.Stop();
Console.WriteLine($"Old: {stopwatch.ElapsedMilliseconds}ms");

// Sonra
stopwatch.Restart();
var usersNew = GetUsersNew();
stopwatch.Stop();
Console.WriteLine($"New: {stopwatch.ElapsedMilliseconds}ms");
```

**Ä°yileÅŸtirme**: 2,400ms â†’ 85ms (96% daha hÄ±zlÄ±)

**Checklist**:
- [ ] N+1 query'ler tespit edildi
- [ ] Eager loading eklendi
- [ ] Performans Ã¶lÃ§Ã¼ldÃ¼
- [ ] API response time <100ms

---

## 4. Database Index Ekleme

### âŒ Sorun

`Orders.CustomerId` Ã¼zerinde index yok â†’ 850ms query

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Missing Index Tespit Et

```sql
-- SQL Server: Missing index recommendation
SELECT 
    OBJECT_NAME(s.object_id) AS TableName,
    i.name AS IndexName,
    s.user_seeks,
    s.user_scans
FROM sys.dm_db_index_usage_stats s
JOIN sys.indexes i ON s.object_id = i.object_id
WHERE s.user_seeks = 0 AND s.user_scans > 1000;
```

#### AdÄ±m 2: EF Migration OluÅŸtur

```csharp
// Migration
public partial class AddIndexCustomerId : Migration
{
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.CreateIndex(
            name: "IX_Orders_CustomerId",
            table: "Orders",
            column: "CustomerId");
    }

    protected override void Down(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.DropIndex(
            name: "IX_Orders_CustomerId",
            table: "Orders");
    }
}
```

#### AdÄ±m 3: Production'da Dikkatli Ã‡alÄ±ÅŸtÄ±r

```bash
# Ã–NCE: Backup al
pg_dump production_db > backup.sql

# Maintenance window'da Ã§alÄ±ÅŸtÄ±r
dotnet ef database update --connection "[PROD_CONNECTION]"

# Index oluÅŸturulurken table lock olabilir!
# BÃ¼yÃ¼k tablolarda ONLINE index oluÅŸtur:
```

```sql
-- PostgreSQL: CONCURRENT index (lock yok)
CREATE INDEX CONCURRENTLY IX_Orders_CustomerId 
ON Orders (CustomerId);
```

**Ä°yileÅŸtirme**: 850ms â†’ 8ms (99% daha hÄ±zlÄ±)

**Checklist**:
- [ ] Missing indexes tespit edildi
- [ ] Migration oluÅŸturuldu
- [ ] Staging'de test edildi
- [ ] Production'da gÃ¼venle deploy edildi

---

## 5. Build SÃ¼resi Optimize Etme

### âŒ Sorun

Build sÃ¼resi 85 saniye (hedef: <30s)

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: TypeScript Incremental Compile

```json
// tsconfig.json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo"
  }
}
```

**Ä°yileÅŸtirme**: Ä°lk build 85s, sonraki build'ler 15s

#### AdÄ±m 2: Webpack Cache

```javascript
// webpack.config.js
module.exports = {
  cache: {
    type: 'filesystem',
    buildDependencies: {
      config: [__filename]
    }
  }
};
```

#### AdÄ±m 3: Thread Loader (Parallel Processing)

```bash
npm install --save-dev thread-loader
```

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: [
          'thread-loader',
          'ts-loader'
        ]
      }
    ]
  }
};
```

**Ä°yileÅŸtirme**: 85s â†’ 25s (71% daha hÄ±zlÄ±)

**Checklist**:
- [ ] Incremental compile aktif
- [ ] Cache enabled
- [ ] Parallel processing aktif
- [ ] Build <30s

---

## 6. API Response Time Ä°yileÅŸtirme

### âŒ Sorun

`/api/products` endpoint 1,200ms (hedef: <100ms)

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Response Cache

```csharp
// Program.cs
builder.Services.AddResponseCaching();
app.UseResponseCaching();

// Controller
[ResponseCache(Duration = 60)]  // 60 saniye cache
[HttpGet]
public IActionResult GetProducts()
{
    var products = _context.Products.ToList();
    return Ok(products);
}
```

#### AdÄ±m 2: Redis Cache (Daha GeliÅŸmiÅŸ)

```bash
dotnet add package StackExchange.Redis
```

```csharp
public class ProductService
{
    private readonly IDatabase _redis;
    
    public async Task<List<Product>> GetProductsAsync()
    {
        var cacheKey = "products:all";
        var cached = await _redis.StringGetAsync(cacheKey);
        
        if (!cached.IsNullOrEmpty)
        {
            return JsonSerializer.Deserialize<List<Product>>(cached);
        }
        
        var products = await _context.Products.ToListAsync();
        
        await _redis.StringSetAsync(
            cacheKey,
            JsonSerializer.Serialize(products),
            TimeSpan.FromMinutes(5)
        );
        
        return products;
    }
}
```

**Ä°yileÅŸtirme**: 
- Ä°lk istek: 1,200ms
- Cached istek: 15ms (98% daha hÄ±zlÄ±)

**Checklist**:
- [ ] Response caching eklendi
- [ ] Redis kuruldu (optional)
- [ ] Cache invalidation stratejisi belirlendi
- [ ] API response <100ms

---

## 7. Lazy Loading (React)

### âŒ Sorun

TÃ¼m componentler initial load'da yÃ¼kleniyor

### âœ… Ã‡Ã¶zÃ¼m

```typescript
// âŒ Ã–ncesi
import AdminDashboard from './AdminDashboard';
import UserProfile from './UserProfile';
import Settings from './Settings';

// âœ… SonrasÄ±: Lazy load
import { lazy, Suspense } from 'react';

const AdminDashboard = lazy(() => import('./AdminDashboard'));
const UserProfile = lazy(() => import('./UserProfile'));
const Settings = lazy(() => import('./Settings'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Routes>
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/profile" element={<UserProfile />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}
```

**Ä°yileÅŸtirme**: Initial bundle 847 KB â†’ 320 KB

---

## ðŸ“Š Performans Metrikleri

### Core Web Vitals Hedefleri

| Metric | Ä°yi | Orta | KÃ¶tÃ¼ |
|--------|-----|------|------|
| LCP (Largest Contentful Paint) | <2.5s | 2.5-4s | >4s |
| FID (First Input Delay) | <100ms | 100-300ms | >300ms |
| CLS (Cumulative Layout Shift) | <0.1 | 0.1-0.25 | >0.25 |

### Ã–lÃ§Ã¼m AraÃ§larÄ±

```bash
# Lighthouse
lighthouse https://yoursite.com --view

# WebPageTest
# https://www.webpagetest.org/

# Chrome DevTools
# Performance tab â†’ Record
```

---

## ðŸ” SÃ¼rekli Ä°zleme

### Lighthouse CI

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on: [push]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Lighthouse
        uses: treosh/lighthouse-ci-action@v9
        with:
          urls: |
            https://yoursite.com
            https://yoursite.com/products
          uploadArtifacts: true
```

**Checklist**:
- [ ] Lighthouse CI kuruldu
- [ ] Performance budget belirlendi
- [ ] Otomatik alert'ler aktif

---

**Son GÃ¼ncelleme**: AralÄ±k 2024
