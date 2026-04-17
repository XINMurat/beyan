# Module: Project Intelligence

**Priority**: P0 (Meta-Orchestrator Module)
**Tokens**: ~5000
**Analysis Time**: İlk aşama (Discovery Phase)

---

## Purpose
Bu modül, hedeflenen projenin genel yapısını, teknoloji yığınını (tech stack), olgunluk seviyesini (maturity) ve mimari vizyon ile mevcut kod arasındaki sapmayı (Drift) analiz ederek sistemin "beyni" olarak işlev görür. Projeye hangi spesifik modüllerin yükleneceğine karar verilmesinde rehberlik eder.

---

## Proje Tipi ve Teknoloji Yığını Algılama

Yapay zeka, projenin kök dizinindeki dosya ve bağımlılıklara bakarak proje tipini belirlemelidir:

```yaml
project_type_heuristics:
  web_frontend:
    indicators: ["package.json", "src/App.js", "src/App.tsx", "index.html", "next.config.js", "vite.config.js"]
    confidence: High
  api_backend:
    indicators: ["requirements.txt", "Pipfile", "pom.xml", "build.gradle", "go.mod", "src/main.rs", ".csproj"]
    confidence: High
  mobile_app:
    indicators: ["android/app/build.gradle", "ios/Podfile", "pubspec.yaml", "app.json"]
    confidence: High
  data_ml_pipeline:
    indicators: ["jupyter", ".ipynb", "dbt_project.yml", "airflow", "dag", "mlflow"]
    confidence: Medium
  devops_infra:
    indicators: ["Dockerfile", "docker-compose.yml", "kubernetes", ".tf", "terraform", "ansible"]
    confidence: High
  blockchain_web3:
    indicators: ["hardhat.config.js", "truffle-config.js", "*.sol", "Anchor.toml"]
    confidence: High
```

### Olgunluk Seviyesi (Maturity) Tespiti

Projenin olgunluk seviyesi, aşağıdaki kriterlere göre belirlenmelidir:

```yaml
maturity_levels:
  Early_Stage:
    characteristics: "README yok veya çok zayıf, test dosyaları (0-10% coverage), tek branch üzerinden çalışma, CI/CD yok."
    recommendation: "Temel dosya yapısı, linting ve temel test altyapısı önerilmeli."
  Growing:
    characteristics: "README mevcut, temel CI (örn. GitHub Actions ile lint/build) var, bazı testler (%10-40 coverage)."
    recommendation: "Gelişmiş testler, CI/CD optimizasyonu ve mimari desenlerin (patterns) oturtturulması önerilmeli."
  Mature:
    characteristics: "Detaylı dokümantasyon, Semantic Versioning, tam teşekküllü CI/CD, yüksek test kapsayıcılığı (>%70), staging ortamları."
    recommendation: "Performans, güvenlik denetimleri ve uç durum (edge-case) senaryoları analiz edilmeli."
  Production_Ready:
    characteristics: "Monitoring (Gözlemlenebilirlik), SLA/SLO dokümantasyonu, Incident Management süreçleri."
    recommendation: "Resilience (Direnç), yük testleri ve cost (maliyet) optimizasyonlarına odaklanılmalı."
```

---

## Modül Öneri Matrisi (Module Recommendation Matrix)

Proje tipi ve olgunluk seviyesine göre yapay zekanın yüklenmesini (manuel modda) veya aksiyon alınmasını önereceği alt modüller şunlardır:

```yaml
recommendation_matrix:
  web_frontend + mature:
    always: [file_structure, security_analysis, performance_analysis, ui_ux_analysis]
    likely: [accessibility_analysis, api_design_analysis, i18n]
    optional: [seo, analytics]

  api_backend + production:
    always: [security_analysis, api_design_analysis, database_analysis, performance_analysis]
    likely: [testing_strategy, resilience_analysis]
    optional: [developer_experience, monitoring_observability]

  blockchain_web3 + early:
    always: [smart_contract_security, gas_optimization]
    likely: [file_structure]
    optional: []
```

---

## Özel Durum Tespiti

Aşağıdaki durumlardan herhangi biri varsa, normal modül seçiminin dışında ek aksiyon alınmalıdır:

