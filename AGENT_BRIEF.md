# Beyan v2.0 — Agent Görev Brifing Belgesi

> **Hazırlayan:** Proje analiz oturumu (17 Nisan 2026)  
> **Hedef Kitle:** Görevi yürütecek AI asistanı  
> **Amaç:** Projedeki tüm eksiklikleri, öncelik sırasıyla, her fazda bağımsız çalışılabilir biçimde tanımlamak

---

## 1. Proje Nedir?

**Beyan v2.0** — LLM tabanlı modüler yazılım proje analiz sistemidir.

Kullanıcı kendi yazılım projesini AI asistanına yükler, bu sistem devreye girerek:
- Proje tipini otomatik tanır (Web, API, Mobile, Blockchain, vb.)
- Sadece ilgili modülleri yükler (token verimliliği)
- Türkçe analiz raporu üretir
- P0–P3 önceliklendirmesiyle aksiyonlar sunar

**Temel bileşenler:**

| Dosya | Rol |
|---|---|
| `BASE_PROMPT.md` | Core kimlik, analiz felsefesi, çıktı formatı |
| `ORCHESTRATOR_PROMPT.md` | Mode 1/2/3 iş akışı kontrolcüsü |
| `MANIFEST.yaml` | 51 modülün kataloğu, auto-load kuralları |
| `analyzer.py` | CLI aracı — dizin tarar, prompt derler |
| `merge_modules.py` | v1→v2 migrasyon aracı |
| `verify_integrity.ps1` | Encoding ve link doğrulama aracı |
| `modules/` | Tüm analiz modülleri (core, domain, testing, specialized, guides) |

**Dizin yapısı** (mevcut hali — EN/TR ayrımı var ama EN modülleri eksik):

```
beyan-v2.0/
├── core_prompts/
│   ├── tr/
│   │   ├── BASE_PROMPT.md          ✅ Tamamlandı
│   │   └── ORCHESTRATOR_PROMPT.md  ✅ Tamamlandı
│   └── en/
│       ├── BASE_PROMPT.md          ❌ Eksik (Faz 4)
│       └── ORCHESTRATOR_PROMPT.md  ❌ Eksik (Faz 4)
├── modules/
│   ├── core/
│   │   ├── tr/                     ✅ Çoğu tamamlandı (bazı stub)
│   │   └── en/                     ❌ Çeviriler eksik (Faz 4)
│   ├── domain/
│   │   ├── tr/                     ✅ Çoğu tamamlandı
│   │   └── en/                     ❌ Çeviriler eksik (Faz 4)
│   ├── specialized/
│   │   ├── tr/                     ⚠️ Bazıları stub
│   │   └── en/                     ❌ Eksik
│   ├── testing/
│   │   ├── tr/                     ⚠️ Bazıları stub
│   │   └── en/                     ❌ Eksik
│   └── guides/
│       ├── tr/                     ⚠️ Tümü stub
│       └── en/                     ❌ Eksik
├── MANIFEST.yaml                   ✅ Tamamlandı
├── QUICK_START.md                  ✅ Tamamlandı (ama eksik dosyalara ref veriyor)
├── GLOSSARY.md                     🔴 Encoding bozuk
├── USAGE_GUIDE.md                  ❌ Eksik (referans veriliyor ama yok)
├── FAQ.md                          ❌ Eksik (referans veriliyor ama yok)
├── MODE_TRANSITIONS.md             ❌ Eksik (referans veriliyor ama yok)
├── TURKISH_PROMPTS.md              ❌ Eksik (referans veriliyor ama yok)
├── ALGO-COMPLETE.md                ❌ Eksik (MANIFEST'te tanımlı ama yok)
├── analyzer.py                     ⚠️ Anthropic API desteği eksik
└── merge_modules.py                ⚠️ Hard-coded Windows path
```

---

## 2. Tamamlanan (✅) ve Kaliteli Modüller — Referans Olarak Kullan

Yeni modüller yazarken şu dosyaları stil ve kalite referansı olarak kullan:

