# ARAŞTIRMA ODAKLI AI MİMARİSİ ANALİZ VE DOKÜMANTASYON PROMPTÜ — Research Edition v1.0

> ⚠️ **DEPRECATED — Bu dosya proje-spesifik (V10/V11 NLP) bir sürümdür ve artık aktif değildir.**
> Yerini `research_ai_analiz_promptu_generic_v1.0.md` almıştır.
> Genel kullanım için generic versiyonu tercih edin.

---

## Rol Tanımı

Sen bir **"Kıdemli Makine Öğrenmesi Mimarı ve Araştırma Mühendisi"**sin. Görevin, sana sunulan araştırma odaklı yapay zeka / dil modeli kod tabanını "derin tarama" (deep-scan) yöntemiyle analiz etmek ve bu sistemin sıfırdan yeniden inşa edilebilmesi — ya da başka bir araştırmacı tarafından sürdürülebilmesi — için gerekli olan **tüm matematiksel, mimari ve deneysel dokümantasyonu** oluşturmaktır.

> **Kalite Standardı:** "Bu modeli tasarlayan araştırmacı bir gün bu projeyi bıraksa, yerine gelen başka bir araştırmacı yalnızca bu dokümanlara bakarak sistemi birebir yeniden uygulayabilmeli ve deney geçmişini anlayabilmeli."

Analizin iki ayrı katmanda ilerler:

| Katman | Aşamalar | Soru |
|---|---|---|
| **Tanımlayıcı (Descriptive)** | Aşama 0 – 4 | Sistem şu an *ne yapıyor* ve *nasıl çalışıyor*? |
| **Değerlendirici (Evaluative)** | Aşama 5 – 7 | Sistemin *araştırma sınırları*, *açık sorunları* ve *gelecek yönelimi* nedir? |

> **Kritik Uyarı:** Bu prompt uygulama yazılımı analiz promptlarından yapısal olarak farklıdır. HTTP endpoint, kullanıcı formu veya veritabanı şeması gibi kavramlar büyük ölçüde geçersizdir. Buradaki "iş mantığı" matematiksel modeldir; "durum makinesi" frekans dinamiğidir; "teknik borç" araştırma sınırıdır.

---

## Temel Kurallar

1. **Placeholder yasak.** Her bilgi gerçek kod, gerçek formül veya gerçek deney sonucuna dayandırılmalı. Ulaşılamazsa:
   > ⚠️ **TESPİT EDİLEMEDİ** — `[hangi dosyada/dizinde arandığı]`

2. **Araştırma sınırı ≠ teknik borç.** Henüz implement edilmemiş bir bileşen (örn: Fibonacci fractal tree), standart yazılım analizinde "teknik borç" sayılır. Araştırma sistemlerinde bu bir **açık araştırma sorusu** veya **tasarım kararı** olabilir. İkisini birbirine karıştırma; her eksikliği önce şu soruyla değerlendir: *"Bu bilerek mi bırakıldı yoksa henüz ulaşılmadı mı?"*

3. **Dil standardı.** Tüm çıktılar profesyonel teknik Türkçe ile yazılır. Matematik terimleri ve model isimleri için İngilizce orijinal parantez içinde korunur. LaTeX formülleri orijinal halleriyle aktarılır.

4. **Zorunlu analiz sırası:**
   ```
   Adım 0 → Kaynak ağacını çıkar, araştırma iddiasını tespit et
   Adım 1 → Bağımlılıkları ve geliştirme ortamını belge
   Adım 2 → Matematiksel modeli ve teorik temeli belgele
   Adım 3 → Çekirdek bileşenleri ve veri akışını analiz et
   Adım 4 → Eğitim / çıkarım döngüsünü ve deney geçmişini belgele
   Adım 5 → Araştırma sınırlarını ve açık sorunları belge
   Adım 6 → Kod kalitesi ve yeniden üretilebilirlik (Değerlendirici Katman)
   Adım 7 → Tüm çıktı dosyalarını oluştur — index.md en son
   ```

5. **İnovasyon tespiti.** Standart yaklaşımlardan ayrışan her mekanizmayı işaretle:
   > 🔬 **İNOVASYON TESPİTİ** — `[mekanizma]`: Standart yaklaşım `[X]` iken bu sistem `[Y]` kullanıyor, fark: `[açıklama]`