```yaml
special_cases:
  migration_in_progress:
    signal: "Hem eski hem yeni sistem aynı depoda"
    action: "legacy-migration modülünü zorunlu ekle"

  security_critical:
    signal: "Sağlık, finans, kimlik doğrulama veya kriptografi bileşenleri"
    action: "security-audit modülü P0 olarak yükle"

  public_api:
    signal: "API birden fazla dış tüketiciye açık"
    action: "api-audit modülünü ekle"

  docs_only_system:
    signal: "Depoda yalnızca .md dosyaları var"
    action: "meta-analysis modülünü yükle"

  research_plus_production:
    signal: "Hem araştırma hem üretim bileşeni aynı depoda"
    action: "ai-research + web-mobile modüllerini paralel yükle"

  very_early_stage:
    signal: "README yok veya 5 satırdan az, test dosyası yok"
    action: "Önce scoring-criteria ile genel sağlık skoru al, derinlemesine analiz sonra"

  monorepo:
    signal: "Tek depoda birden fazla bağımsız proje"
    action: "Aşağıdaki Monorepo Karar Ağacını uygula"
```

---

## Monorepo Karar Ağacı

Tek bir Git deposunda birden fazla bağımsız proje/servis bulunduğunda:

```
Tek depoda kaç bağımsız proje var?
│
├── 2–3 proje
│     → Her biri için ayrı triyaj raporu üret
│     → Modülleri her alt proje için ayrı ayrı seç
│     → Çıktı: docs/triage/[proje-adi]_report.md (her proje için)
│
├── 4+ proje
│     → Önce kapsam belirle: hangi alt projeler bu analizin hedefi?
│     │
│     ├── Tümü → Her biri için ayrı triyaj raporu
│     │         → Ortak üst navigasyon: docs/index.md
│     │
│     └── Seçilmişler → Yalnızca hedeflenenler için triyaj yap
│                       → Diğerlerini "kapsam dışı" olarak belgele
│
└── Paylaşımlı kütüphane / altyapı var mı?
      Evet → Bu ortak bileşeni ayrıca belgele
             → Bağımlı projelerin analizinde bu bileşene referans ver
             → Ortak bileşendeki değişikliklerin tüm projelere etkisini değerlendir
```

**Monorepo Özel Puanlama:**
- Her alt proje kendi sağlık skoru alır
- Paylaşımlı bileşendeki P0 bulgu → tüm bağımlı projelerin skoru **otomatik olarak 6.5 üst sınırına çekilir**
- `docs/monorepo_summary.md` tüm alt proje skorlarını özetler

---

## Drift Detection (Vizyon vs Gerçeklik)

Geliştiricinin planladığı mimari (eğer `ARCHITECTURE.md` veya README'de belirtilmişse) ile koddaki gerçek mimari karşılaştırılarak "Drift Score" (Sapma Skoru) çıkarılmalıdır.

*   **Örnek Drift:** README "Microservices kullanıldı" diyor ancak kod devasa tek bir Monolith içeriyor.
*   **Örnek Drift:** "Katmanlı Mimari (Clean Architecture)" hedeflenmiş fakat Veritabanı (SQL) çağrıları doğrudan UI bileşenleri içinde yapılmış.

---

## Scoring

Bu modül doğrudan 0-10 puan arası bir skor üretmez; ancak genel proje zekasını ve dokümantasyon/vizyon netliğini şu şekilde kategorize eder:

```yaml
scoring:
  excellent: "Proje tipi net, olgunluk production seviyesinde, drift skoru %0-5 (Plan ve kod uyumlu)."
  good: "Proje anlaşılır, olgunluk growing/mature seviyelerinde, ufak çaplı mimari sapmalar var."
  attention: "Birden çok teknoloji yığını karmaşıklaşmış, olgunluk early seviyesinde, vizyon ve kod arası bariz farklar var."
  critical: "Kod tabanında belirgin bir teknoloji örüntüsü yok, dokümantasyon sıfır, drift skoru >%50."
```

---

## Output Format

Yapay zekanın bu modülü işledikten sonra üreteceği rapor formatı:

```markdown
## 🧠 Project Intelligence & Keşif

- **Proje Tipi:** [Örn: React/Node.js Fullstack Web App]
- **Olgunluk Seviyesi:** [Örn: Growing]
- **Tahmini Bus Factor Riski:** [Low / Medium / High]

### 🎯 Drift Analizi
- **Vizyon:** [Dokümantasyonda iddia edilen yapı]
- **Gerçeklik:** [Koddaki mevcut durum]
- **Sapma Oranı:** % [Tahmini] - [Bulgular]

### 📦 Önerilen İleri Analiz Modülleri
*   `[Modül 1]`: [Neden önerildi?]
*   `[Modül 2]`: [Neden önerildi?]
```
