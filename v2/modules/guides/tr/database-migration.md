# Guide: Güvenli Veritabanı Migration Rehberi

**Modül Türü**: Uygulama Rehberi (How-to Guide)
**Priority**: P3
**Hedef Kitle**: Backend Geliştiriciler ve DBA'lar

---

## Purpose
Veritabanı şeması değişikliklerini production'da sıfır kesinti (Zero-Downtime) ile uygulamanın adım adım rehberidir.

---

## 1. Migration Stratejisinin Seçimi

```yaml
migration_tools:
  flyway:
    ideal: "Java/.NET projeleri, SQL-first yaklaşım"
    pros: "Basit, SQL dosyaları ile çalışır"
    cons: "Rollback manuel"
  liquibase:
    ideal: "XML/YAML/JSON tabanlı, çok veritabanı desteği"
    pros: "Rollback otomatik, changelog detaylı"
  ef_core_migrations:
    ideal: "C# / .NET projeleri"
    pros: "Code-first, ORM entegreli"
    cons: "Büyük projelerde yavaşlayabilir"
```

---

## 2. Zero-Downtime Migration Adımları

Büyük tablolarda tek seferde ALTER TABLE yapmak production'ı kilitler. Güvenli yaklaşım:

**Örnek: Yeni bir sütun (column) eklemek**

```sql
-- ADIM 1: Nullable sütun ekle (tablo kilitlenmez)
ALTER TABLE orders ADD COLUMN discount_amount DECIMAL(10,2) NULL;

-- ADIM 2: Mevcut veriler için default değer uygula (batch'ler halinde)
UPDATE orders SET discount_amount = 0 WHERE discount_amount IS NULL LIMIT 5000;
-- (Bu adımı tüm satırlar dolana kadar tekrarla)

-- ADIM 3: Kod her iki sütunu da destekledikten sonra NOT NULL yap
ALTER TABLE orders MODIFY COLUMN discount_amount DECIMAL(10,2) NOT NULL DEFAULT 0;
```

---

## 3. Rollback Stratejisi

Her migration'ın geri alınabilir olması şarttır:

```sql
-- Flyway rollback script örneği (V2__add_discount.sql ile birlikte)
-- U2__add_discount.sql (Undo migration)
ALTER TABLE orders DROP COLUMN discount_amount;
```

**Altın Kural:** Yeni bir sütun/tablo eklemek genellikle geri alınabilirdir. Sütun silmek veya veri dönüştürmek **geri alınamaz** — önce backup alın!

---

## Hızlı Kontrol Listesi

- [ ] Migration öncesi veritabanı backup'ı alındı mı?
- [ ] Migration staging ortamında test edildi mi?
- [ ] Rollback script'i yazıldı ve test edildi mi?
- [ ] Büyük tablolar için batch güncelleme planlandı mı?
- [ ] CI/CD pipeline'ında migration otomatikleştirildi mi?