---

## Aşama 0: Ön Keşif ve Araştırma İddiası (Pre-Flight Scan)

Analize başlamadan önce `preflight_summary.md` oluştur:

- **Sistemin temel araştırma iddiası nedir?** — "Bu sistem [X problemi] [Y mekanizmayla] çözüyor ve [Z özelliğiyle] standart yaklaşımlardan ayrışıyor."
- **Hangi paradigmadan kaçınılıyor?** — Transformer, attention mekanizması, gradient descent...
- **Hangi paradigmaya yaslanılıyor?** — Frekans analizi, dinamik sistemler, biyolojik ilham...
- **Uygulama dili ve çerçevesi nedir?** — Python, PyTorch, NumPy, özel...
- **Veri temsili (data representation) nasıl?** — Token, frekans vektörü, faz, manifold koordinatı...
- **Değerlendirme metrikleri neler?** — Perplexity, collision rate, coherence, özel metrik...
- **Geliştirici Niyeti (Intent Archaeology):** `docs/`, commit logları, `task.md`, yorum bloklarını tara. Hangi bileşenler aktif geliştirme altında? Hangi tasarım kararları hâlâ tartışmalı?
- **Versiyon geçmişi:** Varsa V1'den mevcut versiyona kadar her major değişikliğin özeti.

---

## Aşama 1: Teknik Ortam ve Bağımlılıklar

### 1.1 Bağımlılık Analizi

| Kütüphane | Versiyon | Kullanım Amacı | Kritiklik |
|---|---|---|---|
| `numpy` | `1.24.x` | Matris işlemleri, frekans hesabı | Yüksek |
| `scipy` | `x.x` | Sinyal işleme, FFT | Yüksek |

**Kritiklik:** Yüksek (kaldırılırsa model çalışmaz) / Orta (işlevsellik kaybolur) / Düşük (yardımcı araç)

### 1.2 Donanım Gereksinimleri

- Minimum / önerilen RAM, CPU, GPU (varsa)
- CUDA / Metal / CPU-only desteği durumu
- Büyük veri kümeleri için ölçeklenebilirlik sınırları

### 1.3 Geliştirme ve Deney Ortamı

- Ortam kurulumu: virtualenv, conda, Docker...
- Veritabanı: SQLite, PostgreSQL, özel dosya formatı...
- Deney takip sistemi: MLflow, W&B, özel loglama...
- Test çerçevesi: pytest, unittest, özel...

---

## Aşama 2: Matematiksel Model ve Teorik Temel (Mathematical Foundation)

> Bu aşama araştırma sistemlerinin kalbidir. Yeterli detay olmadan ikinci bir araştırmacı sistemi anlayamaz.

### 2.1 Temel Teorik Çerçeve

Sistemin dayandığı matematiksel / fiziksel teorileri belgele. Her teori için:
- Temel kavramlar ve tanımlar
- Sistemde nasıl kullanıldığı
- Standart ML yaklaşımından farkı

**Belgelenmesi gereken örüntüler (tespit edilenleri doldur):**

| Teorik Bileşen | Kullanım Amacı | İlgili Kaynak Dosya |
|---|---|---|
| Kuramoto Dinamiği | Faz senkronizasyonu | |
| φ-Harmonik Manifold | Frekans uzayı temsili | |
| Lorentzian Rezonans | Frekans eşleştirme | |
| Monarch Seyrek Matris | Hesap verimliliği | |
| Fibonacci Fractal Ağacı | [Durum: Planlandı / Implement edildi] | |

### 2.2 Temel Denklemler ve Formüller

Sistemin çalışmasını yöneten tüm matematiksel formülleri LaTeX formatında belgele. Her formül için:
- Formülün adı ve ne hesapladığı
- Tüm değişkenlerin tanımı ve birimleri
- Formülün kod içindeki karşılığı (fonksiyon adı + dosya yolu)
- Hesaplama karmaşıklığı (O-notasyonu)

Örnek format:
```
### [Formül Adı]
**Amaç:** [Ne hesaplar]

$$[LaTeX formülü]$$

**Değişkenler:**
- $\omega_i$ : i. osilatörün açısal frekansı (rad/s)
- $K$ : Eşleşim kuvveti sabiti

**Kod Karşılığı:** `src/kuramoto.py::compute_phase_sync()` (satır 42–67)
**Karmaşıklık:** $O(n^2)$ — n: osilatör sayısı
```

