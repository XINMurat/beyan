# Performans İyile�?tirme Rehberi

Bu dosya, performans analizi sonucu bulunan sorunları nasıl optimize edece�?inizi adım adım açıklar.

---

## 1. Bundle Size Küçültme

### �? Sorun

Bundle size çok büyük: 847 KB (hedef: <200 KB)

### �?? �?özüm: Adım Adım

#### Adım 1: Bundle Analizi

```bash
# Webpack bundle analyzer
npm install --save-dev webpack-bundle-analyzer

# package.json'a ekle
"scripts": {
  "analyze": "webpack-bundle-analyzer build/stats.json"
}

# �?alı�?tır
npm run build -- --stats
npm run analyze
```

#### Adım 2: En Büyük Package'ları Belirle

Analyzer'da göreceksin:
- `moment.js`: 67 KB
- `lodash`: 72 KB  
- Kullanılmayan dependencies

#### Adım 3: Moment.js �?? date-fns

```bash
# Moment.js'i kaldır
npm uninstall moment

# date-fns ekle (2 KB modüler)
npm install date-fns
```

```typescript
// �? �?ncesi: Moment.js
import moment from 'moment';
const formatted = moment(date).format('DD.MM.YYYY');

// �?? Sonrası: date-fns
import { format } from 'date-fns';
import { tr } from 'date-fns/locale';
const formatted = format(date, 'dd.MM.yyyy', { locale: tr });
```

**Tasarruf**: 67 KB �?? 2 KB = -65 KB

#### Adım 4: Lodash �?? Native JS / Lodash-es

```bash
# E�?er tüm lodash kullanılıyorsa
npm uninstall lodash
npm install lodash-es  # Tree-shakeable
```

```typescript
// �? �?ncesi: Tüm lodash import
import _ from 'lodash';
_.uniq([1,2,2,3]);

// �?? Sonrası: Sadece gerekli fonksiyon
import uniq from 'lodash-es/uniq';
uniq([1,2,2,3]);

// VEYA Native JS
[...new Set([1,2,2,3])];
```

**Tasarruf**: 72 KB �?? 5 KB = -67 KB

#### Adım 5: Code Splitting

```typescript
// React lazy loading
import { lazy, Suspense } from 'react';

// �? �?ncesi: Hepsi main bundle'da
import AdminDashboard from './AdminDashboard';

// �?? Sonrası: Lazy load
const AdminDashboard = lazy(() => import('./AdminDashboard'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <AdminDashboard />
    </Suspense>
  );
}
```

#### Adım 6: �?lç & Do�?rula

```bash
npm run build
# Bundle size kontrol
ls -lh build/static/js/*.js
```

**Checklist**:
- [ ] Bundle analizi yapıldı
- [ ] Büyük dependencies de�?i�?tirildi
- [ ] Code splitting eklendi
- [ ] Bundle size <200 KB

---

## 2. Image Optimization

### �? Sorun

Hero image 2.4 MB �?? LCP 3.2 saniye

### �?? �?özüm: Adım Adım

#### Adım 1: WebP/AVIF'e Dönü�?tür

```bash
# ImageMagick ile
convert hero.jpg -quality 80 hero.webp
convert hero.jpg -quality 80 hero.avif

# Veya online tool: squoosh.app
```

**Boyut**: 2.4 MB �?? 340 KB (WebP) = -86%

#### Adım 2: Responsive Images

```html
<!-- �? �?ncesi: Tek boyut -->
<img src="hero.jpg" alt="Hero" />

<!-- �?? Sonrası: Responsive + modern format -->
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

#### Adım 3: Lazy Loading

```html
<!-- Native lazy loading -->
<img src="product.jpg" alt="Product" loading="lazy" />
```

**Checklist**:
- [ ] Büyük görseller WebP/AVIF'e dönü�?türüldü
- [ ] Responsive srcset eklendi
- [ ] Lazy loading eklendi
- [ ] LCP <2.5s

---

## 3. N+1 Query Düzeltme

### �? Sorun

Orders endpoint'te 347 query (1+N pattern)

### �?? �?özüm: Adım Adım

#### Adım 1: N+1 Tespit Et

```bash
# EF Core query log'larını aç
# appsettings.Development.json
{
  "Logging": {
    "LogLevel": {
      "Microsoft.EntityFrameworkCore.Database.Command": "Information"
    }
  }
}
```

Log'da göreceksin:
```
SELECT * FROM Users
SELECT * FROM Orders WHERE UserId = 1
SELECT * FROM Orders WHERE UserId = 2
SELECT * FROM Orders WHERE UserId = 3
...
```

#### Adım 2: Eager Loading Ekle

```csharp
// �? �?ncesi: N+1
var users = _context.Users.ToList();
foreach (var user in users)
{
    user.Orders = _context.Orders
        .Where(o => o.UserId == user.Id)
        .ToList();
}

