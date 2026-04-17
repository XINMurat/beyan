# 🔍 Beyan — Yapay Zeka Destekli Sistematik Proje Analizi

<p align="center">
  <em>AI-Powered Systematic Project Analysis</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/versiyon-1.0.0-blue" alt="versiyon">
  <img src="https://img.shields.io/badge/prompt-15-green" alt="promptlar">
  <img src="https://img.shields.io/badge/dil-TR%20%7C%20EN-orange" alt="diller">
  <img src="https://img.shields.io/badge/lisans-MIT-lightgrey" alt="lisans">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README_TR.md">Türkçe</a>
</p>

---

# 🚀 Beyan v2.0: Agentic Framework

Beyan, statik bir prompt kütüphanesinden **tam otonom bir agentic framework** yapısına evrildi. Versiyon 2.0; teknolojileri keşfeden, özel promptlar derleyen ve etkileşimli "analizden-düzeltmeye" döngülerini yöneten akıllı bir orkestrasyon katmanı sunar.

### Neden v2.0?
v1.0 "neyin" analiz edileceğini (uzman promptlar) sunarken, v2.0 **"nasıl"** icra edileceğini (execution) sağlar. Tüm keşif ve analiz sürecini otomatikleştirerek insan eforunu %80'e kadar azaltır.

### 🛠️ Temel Yetenekler
- **🔍 Akıllı Keşif (Reconnaissance)**: 20'den fazla teknolojiyi (Python, Go, Node, Flutter vb.) otomatik tespit eden içerik odaklı parmak izi okuma.
- **🧩 Dinamik Derleme**: Keşfedilen teknoloji etiketlerine göre sadece ilgili analiz modüllerini yükleyen, bağlam yoğunluğunu maksimize eden modüler yapı.
- **🧠 Akıllı Token Yönetimi**: Derin analizleri LLM bağlam penceresine sığdırmak için düşük öncelikli modülleri otomatik budayan (pruning) zeka.
- **🤖 Yarı-Otonom Ajan (Mode 3)**: **Analiz → Plan → Kod → Test → Commit** iş akışını insan onaylı kontrol noktalarıyla yöneten etkileşimli döngü.
- **🛡️ Önce Güvenlik**: Tüm yıkıcı işlemler için entegre Git güvenli dallanma (branching) ve onay mekanizmaları.

### 🚦 Hızlı Başlangıç (v2.0)
```bash
cd v2
pip install -r requirements.txt
python cli/analyzer.py --target /path/to/project --mode 1 --lang tr --api openai
```

[**v2.0 Dokümantasyon ve Kodlarını İncele**](v2/)

---

Herhangi bir yazılım projesini derin ve sistematik biçimde analiz etmek için hazırlanmış, yapay zeka destekli prompt kütüphanesi. Legacy kodu devralalım, teknik due diligence yapalım veya bir sistemi kapsamlı belgeleyelim — Beyan eksiksiz bir analitik çerçeve sunar.

> **Temel ilke:** "Bu sistemi yazan geliştirici yarın ayrılsa, yerine gelen başka bir mühendis yalnızca analiz çıktılarına bakarak sistemi birebir yeniden yazabilmeli."

---

## Neden Beyan?

Çoğu prompt kütüphanesi genel amaçlıdır. Beyan farklıdır:

- **Tür farkındalıklı:** Web uygulaması, OS/firmware, AI/ML araştırması, veri boru hatları, DevOps, blockchain ve daha fazlası için ayrı promptlar — yanlış promptu uygulamak yanlış sonuç verir
- **Sistematik:** Her analiz katı bir Tanımlayıcı → Değerlendirici iki katman yapısını izler ve zorunlu tamamlanmamışlık denetimiyle biter
- **Halüsinasyona dirençli:** `TESPİT EDİLEMEDİ` kuralı, placeholder yasağı ve her bulgunun gerçek dosya yolu + satır numarasıyla desteklenmesi zorunluluğu birlikte bir kısıtlama sistemi oluşturur — LLM boşlukları doldurmak yerine işaretler
- **Öz-referanslı:** Beyan, kendi Meta Denetim promptuyla analiz edildi, bulgulardan iyileştirme planı üretildi ve ilk yayın öncesinde sağlık skoru alındı. Araç kendi üzerinde çalıştı.
- **Tam boru hattı:** Triyaj → Analiz → Düzeltme Planı → Sağlık Skoru — her adım bir sonrakini besleyen yapılandırılmış çıktı üretir
- **Tamamlanmamışlık tespiti:** Her prompt yalnızca "ne var"ı değil, "ne eksik"i tespit eder — stub bileşenler, bağlantısız parçalar, yarım kalmış özellikler
- **Kalibre edilmiş skor:** Sağlık Skoru promptu boyut ağırlıklarını proje türüne göre uyarlar — güvenlik OS/firmware için %25 ağırlık taşırken araştırma modeli için %10, çünkü tek bir kart tüm sistemlere uymaz