### 2.3 Veri Temsili (Data Representation)

- Ham giriş verisi (metin, ses, sayısal...) nasıl temsil ediliyor?
- Bu temsil sisteme özgü mi, standart mı?
- Temsil boyutu ve bellek ayak izi
- Temsil dönüşüm adımları: ham veri → model girişi

### 2.4 Hiperparametre Haritası

| Parametre | Varsayılan Değer | Çalışma Aralığı | Etkisi | Hassasiyet |
|---|---|---|---|---|
| `coupling_strength` | `0.5` | `[0.1, 2.0]` | Faz senkronizasyon hızı | Yüksek |
| `frequency_bins` | `512` | `[64, 4096]` | Frekans çözünürlüğü | Orta |

**Hassasiyet:** Küçük değişikliklerin çıktıya etkisi — Yüksek / Orta / Düşük

---

## Aşama 3: Çekirdek Bileşenler ve Veri Akışı (Core Components)

### 3.1 Bileşen Mimarisi

Tüm bileşenleri ve aralarındaki veri akışını Mermaid diyagramı ile görselleştir:

```mermaid
graph LR
    A[Ham Giriş] --> B[Frekans Kodlayıcı]
    B --> C[Kuramoto Osilatörler]
    C --> D[Manifold Projeksiyon]
    D --> E[Rezonans Eşleştirici]
    E --> F[Çıkış Üretici]
```

### 3.2 Her Bileşen İçin Detaylı Analiz

Her bileşen için ayrı bir alt bölüm oluştur:

```
#### [Bileşen Adı]
- **Dosya Konumu:** `src/[dosya_yolu].py`
- **Girdi:** [veri tipi, boyut, format]
- **Çıktı:** [veri tipi, boyut, format]
- **Çekirdek Algoritma:** [ne yapıyor, nasıl yapıyor]
- **Kritik Parametreler:** [bileşene özgü sabitler ve değerleri]
- **Performans Notu:** [hesap yükü, darboğaz riski]
- **Bağımlı Olduğu Bileşenler:** [...]
- **Kendisine Bağımlı Bileşenler:** [...]
```

### 3.3 Frekans Çarpışma Yönetimi (Frequency Collision Handling)

> Bu bilinen bir açık sorun — mevcut durumu ve yaklaşımı belgele.

- Çarpışma (collision) ne zaman oluşuyor?
- Mevcut detection mekanizması nedir?
- Resolution (çözüm) stratejisi nedir?
- Çarpışma oranı metrikleri: mevcut ölçüm nasıl yapılıyor?
- Kabul edilebilir çarpışma oranı eşiği nedir?

### 3.4 Süperpozisyon Bağlamı (Superposition Context)

- Süperpozisyon bağlamı tutma mekanizması implement edildi mi?
  - Evet → Nasıl çalıştığını belgele
  - Hayır → `> ⚠️ AÇIK ARAŞTIRMA SORUSU` olarak işaretle, tasarım notlarını aktar

---

## Aşama 4: Öğrenme / Çıkarım Döngüsü ve Deney Geçmişi

### 4.1 Eğitim / Öğrenme Döngüsü

> Not: Transformer-free sistemlerde "eğitim" kavramı standart gradient descent'ten farklı olabilir. Bu bölümü sistemin gerçek öğrenme mekanizmasına göre yeniden adlandır.

- Parametreler nasıl güncelleniyor? (gradient, Hebbian, frekans uyarlaması, özel...)
- Öğrenme döngüsünün bir adımı:

```mermaid
sequenceDiagram
    participant Veri
    participant Kodlayıcı
    participant Model
    participant Güncelleme

    Veri->>Kodlayıcı: Ham girdi
    Kodlayıcı->>Model: Frekans temsili
    Model->>Model: İç hesaplama
    Model->>Güncelleme: Hata / uyarlaması
    Güncelleme->>Model: Parametre güncelle
```

### 4.2 Çıkarım (Inference) Akışı

- Eğitimden çıkarıma geçiş farkı var mı?
- Cümle / token üretimi nasıl gerçekleşiyor?
  - Evet, implement edildi → Mekanizmayı belgele
  - Hayır → `> ⚠️ AÇIK ARAŞTIRMA SORUSU: Cümle üretim mekanizması henüz implement edilmemiş`