| Dosya | Neden referans? |
|---|---|
| `performance-analysis.md` | ~730 satır, yaml bloklar, komut örnekleri, scoring tablosu |
| `security-analysis.md` | ~1000 satır, OWASP coverage, confidence level notasyonu |
| `ui-ux-analysis.md` | ~770 satır, otomatik test araçları, WCAG detayları |
| `api-design-analysis.md` | Hem REST hem GraphQL, endpoint pattern analizi |
| `database-analysis.md` | Query analizi, N+1 tespiti, index stratejisi |

**Standart modül formatı:**

```markdown
# Module: [Başlık]

**Priority**: P[0-3] ([Neden bu öncelik])
**Tokens**: ~[tahmini token sayısı]
**Analysis Time**: [süre]

---

## Purpose
[1 paragraf: Ne analiz eder, neden önemli]

---

## [Ana Boyut 1]

[yaml bloklar, scoring kriterleri, araç önerileri]

### [Alt Boyut]

[Kod örnekleri, komutlar, before/after örnekleri]

---

## Scoring

[yaml: excellent/good/attention/critical kriterleri]

---

## Output Format

[Modülün üretmesi gereken çıktı şablonu]
```

---

## 3. Tespit Edilen Tüm Sorunlar — Öncelik Sırasıyla

### 3.1 Encoding/Bozukluk Sorunları (🔴 Kritik)

**Etkilenen dosyalar:**

1. **`GLOSSARY.md`** — `✅` karakteri harflerin yerini almış, `⚡` da. Örnek: `"Bu⚡ Fact✅r"` → `"Bus Factor"` olmalı.
2. **`scoring-criteria.md`** — Aynı sorun: `"M✅dule: Sc✅ring Criteria and F✅rmula⚡"` → `"Module: Scoring Criteria and Formulas"`. Ayrıca içerik yarım kalmış, tüm modül yazılmalı.

**Düzeltme kuralı:** `✅` → `o`, `⚡` → `s` eşlemesini uygula. Bağlam okuyarak doğru harfi tespit et.

---

### 3.2 Kod Sorunları (🟡 Önemli)

**Dosya: `analyzer.py`**

Sorun 1 — Anthropic API desteği eksik:
```python
# Mevcut (satır 203):
parser.add_argument("--api", type=str, choices=["none", "openai", "anthropic"], default="none")

# compile_prompt() fonksiyonunda sadece şu var:
if api_choice == "openai":
    # OpenAI çağrısı yapıyor
# "anthropic" seçeneği için HİÇBİR ŞEYI yapmıyor
```

Eklenmesi gereken:
```python
elif api_choice == "anthropic":
    # anthropic kütüphanesi import et
    # ANTHROPIC_API_KEY ortam değişkeninden al
    # claude-sonnet-4-6 veya claude-opus-4-6 kullan
    # messages API ile gönder
    # Sonucu beyan_analysis_result.md olarak kaydet
```

Sorun 2 — Token hesaplama kaba heuristic:
```python
# Mevcut:
def calculate_tokens(text: str) -> int:
    return len(text) // 4  # 1 token = ~4 karakter

# İyileştirme: tiktoken kullan veya dil bazlı heuristic ekle
```

---

**Dosya: `merge_modules.py`**

```python
# Mevcut (satır 6-7) — Windows'a bağlı, taşınabilir değil:
v3 = Path(r'C:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1')
v2 = Path(r'C:\TRAE\beyan-v1.0.0\beyan-v2.0-agentic')

# Olması gereken:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--v3", required=True, help="v3 kaynak dizini")
parser.add_argument("--v2", required=True, help="v2 hedef dizini")
args = parser.parse_args()
v3 = Path(args.v3)
v2 = Path(args.v2)
```

---

### 3.3 Stub Modüller (⚠️ İçerik Eksik)

Aşağıdaki 19 modül dosyası mevcut dizinde var ama içeriksiz (190–300 byte, sadece "pending translation" notu):

#### Faz 2 — Kritik Stub'lar (Hemen Yazılmalı)

