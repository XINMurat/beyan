# Beyan v2.0 Agentic Framework — Kullanım Rehberi (USAGE GUIDE)

Beyan v2.0, projenizi inceleyen, kod standartlarını otonom olarak değerlendiren ve size doğrudan uygulanabilir (P0, P1, P2 öncelikli) teknik aksiyonlar sunan yapay zeka (LLM) destekli bir analiz motorudur.

Bu doküman, sistemin kurulumunu, modüllerin çalışma mantığını ve üretilen raporların nasıl okunması gerektiğini açıklar.

---

## Bölüm 1: Kurulum ve Gereksinimler

Sistem, yapay zekaya devasa kod dosyalarını sunabilmek için bir Python CLI aracına dayanmaktadır.

### 1.1 Python Gereksinimleri
Sistem **Python 3.8+** üzerinde çalışmaktadır. Aşağıdaki komutlarla bağımlılıkları yükleyin:

```bash
# Proje kök dizininde
pip install -r requirements.txt
```
*(Not: `PyYAML` ve tercih edilen API'ye göre `openai` veya `anthropic` paketleri kurulacaktır.)*

### 1.2 Ortam Değişkenleri (API Keys)
Analiz motorunu hangi Yapay Zeka platformuyla kullanacaksanız, ilgili API anahtarını sisteminize tanımlamalısınız.

```bash
# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-..."
$env:ANTHROPIC_API_KEY="sk-ant-..."

# Linux / Mac
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

---

## Bölüm 2: Hızlı Başlangıç ve Kullanım Modları

Sistemin kalbi olan `analyzer.py` betiği, projenizi okuyup uygun modülleri seçer ve yapay zeka için devasa bir prompt derler.

### Temel Kullanım Komutu:
```bash
python cli/analyzer.py --target /path/to/your/project --mode 1 --lang tr --api anthropic
```

### Parametreler ve Çalışma Modları (Mode 1, 2, 3)

*   `--target`: Analiz edilecek hedef projenizin dizini. İçinde bulunduğunuz dizini analiz etmek için `.` kullanabilirsiniz.
*   `--lang`: Raporun dilini seçer. `tr` (Türkçe) veya `en` (İngilizce).
*   `--api`: Prompt derlendikten sonra kime gönderileceğini seçer. `openai`, `anthropic` veya `none` (sadece derleyip diske kaydeder).
*   `--mode`: Agent'ın otonomi seviyesi.
    *   **Mode 1 (Analiz):** Sadece rapor üretir, sorunları listeler ve size sunar. Koda dokunmaz.
    *   **Mode 2 (Plan):** Analiz edilen sorunların çözümü için detaylı bir `implementation_plan.md` üretir.
    *   **Mode 3 (Fix/Agentic):** (Pilot) Sorunları bulur, onayınızı alır ve bizzat kod dosyalarına müdahale edip düzeltir (Checkpoint onaylı).

---

## Bölüm 3: Modülleri Anlama ve Auto-Load Mekanizması

Beyan v2.0'ın gücü, **53 farklı uzmanlık modülüne** sahip olmasından gelir. Sistemin tüm modülleri aynı anda yüklemesi Token israfına (ve unutkanlığa) yol açar.

### MANIFEST.yaml Nasıl Çalışır?
`MANIFEST.yaml` dosyası tüm modüllerin kataloğudur. CLI aracımız projeyi tararken bu dosyaya bakar.

### Auto-load (Otomatik Yükleme)
Eğer projenizde `package.json` varsa, sistem otonom olarak `react-typescript` ve `ui_ux_analysis` modüllerini yükler. Eğer `.csproj` bulursa `.NET Core` modülünü yükler. Bu sayede yapay zeka tam olarak sizin projenizin teknolojisine uygun bir karaktere bürünür.

### Manuel Modül Yükleme
Özel bir analize ihtiyacınız varsa `analyzer.py` içerisindeki `--modules` parametresi eklenebilir veya `MANIFEST.yaml` içerisindeki `auto_load_if` kuralını projenizle eşleşecek şekilde genişletebilirsiniz.

---

## Bölüm 4: İleri Kullanım (Özel Modül Yazma)

Kendi şirketinize, sektörünüze veya kod standartlarınıza özel kuralları yapay zekaya öğretmek çok kolaydır.

1.  `modules/specialized/tr/benim-sirketim.md` adında yeni bir dosya oluşturun.
2.  İçerisine kendi standartlarınızı ve "Scoring" kurallarını yazın.
3.  `MANIFEST.yaml` dosyasına modülünüzü ekleyin:

```yaml
  benim_sirketim:
    path: "modules/specialized/{lang}/benim-sirketim.md"
    priority: P1
    auto_load_if: ["package.json"]
    tags: ["company", "internal"]
```
Bir sonraki analizde yapay zeka artık sizin şirketinize özel bir müfettiş gibi çalışacaktır. Token optimizasyonu için modüllerinizin 2000-3000 token civarında kalmasına özen gösterin.

---

## Bölüm 5: Çıktıları Yorumlama ve Öncelikler

Analiz tamamlandığında (Mode 1), size `beyan_analysis_result.md` adında bir rapor sunulur.

### Skor Aralıkları Nelerdir?
*   **🟢 9.0 - 10.0 (Mükemmel):** Proje Production-Ready. Minimum risk.
*   **🟡 7.0 - 8.9 (İyi):** Genel mimari sağlam ancak iyileştirmeler (P1) var.
*   **🟠 5.0 - 6.9 (Orta):** Kritik güvenlik veya mimari pürüzler var (P0/P1). Ciddi efor gerektirir.
*   **🔴 0.0 - 4.9 (Kritik):** Proje teknik borç batağında veya production'a çıkması tehlikeli.

### Aksiyon Öncelikleri (P0, P1, P2, P3)
Yapay zeka size vereceği görevleri Jira/Trello mantığında sınıflandırır:
*   **P0:** Acil! Güvenlik açığı, veri sızıntısı veya sistemi çökerten hata. Hemen düzeltin.
*   **P1:** Bu Sprint içinde ele alınması gereken önemli performans ve kalite sorunları.
*   **P2:** Gelecek sprintlerde düzeltilebilecek kod okunabilirliği ve test eksiklikleri.
*   **P3:** Backlog (Gelecekteki eklentiler, küçük iyileştirmeler).

---

## Bölüm 6: Sorun Giderme (Troubleshooting)

**Soru: Token limiti hatası (Context Window Exceeded) alıyorum?**
**Çözüm:** Çok fazla modül yüklenmiş olabilir veya analiz ettiğiniz projedeki dosyalar (özellikle log veya json data dosyaları) çok büyüktür. `analyzer.py` içerisindeki dosya filtreleme mantığını `.gitignore`'a benzer şekilde güncelleyin.

**Soru: Modül Bulunamadı Hatası alıyorum?**
**Çözüm:** `MANIFEST.yaml` içerisindeki yol (path) tanımları bozulmuş olabilir veya İngilizce (`--lang en`) seçmiş olmanıza rağmen henüz İngilizce modüller projeye eklenmemiş olabilir. (Faz 4 İngilizce çevirileri eklendiğinde bu düzelecektir.)

**Soru: Yapay zeka Türkçe kodlamama rağmen İngilizce rapor verdi?**
**Çözüm:** LLM'in genel yapısından kaynaklı olabilir. Komutu mutlaka `--lang tr` ile tetiklediğinize emin olun. Gerekirse `BASE_PROMPT.md` içerisindeki dil zorunluluğu kuralını güçlendirin.

---

## Bölüm 7: Navigasyon Standardı

Bu bölüm, sistemin modül ailesinin nasıl kullanılacağını ve hangi analizin ne zaman başlatılacağını özetler.

### 7.1 Modül Kategorileri ve Kullanım Haritası

| Kategori | Klasör | Ne Zaman Kullanılır |
|---|---|---|
| **Core** | `modules/core/` | Her projede otomatik yüklenir. Güvenlik, performans, mimari temel kontroller. |
| **Domains** | `modules/domains/` | Proje türüne göre yüklenir. OS, AI, DevOps, Blockchain vb. |
| **Focus** | `modules/focus/` | Derinlemesine tek konuya odaklanmak için. API denetimi, güvenlik denetimi vb. |
| **Specialized** | `modules/specialized/` | Teknoloji bazlı. React, .NET, Türkiye pazarı vb. |
| **Testing** | `modules/testing/` | Test stratejisi, E2E, gerçek zamanlı test |
| **Guides** | `modules/guides/` | Düzeltme rehberleri. Analiz sonrası uygulanır. |

### 7.2 Standart Analiz Akışı

```
Adım 1  →  analyzer.py çalıştır (--mode 1)
              ↓ project-intelligence.md projeyi tanır
              ↓ Uygun modüller auto-load edilir
              ↓ beyan_compiled_prompt.md derlenir

Adım 2  →  Derlenen promptu LLM'e ver
              ↓ P0/P1/P2/P3 bulgular raporlanır
              ↓ Sağlık skoru hesaplanır

Adım 3  →  Bulgulara göre guides/ modüllerini yükle
              Örn: P0 SQL Injection → security-fixes.md
              Örn: P1 N+1 query  → performance-optimization.md

Adım 4  →  (İsteğe bağlı) --mode 2 ile implementation plan üret
```

### 7.3 Çıktı Dizin Sözleşmesi

Tüm analiz çıktıları projenizde şu yapıda oluşturulur:

```
docs/
├── triage/
│   └── triage_report.md          ← İlk tanılama (monorepo için her proje ayrı)
├── analysis/
│   └── analysis-report-YYYYMMDD.md
├── action-plan-YYYYMMDD.md
└── index.md                      ← Monorepo projelerinde üst navigasyon
```

### 7.4 Triyaj Kalite Kontrol Listesi

Bir analizi başlatmadan önce şu kontrolleri yapın:

- [ ] Birincil proje türü en az iki bağımsız sinyale dayanıyor mu?
- [ ] Olgunluk seviyesi somut gözlemlerle desteklendi mi?
- [ ] Monorepo ise her alt proje ayrı ayrı ele alındı mı?
- [ ] Her önerilen modül için gerekçe yazıldı mı?
- [ ] Belirsizlikler `⚠️ BELİRSİZ` olarak işaretlendi mi?
- [ ] Token bütçesi kontrol edildi mi? (`analyzer.py` çıktısındaki "Tahmini Token Maliyeti" 48.000'i geçmemeli)
