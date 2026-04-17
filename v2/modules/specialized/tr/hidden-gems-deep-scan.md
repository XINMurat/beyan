# Module: Hidden Gems & Deep Scan

**Priority**: P1 (Code Maintenance & Tech Debt)
**Tokens**: ~2500
**Analysis Time**: Otonom (Tüm dosya ağacı okunduğunda)

---

## Purpose
Bu modül projedeki "Zombi" (kullanılmayan) kodları, yüksek "Bus Factor" (bilgi silosu) risklerini, gizli teknik borçları ve geliştiricilerin bile unutmuş olabileceği dâhice yazılmış kod parçalarını (Hidden Gems) gün yüzüne çıkarmak için kullanılır.

---

## Zombie Kod Tespiti

Projede kod tabanı büyüdükçe arkada unutulan parçaları bulmak esastır:

1.  **Hiç Çağrılmayan Fonksiyonlar:** Export edilmiş ama import edilmemiş dosyalar.
2.  **Dead Imports:** Başa yazılmış ancak hiç kullanılmamış kütüphaneler.
3.  **Feature Flag Arkası:** Eski feature flag'lerin (toggle) arkasında kalmış ölü kod blokları.

**Kullanılabilecek Araçlar:** `ts-prune` (TypeScript), `deadcode` (Go), `vulture` (Python), coverage raporlarındaki %0 kapsanan alanlar.

---

## Bus Factor Analizi

Bus factor, "Eğer bu projeyi yazan X kişisine yarın bir otobüs çarparsa (veya işten ayrılırsa) proje yaşayabilir mi?" sorusunun ölçümüdür.

```yaml
bus_factor:
  critical: "1 — Projeyi veya kritik bir modülü sadece tek kişi biliyor, ayrılırsa büyük kriz çıkar."
  low: "2-3 — Risk var ama bilgi birkaç kişiye dağılmış, yönetilebilir."
  healthy: "4+ — Bilgi tamamen takıma dağılmış, kod okuryazarlığı homojen."

nasil_olcersin:
  - "git log --author" komutuyla commit yoğunluğu.
  - Bir dosyanın başına "Yazan: X" notu düşülmesi.
  - En kompleks dosyaları kimlerin en son değiştirdiğine bakılması.
```

---

## Teknik Borç (Tech Debt) Tespiti

Teknik borç sadece "kötü kod" değil, gelecekte baş ağrıtacak gizli patlamalardır:

1.  **Yorum Yoğunluğu:** `TODO`, `FIXME`, `HACK` yorumlarının projede ne kadar yer kapladığı.
2.  **Cyclomatic Complexity:** "If-else" piramitleri ve aşırı iç içe geçmiş döngüler (Spaghetti code).
3.  **Duplicate Code:** Kodun birçok yere kopyala-yapıştır (DRY prensibi ihlali) yapılmış olması.

---

## Gizli Bağımlılıklar (Hidden Dependencies)

1.  **Circular Dependencies:** A modülünün B'yi, B'nin de C üzerinden A'yı çağırması.
2.  **Implicit Global State:** Farklı fonksiyonların aynı global değişkene dokunup sessizce birbirinin ayağına basması.
3.  **Undocumented Side Effects:** Adı "getAmount" olan bir fonksiyonun veritabanını güncellemesi (Side effect).

---

## Yüksek Değerli "Gem" Bulgular

AI, sadece hataları bulmamalı, takdir de etmelidir. Kodun içinde çok zarif, zekice veya mükemmel optimize edilmiş bir bölüm varsa bu "Gem" (Cevher) olarak raporlanmalı ve dokümante edilmesi önerilmelidir.

---

## Scoring

```yaml
scoring:
  excellent: "Zombie kod yok, bus factor > 3, teknik borç minimum seviyede, bağımlılıklar izole."
  good: "Ufak tefek TODO'lar var, bazı dosyalar tek kişinin elinde ama genel yapı sağlam."
  attention: "Kopya kod çok fazla, HACK notları etrafı sarmış, dairesel bağımlılık sinyalleri var."
  critical: "Kodun %30'undan fazlası ölü, bus factor 1 (tüm proje tek kişiye bağlı)."
```

---

## Output Format

```markdown
## 🕵️‍♂️ Derin Tarama ve Teknik Borç Raporu

### 🧟 Zombie Kodlar
*   `[Dosya Yolu]`: [Kullanılmayan kod parçası veya import]

### 🚌 Bus Factor Analizi
*   **Mevcut Durum:** [Critical/Low/Healthy]
*   **Riskli Dosyalar:** [Sadece 1 kişinin ellediği çok kritik dosyalar]

### ⚠️ Gizli Teknik Borç ve Bağımlılıklar
*   [TODO/FIXME listesi veya Side Effect uyarıları]

### 💎 Hidden Gems (Zekice Kod Parçaları)
*   `[Fonksiyon veya Dosya]`: [Bu kodun neden çok iyi yazıldığının takdiri]
```