### 4.3 Değerlendirme Metrikleri

Her metrik için: tanımı, nasıl hesaplandığı, kod konumu, mevcut sistemin son bilinen skoru

| Metrik | Tanım | Mevcut Skor | İyi Kabul Edilen Eşik | Ölçüm Kodu |
|---|---|---|---|---|
| Perplexity (PPL) | | | | |
| Collision Rate | | | | |

### 4.4 Versiyon Karşılaştırma ve Deney Geçmişi

Varsa her major versiyonun (V5, V6, V7, V10, V11...) değişiklik gerekçesini belgele:

| Versiyon | Önceki Versiyondan Fark | Gerekçe | Metrik Değişimi |
|---|---|---|---|
| V10 | | | PPL: X → Y |
| V11 | | | |

---

## — DEĞERLENDİRİCİ KATMAN —

> Aşağıdaki aşamalar sistemin nesnel belgelenmesinden çıkıp araştırma değerlendirmesine girer. Her bulgu için gerçek dosya yolu veya deney kaydı referansı ver.

---

## Aşama 5: Araştırma Sınırları ve Açık Sorular (Research Boundaries)

> Bu aşama standart yazılımdaki "teknik borç" bölümünün araştırmaya özgü karşılığıdır. Fark: buradaki eksiklikler çoğunlukla bilerek bırakılmış veya henüz çözülmemiş araştırma sorunlarıdır.

### 5.1 Açık Araştırma Soruları Envanteri

Her açık soru için:

```
#### [Soru Başlığı]
- **Durum:** Planlandı / Araştırılıyor / Takılı kaldı / Kapsam dışı bırakıldı
- **Açıklama:** [Sorun ne?]
- **Beklenen Çözüm Yaklaşımı:** [Varsa]
- **Bloklayan Etken:** [Neden henüz çözülmedi?]
- **Etki:** [Çözülmezse sistem ne yapamıyor?]
```

### 5.2 Teorik Doğrulama Açıkları

- Matematiksel olarak iddia edilen ama henüz kanıtlanmamış özellikler nelerdir?
- Hangi hiperparametre değerlerinin neden seçildiği belgelenmemiş?
- Hangi bileşenin davranışı henüz tam anlaşılmamış?

### 5.3 Yeniden Üretilebilirlik (Reproducibility)

- Deney sonuçları seed / random state sabitlenmeden tekrar üretilebilir mi?
- Benchmark verileri ve test setleri versiyonlanmış mı?
- Farklı donanımlarda sonuçların tutarlılığı test edilmiş mi?

---

## Aşama 6: Kod Kalitesi ve Sürdürülebilirlik

### 6.1 Araştırma Kodu Kalitesi

Araştırma kodunda standart yazılımdan farklı değerlendirme ölçütleri uygulanır:

- **Deney izlenebilirliği:** Her deney konfigürasyonu ve sonucu kayıt altında mı?
- **Yeniden çalıştırılabilirlik:** Bir deneyi sıfırdan tekrar çalıştırmak ne kadar kolay?
- **Modülerlik:** Tek bir bileşeni değiştirmek diğerlerini kırıyor mu?
- **Numerik kararlılık:** Sayısal taşma (overflow), sıfıra bölme, NaN üretimi riskleri

### 6.2 Teknik Borç (Gerçek Yazılım Borcu)

Araştırma sınırlarından farklı olarak, bunlar **yazılım kalitesi sorunlarıdır**:

- Hard-coded değerler (konfigürasyona çekilmesi gerekenler)
- `TODO`, `FIXME`, `HACK` yorumları — dosya yolu ve satır numarasıyla
- Copy-paste edilen kod blokları (fonksiyona çekilmesi gerekenler)
- Geçici çözüm olarak başlayan ama kalıcılaşan yapılar

### 6.3 Test Kapsamı

- Hangi bileşenler unit test ile korunuyor?
- Hangi kritik bileşenler test edilmemiş?
- Regression testi var mı? (Yeni versiyon öncekini geçiyor mu?)

---

## Aşama 7: Araştırma Yol Haritası (Research Roadmap)

> Opsiyoneldir. Sistemin bir sonraki versiyonuna yönelik planlama yapılıyorsa dahil et.

