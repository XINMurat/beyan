# Beyan v2.0 — AI Asistan Görev Promptu (Fazlı)

> **Bu dosyayı nasıl kullanırsın:**
> Her fazı sırasıyla asistanına ver. Bir faz tamamlanıp onaylandıktan sonra bir sonrakine geç.
> Her fazın başına `AGENT_BRIEF.md` içeriğini de ekle veya önceki konuşmada referans ver.

---

# FAZ 0 — Acil Düzeltmeler (~3 saat)

## Görev Bağlamı
Sen Beyan v2.0 adlı bir LLM tabanlı modüler yazılım analiz sistemini geliştiriyorsun. Bu fazda kodda ve dokümantasyonda 4 kritik sorun var. Sırayla hepsini düzelt.

## Görev 0.1 — GLOSSARY.md Encoding Düzeltmesi

**Dosya:** `GLOSSARY.md`

**Sorun:** UTF-8 encoding bozulması nedeniyle `✅` ve `⚡` karakterleri harflerin yerini almış.
Eşleme kuralı: `✅` → `o`, `⚡` → `s` (bağlam okuyarak doğrula).

**Mevcut içerik:**
```
### UMT (Univer⚡al M✅dular Template)
Si⚡temden kaldirildi.

### Bu⚡ Fact✅r
Pr✅jede bilgi ⚡il✅larının ri⚡kini ifade eder.

### Drift Sc✅re
Planlanan mimari ile mevcut k✅d ara⚡ındaki ⚡apma miÇıktıarı.
```

**Olması gereken:** Encoding düzelt, mevcut terim tanımlarını koru, şu terimleri de ekle:

```markdown
# GLOSSARY — Beyan v2.0 Terim Sözlüğü

### UMT (Universal Modular Template)
Sistemden kaldırıldı. v1.x'te kullanılan evrensel şablon mimarisinin adıydı; v2.0'da modüler yapıya geçildi.

### Bus Factor
Projede bilgi silolarının riskini ifade eder. "Bus factor = 1" demek, tek kişi projeyi terk ederse bilgi kaybolur anlamına gelir.

### Drift Score
Planlanan mimari ile mevcut kod arasındaki sapma miktarı. 0–100 arası; düşük değer iyidir.

### Confidence Level
Her bulgunun ne kadar güvenilir olduğunu gösteren yüzdesel ifade. High: 85–100%, Medium: 60–84%, Low: 30–59%.

### P0 / P1 / P2 / P3
Öncelik seviyeleri. P0: Hemen düzelt (güvenlik/veri riski). P1: Bu sprint. P2: Yakında. P3: Backlog.

### Module
MANIFEST.yaml'da tanımlı, belirli bir analiz boyutunu kapsayan .md dosyası. Sadece gerektiğinde yüklenir.

### Auto-load
MANIFEST.yaml'daki `auto_load_if` kuralına göre projenin teknoloji yığınıyla eşleşen modüllerin otomatik yüklenmesi.

### Epistemic Humility
Her bulguya confidence level ekleme, belirsizliği açıkça belirtme ve varsayımları gerçekmiş gibi sunmama prensibi.

### ROI (Return on Investment)
Önerileri önceliklendirirken kullanılan "düşük çaba / yüksek etki" kriteri.

### Agentic Mode
Mode 3: Sistemin insan onayıyla birlikte analiz → plan → kod yaz → test döngüsünü otomatik yürütmesi.
```

---

## Görev 0.2 — scoring-criteria.md Encoding + İçerik

**Dosya:** `modules/core/tr/scoring-criteria.md`

**Sorun:** Encoding bozuk VE içerik yarım.

**Yaz:**

```markdown
# Module: Scoring Criteria and Formulas

**Priority**: P0 (Core System Module)
**Tokens**: ~1500
**Analysis Time**: Otomatik (tüm modüller tamamlandıktan sonra)

---

## Purpose

Tüm modüllerden gelen alt skorları birleştirerek projenin genel sağlık skorunu (0–10) hesaplar. Ağırlıklı ortalama formülü, her boyutun proje tipine göre farklı ağırlığa sahip olmasını sağlar.

---

## Ağırlık Tablosu (Proje Tipine Göre)

```yaml
weights_by_project_type:
  web_app:
    architecture: 0.20
    code_quality:  0.20
    security:      0.20
    performance:   0.15
    testing:       0.15
    documentation: 0.10

  api_backend:
    architecture: 0.25
    code_quality:  0.20
    security:      0.25
    performance:   0.15
    testing:       0.15
    documentation: 0.00  # ağırlık sıfır değil, baseline

  mobile_app:
    architecture: 0.20
    code_quality:  0.20
    security:      0.15
    performance:   0.20
    testing:       0.15
    documentation: 0.10

  data_pipeline:
    architecture: 0.15
    code_quality:  0.15
    security:      0.10
    performance:   0.30
    testing:       0.20
    documentation: 0.10