---

## Tasarım İlkeleri

### 1. Araştırma Sınırı ≠ Teknik Borç

Araştırma ve AI/ML sistemleri için implement edilmemiş bir bileşen her zaman bir bug değildir — kasıtlı olarak ileriye ertelenen açık bir araştırma sorusu olabilir. Beyan ikisini ayrı tablolar ve açık durum etiketleriyle birbirinden ayırır (`Aktif Araştırılıyor` / `Ertelendi` / `Kapsam Dışı`). İkisini karıştırmak yanıltıcı raporlar üretir.

### 2. İki Katmanlı Analiz

Her prompt katı bir ayrımı zorla uygular:

| Katman | Ne Yapar |
|---|---|
| **Tanımlayıcı** | Sistemi olduğu gibi belgeler — yargı yok, öneri yok |
| **Değerlendirici** | Kaliteyi değerlendirir, boşlukları tespit eder, öneriler üretir |

Tanımlayıcı katman tamamlanmadan değerlendirici katman başlamaz. Bu, erken varılan sonuçların olgusal kayıtı kirletmesini önler.

### 3. TESPİT EDİLEMEDİ Sözleşmesi

Bir bilgiye kod tabanında ulaşılamazsa çıktının şunu söylemesi zorunludur:
> ⚠️ **TESPİT EDİLEMEDİ** — `[hangi dosyada/dizinde arandığı]`

Asla tahmin et. Asla uydur. Bu tek kural, Beyan'ın halüsinasyon direncinin büyük bölümünden sorumludur.

### 4. Öz-Referanslı Geliştirme

Beyan v1.0, kendi araçlarıyla analiz edilmeden yayınlanmadı:

```
İlk tasarım
      │
      ▼
Meta Denetim promptu kütüphanenin kendisine uygulandı
      │
      ▼
Bulgular → Düzeltme Planı Üretici
      │
      ▼
D serisi (hızlı düzeltmeler) ve G serisi (orta vadeli) uygulandı
      │
      ▼
Sağlık Skoru: 2.45 (önce) → 4.75 (sonra)  [+%71 iyileşme]
      │
      ▼
v1.0 yayınlandı
```

Meta-analiz döngüsünün tamamı [`tr/meta-analysis/`](tr/meta-analysis/) dizininde belgelenmiştir.

---

## Prompt Ailesi

### Giriş Noktası
| Prompt | Amaç |
|---|---|
| [Triyaj ve Yönlendirme](tr/triyaj/triyaj_yonlendirme_promptu_v1.0.md) | Bilinmeyen projeyi sınıflandır ve hangi promptları uygulayacağını belirle — her zaman buradan başla |

### Proje Türü Bazlı Promptlar
| Prompt | Ne Zaman |
|---|---|
| [Uygulama Analizi](tr/proje-turu/master_proje_analiz_promptu_v2.3.md) | Web, mobil, masaüstü uygulamalar — mikroservis ve mobil uzantıları dahil |
| [OS / Sistem Yazılımı](tr/proje-turu/os_analiz_promptu_generic_v1.0.md) | Çekirdek, firmware, gömülü sistem, hypervisor |
| [Araştırma / AI-ML](tr/proje-turu/research_ai_analiz_promptu_generic_v1.0.md) | Deneysel modeller, akademik sistemler — LaTeX + kod eşlemeli matematik dokümantasyonu |
| [Veri ve Analitik](tr/proje-turu/veri_analitik_analiz_promptu_v1.0.md) | ETL, veri ambarı, boru hatları — sessiz hata tespiti yerleşik |
| [Altyapı / DevOps](tr/proje-turu/altyapi_devops_analiz_promptu_v1.0.md) | IaC, CI/CD, platform mühendisliği — drift farkındalığı + FinOps |
| [Legacy / Göç](tr/proje-turu/legacy_goc_analiz_promptu_v1.0.md) | Eski sistemden yeniye geçiş — iki sistemi eş zamanlı analiz |
| [Blockchain](tr/proje-turu/blockchain_analiz_promptu_v1.0.md) | Akıllı sözleşme, DeFi, Web3 — değiştirilemezlik farkındalıklı, ekonomik güvenlik dahil |

### Odak Bazlı Promptlar (Proje Türünden Bağımsız)
| Prompt | Ne Zaman |
|---|---|
| [Güvenlik Denetimi](tr/odak/guvenlik_denetim_promptu_v1.0.md) | Derinlemesine güvenlik analizi, OWASP Top 10, tehdit modellemesi |
| [Performans Denetimi](tr/odak/performans_denetim_promptu_v1.0.md) | Darboğaz analizi, kritik yol waterfall, ölçeklenebilirlik sınırları |
| [API Tasarım Denetimi](tr/odak/api_tasarim_denetim_promptu_v1.0.md) | Sözleşme kalitesi, kırıcı değişiklik yönetimi, tüketici etkisi |
| [Uyumluluk Denetimi](tr/odak/uyumluluk_denetim_promptu_v1.0.md) | GDPR, KVKK, PCI-DSS, HIPAA — kişisel veri envanteri + risk matrisi |

