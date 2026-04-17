# Module: Feature Gap Analysis

**Priority**: P2 (Stratejik Rekabet Analizi)
**Tokens**: ~2000
**Analysis Time**: Manuel tetikleme veya `competitor`, `roadmap`, `feature-request` anahtar kelimelerinde yüklenir

---

## Purpose
Projenin, rakip ürünlere veya piyasa standartlarına kıyasla hangi kritik özellikleri eksik olduğunu sistematik bir şekilde tespit eder. Sadece teknik değil, iş (business) boyutlu eksiklikleri de ölçer.

---

## Rakip Karşılaştırma Matrisi

Yapay zekanın, projenin hedef pazarındaki rakiplerle kıyaslamalı bir özellik tablosu oluşturması beklenir:

```yaml
feature_matrix:
  evaluation_criteria:
    - "Core Feature (Temel işlevsellik)"
    - "UX Kalitesi (Kullanıcı Deneyimi)"
    - "API / Entegrasyon Kabiliyeti"
    - "Fiyatlandırma Modeli"
    - "Performans ve Güvenilirlik"
    - "Destek ve Dokümantasyon"
  scoring: "1 (Yok) — 5 (Üstün)"
```

---

## Özellik Öncelik Değerlendirmesi (RICE Skoru)

Her eksik özelliği aşağıdaki RICE formülüyle puanlandırın:

```
RICE Skoru = (Reach × Impact × Confidence) / Effort

Reach:       Kaç kullanıcıyı etkiler? (1-1000)
Impact:      Ne kadar etkili olacak? (0.25 / 0.5 / 1 / 2 / 3)
Confidence:  Tahminlerimize ne kadar güveniyoruz? (%: 100 / 80 / 50)
Effort:      Geliştirme süresi (Person-Month)
```

---

## Output Format

```markdown
## 📊 Özellik Boşluğu Analizi

### Rakip Karşılaştırma Matrisi
| Özellik | Bu Proje | Rakip A | Rakip B | Öncelik |
|---------|----------|---------|---------|---------|
| [Özellik] | ❌ | ✅ | ✅ | YÜKSEK |

### Kritik Boşluklar (Hemen Kapatılmalı)
- **[Özellik adı]:** [Rakip bunu yapıyor, biz yapamıyoruz — RICE: X]

### Yol Haritası Önerisi
- Q1: [En yüksek RICE skorlu özellik]
- Q2: [İkinci öncelik]
```
