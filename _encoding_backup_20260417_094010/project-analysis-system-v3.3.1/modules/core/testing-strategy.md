# Module: Testing Strategy Analysis

**Priority**: P2  
**Tokens**: ~2000  
**Analysis Time**: 10-12 minutes  

## Test Pyramid

```yaml
ideal_distribution:
  unit: "70% (fast, isolated)"
  integration: "20% (moderate speed)"
  e2e: "10% (slow, brittle)"

anti_pattern:
  ice_cream_cone: "Mostly E2E tests (slow, flaky)"
  hourglass: "Unit + E2E, no integration"
```

## Turkish Output

```markdown
# Test Stratejisi Analizi

## Test Coverage: %78 ✅
## Test Piramidi: 🔴 Ters piramit (sorunlu)

### Bulgular

#### 1. 🔴 Test Dağılımı Sorunlu

**Mevcut**:
- Unit: %30 (az)
- Integration: %10 (çok az)
- E2E: %60 (çok fazla!)

**İdeal**:
- Unit: %70
- Integration: %20
- E2E: %10

**Sorun**: E2E testler yavaş (15 dakika) ve sık başarısız oluyor

**Çözüm**:
```typescript
// ❌ E2E test: Yavaş, kırılgan
test('user can place order', async () => {
  await page.goto('/');
  await page.click('[data-test=login]');
  // ... 50 satır daha
});

// ✅ Unit test: Hızlı, güvenilir
test('calculateTotal sums prices correctly', () => {
  const total = calculateTotal([10, 20, 30]);
  expect(total).toBe(60);
});
```

**Çaba**: 1 hafta (E2E → Unit migration)
**Etki**: Test süresi 15 dk → 2 dk
**Güven**: Yüksek (%90)

---

#### 2. 🟡 Flaky Tests (5 test)

**Sorun**: Bazen geçiyor, bazen başarısız

```typescript
// ❌ Flaky: Timing'e bağımlı
test('shows loading spinner', () => {
  fetchData();
  expect(screen.getByRole('progressbar')).toBeInTheDocument();
  // Race condition!
});

// ✅ Kararlı: async/await
test('shows loading spinner', async () => {
  fetchData();
  await waitFor(() => 
    expect(screen.getByRole('progressbar')).toBeInTheDocument()
  );
});
```

**Çaba**: 2 saat
**Güven**: Yüksek (%95)

---

## Öneriler

### 🔴 P0
1. Flaky testleri düzelt (2 saat)
2. Test timeout'ları artır (30 dakika)

### 🟡 P1
3. Unit test coverage %70'e çıkar (1 hafta)
4. Integration test ekle (3 gün)

**Hedef**: Güvenilir, hızlı test suite

---

**Analiz Tamamlandı** | Test Kalitesi: 7/10
```