```

## Hesaplama Formülü

```
Overall Score (O) = Σ (boyut_skoru × boyut_ağırlığı)
Final Score       = min(10, max(0, O))
```

**Örnek:**
- Architecture: 8.0 × 0.20 = 1.60
- Code Quality:  7.0 × 0.20 = 1.40
- Security:      6.0 × 0.20 = 1.20
- Performance:   8.5 × 0.15 = 1.28
- Testing:       5.0 × 0.15 = 0.75
- Documentation: 7.0 × 0.10 = 0.70
- **Toplam: 6.93 / 10**

---

## Skor Aralıkları ve Anlamları

```yaml
score_ranges:
  9.0 - 10.0:
    status: "🟢 Mükemmel"
    meaning: "Production-ready, minimal risk"
    action: "Periyodik takip yeterli"

  7.0 - 8.9:
    status: "🟡 İyi"
    meaning: "Birkaç iyileştirme noktası var"
    action: "P1 sorunları bu sprint ele al"

  5.0 - 6.9:
    status: "🟠 Orta"
    meaning: "Dikkat gerektiren sorunlar mevcut"
    action: "P0 ve P1 sorunları acilen çöz"

  0.0 - 4.9:
    status: "🔴 Kritik"
    meaning: "Production'a çıkma riski yüksek"
    action: "Acil müdahale gerekli, deployment durdur"
```

---

## Kritik Override Kuralları

Genel skor ne olursa olsun, şu durumlar skoru otomatik olarak düşürür:

```yaml
critical_overrides:
  any_p0_finding:
    description: "Herhangi bir P0 bulgu varsa"
    cap_score_at: 6.0
    reason: "P0 = production outage veya güvenlik açığı riski"

  security_score_below_5:
    description: "Security skoru 5'in altındaysa"
    cap_score_at: 5.5
    reason: "Güvenlik açığı tüm sistemi tehdit eder"

  test_coverage_below_20:
    description: "Test coverage %20'nin altındaysa"
    deduct: 1.0
    reason: "Kör bölge riski çok yüksek"

  no_readme:
    description: "README.md yoksa"
    deduct: 0.5
    reason: "Onboarding imkansız"
```

---

## Output Format

```markdown
## Proje Sağlık Skoru: X.X / 10 [STATUS_EMOJI]

| Boyut | Skor | Ağırlık | Katkı |
|-------|------|---------|-------|
| Architecture | X.X | %20 | X.XX |
| Code Quality | X.X | %20 | X.XX |
| Security | X.X | %20 | X.XX |
| Performance | X.X | %15 | X.XX |
| Testing | X.X | %15 | X.XX |
| Documentation | X.X | %10 | X.XX |
| **TOPLAM** | | | **X.XX** |

[Varsa override açıklamaları]
```
```

---

## Görev 0.3 — merge_modules.py Hard-coded Path Düzeltmesi

**Dosya:** `merge_modules.py`

**Sorun:** Satır 6–7'deki Windows'a özgü sabit yollar cross-platform değil.

**Dosyayı şu değişikliklerle güncelle:**

1. `argparse` ekle, `--v3` ve `--v2` argümanlarını al
2. Mevcut hard-coded path'leri kaldır
3. Başa kullanım talimatı ekle:

```python
#!/usr/bin/env python3
"""
Beyan v1→v2 Module Migration Tool

Usage:
    python merge_modules.py --v3 /path/to/beyan-v1 --v2 /path/to/beyan-v2
    python merge_modules.py --v3 ../project-analysis-system-v3.3.1 --v2 .
"""
import argparse
import os
import shutil
import yaml
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Beyan v1 → v2 module migration tool")
    parser.add_argument("--v3", required=True, help="Kaynak v3 dizini (project-analysis-system-v3.x)")
    parser.add_argument("--v2", required=True, help="Hedef v2 dizini (beyan-v2.0-agentic)")
    parser.add_argument("--dry-run", action="store_true", help="Değişiklik yapmadan önizle")
    args = parser.parse_args()

    v3 = Path(args.v3).resolve()
    v2 = Path(args.v2).resolve()

    if not v3.exists():
        print(f"[HATA] v3 dizini bulunamadı: {v3}")
        return 1
    if not v2.exists():
        print(f"[HATA] v2 dizini bulunamadı: {v2}")
        return 1

    print(f"[*] Kaynak (v3): {v3}")
    print(f"[*] Hedef  (v2): {v2}")
    if args.dry_run:
        print("[*] DRY-RUN modu — hiçbir dosya kopyalanmayacak\n")

    # ... (geri kalan mevcut mantık aynen korunur, sadece v3/v2 değişkenleri argparse'tan geliyor)
```

---

## Görev 0.4 — analyzer.py Anthropic API Desteği

**Dosya:** `analyzer.py`

`compile_prompt()` fonksiyonunun sonuna, mevcut `if api_choice == "openai":` bloğundan sonra şu bloğu ekle:

```python
elif api_choice == "anthropic":
    try:
        import anthropic
    except ImportError:
        msg = "[ERROR] anthropic package not installed. Run: pip install anthropic" if lang == "en" \
              else "[HATA] anthropic paketi kurulu değil. Çalıştır: pip install anthropic"
        print(msg)
        return

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        msg = "[ERROR] ANTHROPIC_API_KEY environment variable not set." if lang == "en" \
              else "[HATA] ANTHROPIC_API_KEY ortam değişkeni bulunamadı."
        print(msg)
        return

    model = "claude-sonnet-4-6"
    print(f"[*] Anthropic API'sine istek gönderiliyor ({model})...")

    client = anthropic.Anthropic(api_key=api_key)

    try:
        system_prompt = (
            "You are the Master Controller of the Beyan Agentic Framework. "
            "Analyze the provided project prompt and return a structured analysis report."
        ) if lang == "en" else (
            "Sen Beyan Agentic Framework'ün Ana Kontrolcüsüsün. "
            "Sağlanan proje promptunu analiz et ve Türkçe yapılandırılmış analiz raporu üret."
        )

        message = client.messages.create(
            model=model,
            max_tokens=8192,
            system=system_prompt,
            messages=[
                {"role": "user", "content": compiled_text[:120000]}  # ~100K token güvenli limit
            ]
        )

        result = message.content[0].text

        res_file = target_path / "beyan_analysis_result.md"
        with open(res_file, "w", encoding="utf-8") as f:
            f.write(result)

        msg = f"[SUCCESS] Analysis complete, saved to: {res_file.absolute()}" if lang == "en" \
              else f"[BAŞARILI] Analiz tamamlandı ve kaydedildi: {res_file.absolute()}"
        print(msg)

    except Exception as e:
        msg = f"[ERROR] Anthropic API error: {e}" if lang == "en" \
              else f"[HATA] Anthropic API hatası: {e}"
        print(msg)
```

Ayrıca dosyanın başındaki import bloğuna ekle:
```python
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
```

---

## Faz 0 Tamamlanma Kriterleri

- [ ] `GLOSSARY.md` okunabilir, encoding bozukluğu yok
- [ ] `scoring-criteria.md` tam içerikli, encoding sorunu giderildi
- [ ] `merge_modules.py` `--v3` ve `--v2` argümanı alıyor, Windows path yok
- [ ] `analyzer.py` `--api anthropic` seçeneği çalışıyor
- [ ] `python analyzer.py --help` hata vermiyor

---
---

# FAZ 1 — Kritik Stub Modüller + USAGE_GUIDE (~2 gün)

## Görev Bağlamı
Faz 0 tamamlandı. Şimdi P0 ve P1 öncelikli 5 stub modülü ve USAGE_GUIDE.md dosyasını yazıyorsun.

Her modülü yazarken **referans dosyaları** oku:
- `performance-analysis.md` — Scoring yaml formatı için
- `security-analysis.md` — Confidence level notasyonu için
- `ui-ux-analysis.md` — Output format şablonu için