// �?? Sonrası: 1 query
var users = _context.Users
    .Include(u => u.Orders)
        .ThenInclude(o => o.OrderItems)
    .ToList();
```

#### Adım 3: Performans �?lçümü

```csharp
// �?nce
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

**İyile�?tirme**: 2,400ms �?? 85ms (96% daha hızlı)

**Checklist**:
- [ ] N+1 query'ler tespit edildi
- [ ] Eager loading eklendi
- [ ] Performans ölçüldü
- [ ] API response time <100ms

---

## 4. Database Index Ekleme

### �? Sorun

`Orders.CustomerId` üzerinde index yok �?? 850ms query

### �?? �?özüm: Adım Adım

#### Adım 1: Missing Index Tespit Et

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

#### Adım 2: EF Migration Olu�?tur

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

#### Adım 3: Production'da Dikkatli �?alı�?tır

```bash
# �?NCE: Backup al
pg_dump production_db > backup.sql

# Maintenance window'da çalı�?tır
dotnet ef database update --connection "[PROD_CONNECTION]"

# Index olu�?turulurken table lock olabilir!
# Büyük tablolarda ONLINE index olu�?tur:
```

```sql
-- PostgreSQL: CONCURRENT index (lock yok)
CREATE INDEX CONCURRENTLY IX_Orders_CustomerId 
ON Orders (CustomerId);
```

**İyile�?tirme**: 850ms �?? 8ms (99% daha hızlı)

**Checklist**:
- [ ] Missing indexes tespit edildi
- [ ] Migration olu�?turuldu
- [ ] Staging'de test edildi
- [ ] Production'da güvenle deploy edildi

---

## 5. Build Süresi Optimize Etme

### �? Sorun

Build süresi 85 saniye (hedef: <30s)

### �?? �?özüm: Adım Adım

#### Adım 1: TypeScript Incremental Compile

```json
// tsconfig.json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo"
  }
}
```

**İyile�?tirme**: İlk build 85s, sonraki build'ler 15s

#### Adım 2: Webpack Cache

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

#### Adım 3: Thread Loader (Parallel Processing)

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

**İyile�?tirme**: 85s �?? 25s (71% daha hızlı)

**Checklist**:
- [ ] Incremental compile aktif
- [ ] Cache enabled
- [ ] Parallel processing aktif
- [ ] Build <30s

---

## 6. API Response Time İyile�?tirme

### �? Sorun

`/api/products` endpoint 1,200ms (hedef: <100ms)

### �?? �?özüm: Adım Adım

#### Adım 1: Response Cache

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

#### Adım 2: Redis Cache (Daha Geli�?mi�?)

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

**İyile�?tirme**: 
- İlk istek: 1,200ms
- Cached istek: 15ms (98% daha hızlı)

**Checklist**:
- [ ] Response caching eklendi
- [ ] Redis kuruldu (optional)
- [ ] Cache invalidation stratejisi belirlendi
- [ ] API response <100ms

---

## 7. Lazy Loading (React)

### �? Sorun

Tüm componentler initial load'da yükleniyor

### �?? �?özüm

```typescript
// �? �?ncesi
import AdminDashboard from './AdminDashboard';
import UserProfile from './UserProfile';
import Settings from './Settings';

// �?? Sonrası: Lazy load
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

**İyile�?tirme**: Initial bundle 847 KB �?? 320 KB

---

## �??? Performans Metrikleri

### Core Web Vitals Hedefleri

| Metric | İyi | Orta | Kötü |
|--------|-----|------|------|
| LCP (Largest Contentful Paint) | <2.5s | 2.5-4s | >4s |
| FID (First Input Delay) | <100ms | 100-300ms | >300ms |
| CLS (Cumulative Layout Shift) | <0.1 | 0.1-0.25 | >0.25 |

### �?lçüm Araçları

```bash
# Lighthouse
lighthouse https://yoursite.com --view

# WebPageTest
# https://www.webpagetest.org/

# Chrome DevTools
# Performance tab �?? Record
```

---

## �??� Sürekli İzleme

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

**Son Güncelleme**: Aralık 2024