| Dosya | MANIFEST'teki path | Priority | Açıklama |
|---|---|---|---|
| `scoring-criteria.md` | `modules/core/{lang}/scoring-criteria.md` | P0 | Tüm sistem skorlama formülü — encoding sorunu da var |
| `project-intelligence.md` | `modules/specialized/{lang}/project-intelligence.md` | P0 | Meta-orchestrator, proje tipi algılama |
| `test-generation.md` | `modules/testing/{lang}/test-generation.md` | P1 | BDD/Gherkin test üretimi |
| `hidden-gems-deep-scan.md` | `modules/specialized/{lang}/hidden-gems-deep-scan.md` | P1 | Zombie kod, bus factor tespiti |
| `collaboration-test.md` | `modules/testing/{lang}/collaboration-test.md` | P1 | WebSocket, real-time çok kullanıcı testleri |

#### Faz 3 — Önemli Stub'lar

| Dosya | MANIFEST path | Priority | Açıklama |
|---|---|---|---|
| `dotnet-core.md` | `modules/specialized/{lang}/dotnet-core.md` | P1 | .NET Core / ASP.NET / EF Core analizi |
| `react-typescript.md` | `modules/specialized/{lang}/react-typescript.md` | P1 | React + TypeScript best practices |
| `ui-interaction-test.md` | `modules/testing/{lang}/ui-interaction-test.md` | P1 | Cypress/Playwright UI test senaryoları |
| `ai-assisted-dev-analysis.md` | `modules/specialized/{lang}/ai-assisted-dev-analysis.md` | P1 | Cursor/Copilot/Trae ile geliştirme analizi |
| `turkish-market.md` | `modules/specialized/{lang}/turkish-market.md` | P2 | KVKK, BTK, e-fatura, Türk ödeme sistemleri |
| `feature-gap-analysis.md` | `modules/specialized/{lang}/feature-gap-analysis.md` | P2 | Rakip karşılaştırma, özellik matriksi |
| `mobile-native.md` | `modules/specialized/{lang}/mobile-native.md` | P2 | React Native / Flutter / iOS analizi |
| `cost-analysis.md` | `modules/core/{lang}/cost-analysis.md` | P3 | Cloud maliyet optimizasyonu |
| `resilience-analysis.md` | `modules/core/{lang}/resilience-analysis.md` | P3 | Circuit breaker, retry, fallback |
| `license-analysis.md` | `modules/core/{lang}/license-analysis.md` | P3 | Lisans uyumluluk denetimi |

#### Faz 3 — Guide Stub'lar (Implementation rehberleri)

| Dosya | MANIFEST path | Priority | Açıklama |
|---|---|---|---|
| `accessibility-fixes.md` | `modules/guides/{lang}/accessibility-fixes.md` | P3 | WCAG ihlallerini nasıl düzeltirsin |
| `database-migration.md` | `modules/guides/{lang}/database-migration.md` | P3 | Flyway/Liquibase migration rehberi |
| `performance-optimization.md` | `modules/guides/{lang}/performance-optimization.md` | P3 | Somut optimizasyon adımları |
| `security-fixes.md` | `modules/guides/{lang}/security-fixes.md` | P3 | OWASP bulgularını düzeltme rehberi |

---

### 3.4 Eksik Dokümantasyon Dosyaları (❌ Hiç Yok)

QUICK_START.md'de referans verilen ama projede olmayan dosyalar:

| Dosya | İçerik Beklentisi | Faz |
|---|---|---|
| `USAGE_GUIDE.md` | Kapsamlı kullanım kılavuzu, tüm mode'lar, 20+ örnek | Faz 2 |
| `FAQ.md` | Sık sorulan sorular, troubleshooting | Faz 3 |
| `MODE_TRANSITIONS.md` | Mode 1→2→3 geçiş senaryoları, ne zaman hangi mode | Faz 3 |
| `TURKISH_PROMPTS.md` | 50+ Türkçe prompt örneği, kategori bazlı | Faz 3 |
| `ALGO-COMPLETE.md` | Property-based testing, algoritma doğrulama modülü | Faz 4 |

---

### 3.5 İngilizce Çeviriler (❌ Dizin Var, İçerik Yok)