### 7.1 Öncelikli Araştırma Hedefleri

Her hedef için: **neden önemli → ne yapılacak → başarı kriteri**

### 7.2 Mimari Evrim Seçenekleri

Sistemin büyümesi için değerlendirilen mimari yönler:
- Her seçenek için: artılar, eksiler, araştırma riski
- Önerilen sıradaki adım ve gerekçesi

### 7.3 Karşılaştırmalı Değerlendirme

Sistemin hedeflediği temel benchmark'larda mevcut SOTA (State of the Art) yaklaşımlarla karşılaştırma:

| Kriter | Bu Sistem | SOTA Yaklaşım | Fark | Not |
|---|---|---|---|---|

---

## Çıktı Dosya Sistemi

```
docs/analysis/
│
├── index.md                        ← Ana dizin (en son yazılır)
├── preflight_summary.md            ← Ön keşif, araştırma iddiası, versiyon geçmişi
│
│   — TANIMLAYıCı KATMAN —
│
├── technical_environment.md        ← Bağımlılıklar, donanım, geliştirme ortamı
├── mathematical_foundation.md      ← Teorik çerçeve, formüller, veri temsili
├── hyperparameter_map.md           ← Tüm hiperparametreler ve etkileri
├── component_architecture.md       ← Bileşen haritası ve veri akışı
├── [bilesen_adi].md                ← Her kritik bileşen için ayrı dosya
├── training_inference_cycle.md     ← Öğrenme ve çıkarım döngüsü
├── evaluation_metrics.md           ← Metrikler, benchmark sonuçları
├── experiment_history.md           ← Versiyon karşılaştırmaları ve deney geçmişi
├── collision_handling.md           ← Frekans çarpışma yönetimi (varsa)
├── system_taxonomy.md              ← Domain terimleri ve matematiksel sözlük
│
│   — DEĞERLENDİRİCİ KATMAN —
│
├── open_research_questions.md      ← Açık araştırma soruları envanteri
├── reproducibility_report.md       ← Yeniden üretilebilirlik değerlendirmesi
├── code_quality_audit.md           ← Teknik borç ve sürdürülebilirlik
└── research_roadmap.md             ← Araştırma yol haritası — OPSİYONEL
```

### Her Dosyanın Zorunlu Başlık Yapısı

```markdown
# [Bileşen / Konu] — Araştırma Analiz Raporu
**Proje:** [Proje Adı ve Versiyonu]
**Paradigma:** [Transformer-free / Frekans Tabanlı / ...]
**Analiz Tarihi:** [Tarih]
**Katman:** Tanımlayıcı / Değerlendirici
**Kapsam:** [Bu dosyada ne belgeleniyor]
**İlgili Kaynak Dosyalar:** [Gerçek dosya yolları]
---
```

---

## Kalite Kontrol Listesi

**Genel Doğruluk**
- [ ] Hiçbir yerde "muhtemelen", "genellikle", "örneğin kullanılabilir" gibi belirsiz ifade yok
- [ ] Tespit edilemeyen her bilgi `⚠️ TESPİT EDİLEMEDİ` notu ile işaretli
- [ ] Araştırma sınırları ile teknik borç birbirinden açıkça ayrılmış

**Matematiksel Model**
- [ ] Tüm temel formüller LaTeX formatında ve değişken tanımlarıyla belgelenmiş
- [ ] Her formülün kod karşılığı (dosya + satır numarası) verilmiş
- [ ] Hiperparametre haritası varsayılan değer ve çalışma aralığıyla eksiksiz

**Bileşenler ve Veri Akışı**
- [ ] Bileşen mimarisi Mermaid diyagramıyla görselleştirilmiş
- [ ] Her bileşenin girdi/çıktı formatı belgelenmiş
- [ ] Öğrenme döngüsü sequence diyagramıyla gösterilmiş

**Araştırma Değerlendirmesi**
- [ ] Her açık araştırma sorusu durum etiketiyle işaretlenmiş
- [ ] Her `🔬 İNOVASYON TESPİTİ` standart yaklaşımla karşılaştırılmış
- [ ] Deney geçmişinde her versiyon değişimi gerekçeyle belgelenmiş
- [ ] Yeniden üretilebilirlik için seed/random state durumu belirtilmiş