**Önemli:** Her modülü ayrı bir dosya olarak kaydet. Türkçe sürümler `modules/*/tr/` altına, İngilizce (Faz 4'e ertelendi) şimdilik boş bırak.

---

## Görev 1.1 — project-intelligence.md

**Kaydet:** `modules/specialized/tr/project-intelligence.md`
**MANIFEST tokens:** ~5000  
**Priority:** P0

Bu modül sistemin "beyin"idir. Bir projeyi ilk gördüğünde neye baktığını, nasıl sınıflandırdığını ve hangi modülleri yükleyeceğini belirler.

**İçermesi gerekenler:**

1. **Proje Tipi Algılama** — Hangi dosyalar hangi proje tipine işaret eder:
   - `package.json` → web/frontend
   - `*.csproj` / `*.sln` → .NET backend
   - `requirements.txt` + `*.ipynb` → AI/ML
   - `Dockerfile` → DevOps
   - `*.sol` → Blockchain
   - vb.

2. **Olgunluk Seviyesi Tespiti**:
   - Early: README yok, test yok, tek branch
   - Growing: Temel CI var, bazı testler
   - Mature: CI/CD, %70+ test coverage, semantic versioning
   - Production: Monitoring, SLA, incident management

3. **Modül Öneri Matrisi** — Proje tipine ve olgunluğa göre hangi modüllerin yükleneceği:

```yaml
recommendation_matrix:
  web_app + production:
    always: [file_structure, security_analysis, performance_analysis, ui_ux_analysis]
    likely: [accessibility_analysis, api_design_analysis, database_analysis]
    optional: [i18n, seo, analytics]

  api_backend + mature:
    always: [security_analysis, api_design_analysis, database_analysis]
    likely: [performance_analysis, testing_strategy]
    optional: [developer_experience, monitoring_observability]
  # ... diğer tipler
```

4. **Drift Detection** — Vision vs. Reality karşılaştırması için veri toplama.

5. **Output Format** — Standart proje keşif raporu şablonu.

---

## Görev 1.2 — test-generation.md

**Kaydet:** `modules/testing/tr/test-generation.md`
**MANIFEST tokens:** ~4000  
**Priority:** P1

**İçermesi gerekenler:**

1. **BDD / Gherkin Test Senaryoları** — Given/When/Then formatı, gerçek örneklerle:
   ```gherkin
   Feature: User Authentication
     Scenario: Successful login
       Given the user is on the login page
       When they enter valid credentials
       Then they should be redirected to the dashboard
   ```

2. **Test Türleri ve Araçlar**:
   - Unit tests: Jest (JS/TS), pytest (Python), xUnit (.NET)
   - Integration tests: Supertest, RestAssured
   - E2E tests: Cypress, Playwright
   - Coverage: Istanbul/NYC, pytest-cov

3. **Test Coverage Analizi**:
   ```yaml
   coverage_scoring:
     excellent: ">= 80% lines, >70% branches"
     good: "70-79%"
     attention: "50-69%"
     critical: "< 50%"
   ```

4. **Kod'dan Test Üretme** — Mevcut koda bakarak otomatik test senaryosu önerisi:
   - Input boundary cases
   - Error handling paths
   - Happy path + edge cases

5. **Test Kalitesi Değerlendirmesi** — Flaky test tespiti, assert density, mock abuse.

6. **Output:** Proje için hazır test dosyası iskeletleri.

---

## Görev 1.3 — hidden-gems-deep-scan.md

**Kaydet:** `modules/specialized/tr/hidden-gems-deep-scan.md`
**MANIFEST tokens:** ~2500  
**Priority:** P1

**İçermesi gerekenler:**

1. **Zombie Kod Tespiti**:
   - Hiç çağrılmayan fonksiyonlar
   - Dead imports
   - Feature flag'ler arkasında kalmış kod
   - Araçlar: `ts-prune`, `deadcode`, coverage reports

2. **Bus Factor Analizi**:
   ```yaml
   bus_factor:
     critical: "1 — tek kişi bilir, ayrılırsa kriz"
     low: "2-3 — risk var ama yönetilebilir"
     healthy: "4+ — bilgi dağılmış"
   nasil_olcersin:
     - git log --author ile commit yoğunluğu
     - Dosya başına committer sayısı
     - "Bu dosyayı kim en son değiştirdi?"
   ```

3. **Teknik Borç Tespiti**:
   - TODO/FIXME/HACK yorum sayısı ve yoğunluğu
   - Cyclomatic complexity hotspot'ları
   - Duplicate code (copy-paste oranı)

4. **Gizli Bağımlılıklar**:
   - Circular dependencies
   - Implicit global state
   - Undocumented side effects

5. **Yüksek Değerli "Gem" Bulgular** — İyi yazılmış ama bilinmeyen/takdir görmeyen kod parçaları.

---

## Görev 1.4 — collaboration-test.md

**Kaydet:** `modules/testing/tr/collaboration-test.md`
**MANIFEST tokens:** ~3500  
**Priority:** P1

**İçermesi gerekenler:**

1. **WebSocket / SignalR Test Stratejisi**:
   - Bağlantı kurma ve kopma senaryoları
   - Yeniden bağlanma davranışı
   - Message ordering garantisi
   - Backpressure handling

2. **Çok Kullanıcılı Senaryo Testleri**:
   ```yaml
   test_scenarios:
     concurrent_edit:
       - "2 kullanıcı aynı kaynağı aynı anda düzenliyor"
       - "Conflict resolution beklenen davranışa uyuyor mu?"
     user_join_leave:
       - "Kullanıcı katıldığında mevcut state doğru aktarılıyor mu?"
       - "Kullanıcı ayrıldığında cursors/presence temizleniyor mu?"
     network_partition:
       - "Bağlantı 5 saniye kopsa state ne olur?"
   ```

3. **CRDT / OT Uyumluluk Testleri** (varsa):
   - Convergence testleri
   - Merge conflict simülasyonu

4. **Performans ve Ölçek**:
   - 100 eşzamanlı kullanıcı test senaryosu
   - Message latency ölçümü
   - Memory leak tespiti

5. **Araçlar:** Socket.IO tester, Artillery, k6 websocket.

---

## Görev 1.5 — USAGE_GUIDE.md

**Kaydet:** Proje kök dizinine `USAGE_GUIDE.md`

**İçermesi gerekenler:**

### Bölüm 1: Kurulum
- Python gereksinimleri
- `pip install -r requirements.txt`
- Ortam değişkenleri (OPENAI_API_KEY, ANTHROPIC_API_KEY)

### Bölüm 2: Hızlı Başlangıç
- `analyzer.py` komut satırı örnekleri
- Mode 1, 2, 3 ne zaman kullanılır

### Bölüm 3: Modülleri Anlama
- MANIFEST.yaml okuma rehberi
- Auto-load nasıl çalışır
- Manuel modül yükleme

### Bölüm 4: İleri Kullanım
- Özel modül yazma
- Kendi sektörüne özel modül ekleme
- Token optimizasyonu

### Bölüm 5: Çıktıları Yorumlama
- Skor aralıkları ne anlama geliyor
- P0–P3 aksiyonları nasıl önceliklendirilir
- Takım ile paylaşma

### Bölüm 6: Sorun Giderme
- Context window dolu hatası
- Modül bulunamadı hatası
- Türkçe yerine İngilizce geldi

Toplam: ~800–1200 satır, gerçek komut çıktılarıyla.

---

## Faz 1 Tamamlanma Kriterleri

- [ ] `modules/specialized/tr/project-intelligence.md` mevcut ve doluysa
- [ ] `modules/testing/tr/test-generation.md` ≥ 150 satır
- [ ] `modules/specialized/tr/hidden-gems-deep-scan.md` ≥ 100 satır
- [ ] `modules/testing/tr/collaboration-test.md` ≥ 120 satır
- [ ] `USAGE_GUIDE.md` ≥ 200 satır, tüm bölümler var
- [ ] `python analyzer.py --target . --mode 1` hatasız çalışıyor

---
---

# FAZ 2 — Teknoloji Stack Modülleri (~2-3 gün)

## Görev Bağlamı
Faz 1 tamamlandı. Şimdi belirli teknoloji stacklerine odaklanan 5 stub modülü yazıyorsun. Bunlar `auto_load_if` ile ilgili dosya uzantıları/isimlere göre otomatik tetikleniyor.

---

## Görev 2.1 — dotnet-core.md

**Kaydet:** `modules/specialized/tr/dotnet-core.md`
**MANIFEST tokens:** ~1800  
**Trigger:** `.csproj`, `asp.net`, `entity-framework`

**İçermesi gerekenler:**

1. **ASP.NET Core Yapısal Analiz**:
   - Controller → Service → Repository katman ayrımı
   - Dependency Injection doğru kullanımı
   - Middleware pipeline değerlendirmesi

2. **Entity Framework Core**:
   - N+1 query tespiti (AsNoTracking, Include kullanımı)
   - Migration yönetimi
   - Connection pooling

3. **Güvenlik** (.NET'e özgü):
   - [Authorize] attribute kullanımı
   - Anti-forgery token
   - CORS politikası
   - Secret Manager vs. appsettings.json

4. **Performans**:
   - Async/await doğru kullanımı (Result veya Wait() antipattern tespiti)
   - Response caching
   - IMemoryCache vs. IDistributedCache

5. **Scoring:** .NET'e özgü kod kalite metrikleri

---

## Görev 2.2 — react-typescript.md

**Kaydet:** `modules/specialized/tr/react-typescript.md`
**MANIFEST tokens:** ~2000  
**Trigger:** `react`, `typescript`, `.tsx`

**İçermesi gerekenler:**

1. **TypeScript Strict Mode Analizi**:
   - `tsconfig.json` kontrolleri
   - `any` kullanım sıklığı
   - Type assertion kötüye kullanımı

2. **React Best Practices**:
   - Hook kuralları (Rules of Hooks)
   - useEffect dependency array hataları
   - Gereksiz re-render tespiti (useMemo, useCallback)
   - Key prop antipatternleri

3. **State Management**:
   - Context API overuse
   - Prop drilling derinliği
   - Redux/Zustand/Jotai kullanım değerlendirmesi

4. **Component Kalitesi**:
   - God component tespiti (>300 satır)
   - Separation of Concerns
   - Custom hook fırsatları

5. **Bundle Analizi**:
   - tree-shaking etkinliği
   - Lazy loading fırsatları

---

## Görev 2.3 — ui-interaction-test.md

**Kaydet:** `modules/testing/tr/ui-interaction-test.md`
**MANIFEST tokens:** ~4500  
**Trigger:** `visual_builder`, `canvas`, `drag_drop`, `ui_request`

**İçermesi gerekenler:**

1. **Cypress ve Playwright Karşılaştırması**:
   - Ne zaman Cypress, ne zaman Playwright
   - Konfigürasyon örnekleri

2. **Visual Builder / Canvas Testleri**:
   - Drag-and-drop test senaryoları
   - Canvas element seçimi
   - Snapshot testing

3. **Form Test Senaryoları**:
   - Validation error gösterimi
   - Submit davranışı
   - Async validation

4. **Accessibility Otomasyonu**:
   - axe-core entegrasyonu
   - Keyboard navigation testi

5. **Test Data Yönetimi**:
   - Fixtures
   - Mock API responses
   - Database seeding

---

## Görev 2.4 — ai-assisted-dev-analysis.md

**Kaydet:** `modules/specialized/tr/ai-assisted-dev-analysis.md`
**MANIFEST tokens:** ~2500  
**Trigger:** `trae_ide`, `cursor`, `copilot`

**İçermesi gerekenler:**

1. **AI Kod Üretiminin Riskleri**:
   - Halüsinasyon tespiti (gerçek olmayan kütüphane importları)
   - Güvenlik açığı içeren üretilmiş kod kalıpları
   - Test coverage'sız üretilen kod

2. **Kalite Göstergeleri** (AI-assisted projeye özgü):
   - Commit mesajlarının kalitesi
   - Code review yoğunluğu
   - Refactoring sıklığı

3. **AI Araç Uyumluluk Değerlendirmesi**:
   - .cursorrules / .trae dosyası kalitesi
   - Context window optimize prompt örnekleri

4. **İnsan + AI İş Birliği Metrikleri**:
   - Hangi dosyalar tamamen AI üretimi? (commit mesajı analizi)
   - Hangi bölümler insan onayı aldı?

---

## Görev 2.5 — turkish-market.md

**Kaydet:** `modules/specialized/tr/turkish-market.md`
**MANIFEST tokens:** ~1500  
**Trigger:** `turkish`, `turkey`, `tr`

**İçermesi gerekenler:**

1. **KVKK Uyumluluk Kontrolleri**:
   - Açık rıza mekanizması
   - Veri silme hakkı (sağ olmak hakkı)
   - Veri işleme envanteri
   - Yurt dışı veri transferi kuralları

2. **BTK Gereklilikleri**:
   - Bilgi Teknolojileri ve İletişim Kurumu bildirimleri
   - E-ticaret kanunu uyumu
   - Sosyal medya yönetmeliği (varsa)

3. **Türk Ödeme Sistemleri**:
   - Iyzico / PayTR / Sipay entegrasyon kalite değerlendirmesi
   - 3D Secure zorunluluğu
   - BDDK uyumu

4. **Yerel Teknik Gereklilikler**:
   - Türkçe karakter encoding (UTF-8)
   - Türkçe tarih/para formatı
   - E-fatura / E-arşiv entegrasyonu (GİB)
   - KEP (Kayıtlı Elektronik Posta)

5. **Scoring:** Türkiye'ye özgü uyumluluk skoru

---

## Faz 2 Tamamlanma Kriterleri

- [ ] 5 modülün tamamı ≥ 100 satır, MANIFEST formatına uygun
- [ ] Her modülde scoring yaml bloğu var
- [ ] Her modülde en az 1 kod örneği var
- [ ] `analyzer.py --target /csharp-proje` çalıştırıldığında `dotnet-core` yükleniyor
- [ ] `analyzer.py --target /react-proje` çalıştırıldığında `react-typescript` yükleniyor

---
---

# FAZ 3 — Rehber Modüller + Kalan Stub'lar + Yardımcı Dosyalar (~3 gün)

## Görev Bağlamı
Faz 2 tamamlandı. Bu fazda kalan 9 stub modülü, 4 guide modülü ve 3 yardımcı dokümantasyon dosyasını tamamlıyorsun.

---

## Görev 3.1 — 4 Guide Modülü

Rehber modüller *analiz* değil, *nasıl düzeltilir* sorusunu yanıtlar. Somut adımlar, kod örnekleri ve checklist'ler içerir.

**`modules/guides/tr/accessibility-fixes.md`** — WCAG 2.1 ihlallerini düzeltme rehberi. Renk kontrastı, ARIA label, keyboard navigation, focus management.

**`modules/guides/tr/database-migration.md`** — Güvenli migration rehberi. Flyway/Liquibase, zero-downtime migration, rollback stratejisi.

**`modules/guides/tr/performance-optimization.md`** — Somut optimizasyon adımları. Frontend: code splitting, lazy loading. Backend: query optimizasyon, caching katmanı.

**`modules/guides/tr/security-fixes.md`** — OWASP Top 10 bulgularını düzeltme. SQL injection, XSS, CSRF, Secret Management.

Her guide için format:
```markdown
# Guide: [Başlık]
## Sorun: [Kısaca ne]
## Etki: [Neden önemli]
## Çözüm Adımları (numaralı liste)
## Kod Örnekleri (önce: ❌ Yanlış, sonra: ✅ Doğru)
## Doğrulama (nasıl test edersin)
## Kaynaklar
```

---

## Görev 3.2 — Kalan 9 Stub Modül

Aşağıdakileri sırayla yaz. Her biri için MANIFEST'teki token hedefine bak:

**`modules/specialized/tr/feature-gap-analysis.md`** (~2500 token)
Rakip ürünlerle özellik karşılaştırması. Feature matrix oluşturma, pazar standardı benchmarking, roadmap önerileri.

**`modules/specialized/tr/mobile-native.md`** (~800 token)
React Native / Flutter / iOS / Android'e özgü analiz. Performance, native module kalitesi, deep link yapısı.

**`modules/core/tr/cost-analysis.md`** (~800 token)
Cloud maliyet analizi. AWS/Azure/GCP maliyet optimizasyon önerileri, reserved instance fırsatları, waste tespiti.

**`modules/core/tr/resilience-analysis.md`** (~800 token)
Circuit breaker, retry mekanizması, timeout değerleri, fallback stratejisi, chaos engineering hazırlığı.

**`modules/core/tr/license-analysis.md`** (~800 token)
Dependency lisans uyumluluğu. GPL/MIT/Apache karışımı riskleri, ticari kullanım kısıtlamaları, SBOM oluşturma.

---

## Görev 3.3 — FAQ.md

**Kaydet:** `FAQ.md` (proje kök)

Şu kategorilerde soru-cevap:
- Genel kullanım (10 soru)
- Teknik sorunlar (8 soru)
- Modüller hakkında (6 soru)
- Çıktıları yorumlama (6 soru)
- Katkıda bulunma (4 soru)

---

## Görev 3.4 — MODE_TRANSITIONS.md

**Kaydet:** `MODE_TRANSITIONS.md` (proje kök)

İçerik:
- Mode 1 → Mode 2 geçiş senaryosu (ne zaman plan isterim)
- Mode 2 → Mode 3 geçiş senaryosu (ne zaman otomatik düzeltme isterim)
- Mode 3'te insan onay noktaları nerede
- Geri alma (rollback) senaryosu

---

## Görev 3.5 — TURKISH_PROMPTS.md

**Kaydet:** `TURKISH_PROMPTS.md` (proje kök)

50+ Türkçe prompt örneği, kategorilere göre:
- Genel analiz
- Güvenlik
- Performans
- Test
- DevOps
- E-ticaret'e özgü
- SaaS'a özgü
- Mobil app'e özgü
- Proje yönetimi

---

## Faz 3 Tamamlanma Kriterleri

- [ ] 4 guide modülü doluysa ve format doğruysa
- [ ] 9 stub modülü ≥ 80 satır/adet
- [ ] `FAQ.md`, `MODE_TRANSITIONS.md`, `TURKISH_PROMPTS.md` mevcut
- [ ] `find modules/ -name "*.md" -size -500c` sonuç vermiyorsa (stub kalmadı)

---
---

# FAZ 4 — ALGO-COMPLETE.md + İngilizce Çeviriler (~1 hafta)

## Görev Bağlamı
Bu faz en kapsamlı fazdır. İki bağımsız alt görev içerir ve paralel yürütülebilir.

---

## Görev 4A — ALGO-COMPLETE.md

**Kaydet:** `ALGO-COMPLETE.md` (proje kök)
**MANIFEST tokens:** ~8000  
**Açıklama:** Property-based testing ve algoritma doğrulama modülü.

**İçermesi gerekenler:**

1. **Property-Based Testing Nedir?** — Hypothesis, fast-check, FsCheck ile örnekler
2. **Matematiksel Doğrulama**:
   - Invariant tespiti
   - Pre/post condition tanımlama
   - Formal verification introduction
3. **İstatistiksel Test Teknikleri**:
   - Fuzz testing
   - Mutation testing
   - Model-based testing
4. **Algoritma Kalite Kriterleri**:
   - Big-O analizi
   - Edge case coverage
   - Numerical stability
5. **Dil Bazlı Örnekler**: Python, TypeScript, C#
6. **Otomatik Test Senaryosu Üreteci** şablonu

---

## Görev 4B — İngilizce Çeviriler

**Hedef:** Tüm TR modüllerinin EN sürümlerini oluştur.

**Kapsam:**
- `core_prompts/en/BASE_PROMPT.md`
- `core_prompts/en/ORCHESTRATOR_PROMPT.md`
- `modules/core/en/` — 20 dosya
- `modules/domain/en/` — 7 dosya
- `modules/specialized/en/` — 10 dosya
- `modules/testing/en/` — 4 dosya
- `modules/guides/en/` — 4 dosya

**Çeviri kuralları:**
- Teknik terimler İngilizce kalır (zaten İngilizce)
- Türkçe açıklamalar İngilizce'ye çevrilir
- Kod örnekleri değişmez
- Scoring yaml'ları değişmez
- Türkiye'ye özgü modül (`turkish-market.md`) EN versiyonunda "For Turkish market compliance" başlığıyla korunur

**Öneri:** Faz 4B'yi 10'ar dosyalık alt fazlara bölerek yürüt.

---

## Faz 4 Tamamlanma Kriterleri

- [ ] `ALGO-COMPLETE.md` ≥ 300 satır
- [ ] `modules/*/en/` dizinlerinde TR ile eş sayıda dosya var
- [ ] `python analyzer.py --target /proje --lang en` hatasız çalışıyor
- [ ] `verify_integrity.ps1` (veya Python eşdeğeri) tüm fazlarda pass ediyor

---

## Son Kontrol — Tüm Fazlar Bitti mi?

```bash
# 1. Encoding hatası yok
grep -r "[✅⚡]" . --include="*.md"
# → Sonuç boş olmalı

# 2. Stub kalmadı
find modules/ -name "*.md" -size -500c
# → Sonuç boş olmalı

# 3. MANIFEST senkron
python analyzer.py --target . --mode 1 --lang tr
python analyzer.py --target . --mode 1 --lang en
# → Her ikisi de hatasız çalışmalı

# 4. Eksik referans yok
grep -r "USAGE_GUIDE\|FAQ\.md\|MODE_TRANSITIONS\|TURKISH_PROMPTS\|ALGO-COMPLETE" QUICK_START.md
# → Her referans artık gerçek bir dosyaya işaret etmeli

# 5. Token limiti
# analyzer.py çıktısında "Tahmini Token Maliyeti: X (Limit: 35000)"
# Herhangi bir senaryo için X > 35000 ise o kombinasyonu optimize et
```

---

*Beyan v2.0 — Agent Görev Promptu v1.0 | Hazırlanma: 17 Nisan 2026*
