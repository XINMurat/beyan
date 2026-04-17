# Module: UMT Architecture Analysis

**Priority**: P1 (For UMT Projects)  
**Tokens**: ~2000  

## UMT Principles

```yaml
table_driven:
  logic_in_tables: "Business rules stored in DB tables"
  runtime_execution: "UMT Runtime reads and executes"
  no_hardcoded_logic: "Minimal code, maximum configuration"
```

## Turkish Output

```markdown
# UMT Mimari Analizi

## UMT Uyumluluk: 7/10 🟡

### Bulgular

#### 1. 🟡 Hardcoded Business Logic (3 yer)

**Sorun**: Controller'da iş mantığı var (UMT'de olmamalı)

```csharp
// ❌ Hardcoded: Controller'da logic
public IActionResult CalculateDiscount(Order order) {
    if (order.Total > 1000) {
        order.Discount = order.Total * 0.10;
    }
}

// ✅ UMT: Table-driven
// DiscountRules tablosundan oku
var rule = _umt.GetRule("discount", order.Total);
order.Discount = _umt.Execute(rule, order);
```

**Çaba**: 2 gün
**Güven**: Yüksek (%85)

---

#### 2. ✅ UMT Runtime İyi Kullanılmış

**İyi Örnekler**:
- Validation rules table-driven ✅
- Workflow engine UMT-based ✅
- Permission system table-driven ✅

---

## Öneriler

### 🔴 P0
1. Hardcoded logic'i UMT'ye taşı (2 gün)
2. UMT table schema dokümante et (1 gün)

**Hedef**: %95+ UMT uyumluluğu

---

**Analiz Tamamlandı** | UMT Skoru: 7/10
```
