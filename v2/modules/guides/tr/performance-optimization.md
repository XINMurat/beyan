# Guide: Performans Optimizasyonu Adımları

**Modül Türü**: Uygulama Rehberi (How-to Guide)
**Priority**: P3
**Hedef Kitle**: Full-Stack Geliştiriciler

---

## Purpose
Performans analizi bulgularına karşılık gelen somut, uygulanabilir optimizasyon tekniklerini frontend ve backend katmanları için ayrı ayrı açıklar.

---

## Frontend Optimizasyonları

### 1. Code Splitting ve Lazy Loading (React)
```javascript
// ❌ YANLIŞ: Tüm sayfalar tek bundle'da, ilk yükleme ağır
import AdminPanel from './pages/AdminPanel';
import Dashboard from './pages/Dashboard';

// ✅ DOĞRU: Sadece ziyaret edilen sayfa yüklenir
const AdminPanel = React.lazy(() => import('./pages/AdminPanel'));
const Dashboard = React.lazy(() => import('./pages/Dashboard'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Routes>
        <Route path="/admin" element={<AdminPanel />} />
        <Route path="/" element={<Dashboard />} />
      </Routes>
    </Suspense>
  );
}
```

### 2. Resim Optimizasyonu
```html
<!-- ❌ YANLIŞ: Her cihaz aynı büyük resmi indirir -->
<img src="hero-image.jpg" />

<!-- ✅ DOĞRU: Tarayıcı ekran boyutuna göre doğru resmi seçer -->
<img
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"
  src="hero-800.webp"
  loading="lazy"
  alt="Ana sayfa görseli"
/>
```

---

## Backend Optimizasyonları

### 3. Veritabanı Sorgu Optimizasyonu

```sql
-- ❌ YANLIŞ: Index yok, Full Table Scan yapıyor
SELECT * FROM orders WHERE customer_email = 'user@example.com';

-- ✅ DOĞRU: Index ekle
CREATE INDEX idx_orders_email ON orders(customer_email);

-- ✅ DOĞRU: Sadece gerekli sütunları çek (SELECT * yerine)
SELECT id, created_at, total_amount
FROM orders
WHERE customer_email = 'user@example.com';
```

### 4. Caching Katmanı (Redis)

```python
# ❌ YANLIŞ: Her request'te DB'ye gidiliyor
def get_product(product_id):
    return db.query(f"SELECT * FROM products WHERE id = {product_id}")

# ✅ DOĞRU: Önce cache'e bak, yoksa DB'den al ve cache'e yaz
import redis
cache = redis.Redis()

def get_product(product_id):
    cached = cache.get(f"product:{product_id}")
    if cached:
        return json.loads(cached)
    
    product = db.query("SELECT * FROM products WHERE id = ?", product_id)
    cache.setex(f"product:{product_id}", 3600, json.dumps(product))  # 1 saat TTL
    return product
```

---

## Hızlı Kontrol Listesi

- [ ] Bundle analyzer çalıştırıldı, büyük bağımlılıklar tespit edildi mi?
- [ ] Route bazlı lazy loading uygulandı mı?
- [ ] Sık sorgulanan sütunlara index eklendi mi?
- [ ] Hot path'ler için cache mekanizması kuruldu mu?
- [ ] Resimler WebP formatına dönüştürüldü mü?