### Yatay Araçlar
| Prompt | Ne Zaman |
|---|---|
| [Düzeltme Planı Üretici](tr/yatay-araclar/duzeltme_plani_uretici_promptu_v1.0.md) | Analiz bulgularını etki-çaba matrisi + sprint aksiyon kartlarına dönüştür |
| [Proje Sağlık Skoru](tr/yatay-araclar/proje_saglik_skoru_promptu_v1.0.md) | Genel durumu proje türüne kalibre edilmiş 1–5 skalasında puanla |

### Özel
| Prompt | Ne Zaman |
|---|---|
| [Meta Denetim](tr/ozel/ai_analiz_sistemi_denetim_promptu_v1.0.md) | Beyan kütüphanesini veya herhangi bir `.md` tabanlı bilgi sistemini denetle |

---

## Nasıl Çalışır?

```
Bilinmeyen Proje
      │
      ▼
  [Triyaj Promptu]  ──►  triage_report.md  ──►  "Şu promptları şu sırayla uygula"
      │
      ▼
[Proje Türü Promptu(ları)]  +  [Odak Promptu(ları)]
      │
      ▼
 Yapılandırılmış çıktı:
   completeness_report.md   ← ne eksik
   fragility_report.md      ← ne kırılabilir
   risk_matrix.md           ← ne tehlikeli
   ...
      │
      ├──►  [Düzeltme Planı]  ──►  Etki-çaba matrisi + sprint aksiyon kartları
      └──►  [Sağlık Skoru]    ──►  Boyuta göre kalibre edilmiş 1–5 puan kartı
```

---

## Hızlı Başlangıç

1. **Repoyu klonla**
   ```bash
   git clone https://github.com/yourusername/beyan.git
   ```

2. **Triyaj promptunu aç**, AI asistanına proje dosya ağacı / README / temel dosyalarla birlikte yapıştır.

3. **Triyaj çıktısını takip et** — hangi promptları hangi sırayla uygulayacağını söyler.

4. **Önerilen promptları çalıştır**, çıktıları projenin `docs/` dizinine kaydet.

5. **İsteğe bağlı:** Toplanan çıktılar üzerinde Düzeltme Planı + Sağlık Skoru çalıştır.

> Claude, GPT-4, Gemini veya yetenekli herhangi bir LLM ile çalışır.

---

## Çıktı Yapısı

Her prompt standart bir `docs/` dizini üretir. Birden fazla prompt temiz biçimde birleşir:

```
projeniz/
└── docs/
    ├── index.md                    ← Ana navigasyon (tüm promptlar çalıştıktan sonra elle oluştur)
    ├── triage/
    ├── analysis/                   ← Proje türü promptları bu dizini paylaşır
    ├── security-audit/
    ├── performance-audit/
    ├── compliance-audit/
    ├── api-audit/
    ├── migration-analysis/
    ├── blockchain-audit/
    ├── remediation/
    └── health-score/
```

Tam çok-promptlu çıktı rehberi için [Navigasyon Standardı](tr/NAVIGASYON_STANDARDI.md)'na bakın.

---

## Dil Desteği

| Dil | Durum | Dizin |
|---|---|---|
| 🇹🇷 Türkçe | ✅ Tam | [`tr/`](tr/) |
| 🇺🇸 İngilizce | ✅ Tam | [`en/`](en/) |

---

## Katkı

Katkılarınızı bekliyoruz! Detaylar için [CONTRIBUTING.md](CONTRIBUTING.md)'e bakın.

**Katkı yolları:**
- 🐛 Promptta sorun mu buldunuz? Hata raporu açın
- 💡 Eksik proje türü mü var? Yeni prompt isteği oluşturun
- 🌍 Çevirileri geliştirmeye yardım edin
- ⭐ Projeyi desteklemek için yıldız verin

---

## Lisans

[MIT](LICENSE) — serbestçe kullanın, değiştirin, dağıtın.

---

## Notlar

Beyan, yinelemeli öz-referanslı bir süreçle geliştirildi: tasarlandı, ardından kendi Meta Denetim promptuyla analiz edildi, bulgulara göre iyileştirildi ve yayın öncesinde sağlık skoru alındı. Meta-analiz döngüsünün tamamı — tüm bulgular, düzeltme planı ve önce/sonra sağlık skorları dahil — [`tr/meta-analysis/`](tr/meta-analysis/) dizininde belgelenmiştir.
