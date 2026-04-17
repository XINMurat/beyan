# Module: Büyüme Stratejisi ve Prompt Ailesi Yönetimi

**Priority**: P3 (Çerçeve Yönetimi)
**Tokens**: ~2000
**Analysis Time**: Manuel tetikleme — yeni modül eklenirken veya dönemsel gözden geçirmede

---

## Purpose
Bu modül, Beyan v2.0 sisteminin **kendisini nasıl büyüteceğini** ve yönetileceğini tanımlar. Yeni analiz modülü eklenirken hangi standartların izleneceğini, mevcut modüllerin nasıl güncelleneceğini ve sistemin periyodik olarak nasıl gözden geçirileceğini kurallaştırır.

---

## Sistemin Mevcut Yapısı

```
CORE MODÜLLER (23 modül)          DOMAIN MODÜLLER (7 modül)
├── security-analysis              ├── web-mobile
├── performance-analysis           ├── ai-research
├── file-structure-analysis        ├── devops-infra
├── code-quality-patterns          ├── os-firmware
├── database-analysis              ├── blockchain-web3
├── scoring-criteria               ├── data-pipeline
└── ... (17 more)                  └── legacy-migration

ODAK MODÜLLERİ (4 modül)         ÖZEL MODÜLLER (10 modül)
├── api-audit                      ├── project-intelligence
├── security-audit                 ├── react-typescript
├── performance-audit              ├── dotnet-core
└── compliance-audit               └── ... (7 more)

TEST MODÜLLERİ (3 modül)         REHBER MODÜLLERİ (4 modül)
├── test-generation                ├── accessibility-fixes
├── collaboration-test             ├── security-fixes
└── ui-interaction-test            └── ... (2 more)
```

---

## Yeni Modül Ne Zaman Eklenir?

Yeni bir modül eklemeden önce şu üç soruyu cevapla:

**1. Bu gerçekten yeni bir alan mı?**
Mevcut hiçbir modülün kapsamına girmiyorsa yeni modül gerekir.
- *Örnek:* "Oyun motoru analizi" → Mevcut modüllere sığmıyor → `game-engine.md` ekle.

**2. Yoksa mevcut bir modüle bölüm eklemek yeterli mi?**
Kapsam küçükse yeni dosya yerine mevcut modüle alt bölüm ekle.
- *Örnek:* "CLI aracı desteği" → `developer-experience.md`'e not eklemek yeterli.

**3. Yoksa odak bazlı bir ek mi?**
Tüm proje türlerine uygulanabilecek yatay bir lens mi?
- *Örnek:* "Erişilebilirlik denetimi" → `focus/` kategorisine eklenebilir.

---

## Yeni Modül Yazma Standardı

Her yeni modül şu yapıyı zorunlu olarak içermelidir:

```markdown
# Module: [Modül Adı]

**Priority**: [P0/P1/P2/P3]
**Tokens**: [Tahmini token sayısı]
**Analysis Time**: [Ne zaman yüklenir]

---

## Purpose
[Tek paragrafta ne yapar]

---

## [Ana İçerik Bölümleri]
...

---

## Scoring
[excellent/good/attention/critical seviyeleri]

---

## Output Format
[Yapay zekanın üretmesi beklenen rapor formatı]
```

### Zorunlu Kurallar
- ❌ Placeholder içerik bırakılamaz — her örnek gerçek ve doldurulmuş olmalı
- ❌ Modül başlığında proje adı veya kişi adı geçemez
- ✅ Her modülün hem `tr/` hem `en/` versiyonu aynı anda yazılmalı
- ✅ `MANIFEST.yaml`'a eklenmeden modül sisteme dahil edilmez

---

## Mevcut Modül Güncelleme Kuralları

### Ne Zaman Güncellenir?
- Ekosistem değişikliği (ör: React 19 yeni Hook kuralları)
- Mevzuat değişikliği (ör: KVKK güncellemesi)
- Kullanımda tespit edilen boşluk veya hata
- Periyodik gözden geçirme (6 aylık döngü)

### Güncelleme Prosedürü
1. İlgili modül dosyasını aç
2. Değişikliği yap
3. `verify_integrity.ps1` ile sistem bütünlüğünü doğrula
4. Eğer yapısal değişiklikse MANIFEST'teki versiyon notunu güncelle

---

## Periyodik Gözden Geçirme Döngüsü

### Tetikleyiciler
- 5+ yeni modül eklendikten sonra
- Gerçek bir projede uygulamada ciddi boşluk tespit edildiğinde
- 6 ay geçmişse (zaman bazlı)

### Gözden Geçirme Adımları
```yaml
review_steps:
  1: "MANIFEST.yaml'ı incele — stub kalmış modül var mı?"
  2: "verify_integrity.ps1 çalıştır — sıfır hata hedef"
  3: "Token bütçesini kontrol et — 35.000 limitinin üzerinde modül kombinasyonu var mı?"
  4: "Büyüme Stratejisi modülündeki 'Bilinen Boşluklar' tablosunu güncelle"
```

---

## Bilinen Boşluklar ve Gelecek Modüller

Aşağıdaki alanlar bilerek ertelenmiştir — öncelik kazandığında eklenecek:

| Eksik Alan | Öncelik | Tetikleyici Koşul |
|---|---|---|
| Oyun / Game Engine Analiz Modülü | Düşük | Oyun projesi analiz talebi |
| Hardware / FPGA Analiz Modülü | Düşük | Donanım projesi analiz talebi |
| Mikroservis Mimari Özgün Modülü | Orta | Mevcut modüllerin yetersizliği tespit edilirse |
| Erişilebilirlik Odak Denetim Modülü | Düşük | Kamu veya sağlık projesi talebi |
| GraphQL API Tasarım Modülü | Orta | GraphQL projesi analiz talebi |

---

## Scoring

```yaml
scoring:
  excellent: "MANIFEST senkronize, sıfır stub, her modülün EN/TR versiyonu tam, token bütçesi verimli."
  good: "Çoğu modül dolu, 1-2 stub kalmış, bütçe yönetilebilir."
  attention: "5+ stub var, MANIFEST ile fiziksel dosyalar arasında sapma var."
  critical: "MANIFEST tamamen desenkronize, modüllerin yarısı stub, sistem güvenilmez çıktı veriyor."
```

---

## Output Format

```markdown
## 📈 Sistem Büyüme Durumu Raporu

### Mevcut Yapı
- **Toplam Modül:** X (TR: X, EN: X)
- **Dolu Modül:** X
- **Stub Kalan:** X

### Token Bütçesi
- **Ortalama Yük:** X / 35.000 token

### Önerilen Yeni Modüller (RICE Skoru ile)
1. [Modül] — RICE: X — [Gerekçe]

### Periyodik Bakım Bulguları
- [Güncellenecek modüller, deprecate edilecek modüller]
```