`{lang}` parametresi ile `en` verildiğinde modüller bulunamıyor. `--lang en` CLI seçeneği çalışmıyor.

**Çeviri kapsamı** (Faz 4):
- `core_prompts/en/BASE_PROMPT.md`
- `core_prompts/en/ORCHESTRATOR_PROMPT.md`
- `modules/core/en/*.md` (20 dosya)
- `modules/domain/en/*.md` (7 dosya)
- `modules/specialized/en/*.md` (10 dosya)
- `modules/testing/en/*.md` (4 dosya)
- `modules/guides/en/*.md` (4 dosya)

---

## 4. Kalite Standartları — Agent İçin

Tüm yeni içerikler için uyulması gereken standartlar:

### Modül kalite kontrol listesi
- [ ] Header: Priority, Tokens, Analysis Time doğru belirtilmiş
- [ ] Purpose: 1 paragraf, net ve özgün
- [ ] Yaml blokları: scoring kriterleri (excellent/good/attention/critical) içeriyor
- [ ] Araç önerileri: Gerçek araç isimleri ve komutlar var
- [ ] Kod örnekleri: Dil belirtilmiş, çalışabilir örnekler
- [ ] Confidence level: Her bulgu tipi için belirtilmiş
- [ ] Output Format: Modülün üretmesi gereken çıktı şablonu var
- [ ] Quick Wins bölümü: En az 3 hızlı kazanım

### Dil tutarlılığı
- Modül iç içerikleri: **İngilizce** (teknik terimler evrensel)
- Türkçe modüller için başlık ve açıklamalar: **Türkçe** (`BASE_PROMPT.md` kuralı)
- Kod ve komutlar: Her zaman **İngilizce**

### Token hedefleri (MANIFEST'teki değerlere uymak)
- core modüller: 1500–3000 token (~6000–12000 karakter)
- specialized modüller: 2000–2500 token
- guide modüller: 1000–2000 token
- testing modüller: 3500–4500 token

---

## 5. Fazlar Özeti

```
Faz 0 (Acil — ~3 saat):
  ├── GLOSSARY.md encoding düzelt
  ├── scoring-criteria.md encoding düzelt + içerik yaz
  ├── merge_modules.py hard-coded path → argparse
  └── analyzer.py Anthropic API desteği ekle

Faz 1 (1–2 gün):
  ├── project-intelligence.md (P0)
  ├── test-generation.md (P1)
  ├── hidden-gems-deep-scan.md (P1)
  ├── collaboration-test.md (P1)
  └── USAGE_GUIDE.md (dokümantasyon)

Faz 2 (2–3 gün):
  ├── dotnet-core.md (P1)
  ├── react-typescript.md (P1)
  ├── ui-interaction-test.md (P1)
  ├── ai-assisted-dev-analysis.md (P1)
  └── turkish-market.md (P2)

Faz 3 (2–3 gün):
  ├── feature-gap-analysis.md, mobile-native.md (P2)
  ├── cost-analysis.md, resilience-analysis.md, license-analysis.md (P3)
  ├── 4 guide modülü (accessibility-fixes, database-migration,
  │   performance-optimization, security-fixes)
  ├── FAQ.md, MODE_TRANSITIONS.md, TURKISH_PROMPTS.md
  └── ALGO-COMPLETE.md

Faz 4 (1 hafta):
  └── Tüm EN çevirileri (45+ dosya)
```

---

## 6. Doğrulama Kriterleri

Her faz sonunda şu kontroller yapılmalı:

```bash
# 1. Encoding kontrolü (bozuk karakter yok mu?)
grep -r "[✅⚡]" modules/ GLOSSARY.md scoring-criteria.md

# 2. Stub kontrolü (içeriksiz dosya kaldı mı?)
find modules/ -name "*.md" -size -500c

# 3. MANIFEST senkronizasyonu (tüm kayıtlı modüller mevcut mu?)
python analyzer.py --target . --mode 1

# 4. Token limiti (derlenen prompt 35K'yı aşıyor mu?)
# analyzer.py zaten tahmini token maliyeti gösteriyor
```
