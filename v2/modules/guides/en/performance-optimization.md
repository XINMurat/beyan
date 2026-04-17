# Guide: Performance Optimization Steps

**Module Type**: Implementation Guide
**Priority**: P3

---

## Purpose
Provides actionable performance optimizations mapped directly to findings from the performance analysis module.

---

## Frontend Optimizations

### Route-based Code Splitting
```javascript
// ❌ WRONG: Everything bundled together
import AdminPanel from './pages/AdminPanel';

// ✅ CORRECT: Load page only when visited
const AdminPanel = React.lazy(() => import('./pages/AdminPanel'));
```

### Image Optimization
```html
<img
  srcset="hero-400.webp 400w, hero-800.webp 800w"
  sizes="(max-width: 600px) 400px, 800px"
  src="hero-800.webp"
  loading="lazy"
  alt="Hero image"
/>
```

---

## Backend Optimizations

### Database Index
```sql
-- Slow: Full table scan
SELECT * FROM orders WHERE customer_email = 'user@example.com';

-- Add index
CREATE INDEX idx_orders_email ON orders(customer_email);
```

### Redis Caching
```python
def get_product(product_id):
    cached = cache.get(f"product:{product_id}")
    if cached:
        return json.loads(cached)
    product = db.query("SELECT * FROM products WHERE id = ?", product_id)
    cache.setex(f"product:{product_id}", 3600, json.dumps(product))
    return product
```

## Quick Checklist

- [ ] Bundle analyzer run, large dependencies identified?
- [ ] Route-based lazy loading implemented?
- [ ] High-traffic columns indexed?
- [ ] Hot path data cached with Redis/Memcached?
- [ ] Images converted to WebP with srcset?
