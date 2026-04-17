# Modül Kodlama Sistemi - Hızlı Prompt Olu�?turma

**Amaç**: Karma�?ık modül kombinasyonlarını kısa kodlarla ifade ederek prompt olu�?turmayı kolayla�?tırmak.

---

## �??� Nasıl Kullanılır?

**Basit Yöntem**: Kodları birle�?tirerek istedi�?iniz analizi talep edin.

```markdown
# �?rnek 1: Security + Performance
"SEC+PERF kodlarıyla analiz yap"

# �?rnek 2: Full Frontend
"FE-FULL kodlarıyla analiz yap"

# �?rnek 3: �?zel Kombinasyon
"FS+SEC+PERF+API+DB kodlarıyla deep analysis yap"
```

---

## �??? Modül Kod Tablosu

### �??� P0 - Critical (Her Projede �?nerilir)

| Kod | Modül Adı | Dosya | Ne İnceler? | Token |
|-----|-----------|-------|-------------|-------|
| **PROJECT-INTEL** | Project Intelligence | project-intelligence.md | Meta-orchestrator, auto-analysis, module recommendation | ~5000 |
| **FS** | File Structure | file-structure-analysis.md | God files, circular deps, klasör yapısı | ~2000 |
| **SEC** | Security | security-analysis.md | OWASP Top 10, secrets, auth/authz | ~3500 |
| **PERF** | Performance | performance-analysis.md | Bundle size, N+1, lazy loading | ~2500 |

### �??� P1 - High Priority (�?o�?u Projede �?nerilir)

| Kod | Modül Adı | Dosya | Ne İnceler? | Token |
|-----|-----------|-------|-------------|-------|
| **API** | API Design | api-design-analysis.md | REST conventions, status codes | ~2000 |
| **DB** | Database | database-analysis.md | Queries, indexing, N+1 | ~1800 |
| **UI** | UI/UX | ui-ux-analysis.md | Design consistency, UX patterns | ~2500 |
| **DX** | Developer Experience | developer-experience.md | Build time, hot reload, setup | ~1800 |
| **TEST-GEN** | Test Generation | test-generation.md | BDD scenarios, Gherkin, executable tests | ~4000 |
| **UI-TEST** | UI Interaction Test | ui-interaction-test.md | Visual builders, Cypress, Playwright, canvas | ~4500 |
| **COLLAB-TEST** | Collaboration Test | collaboration-test.md | Real-time, WebSocket, multi-user sync | ~3500 |
| **ALGO-COMPLETE** | Algorithm Testing | ALGO-COMPLETE.md | Mathematical validation, property-based testing | ~8000 |

### �??� P2 - Medium Priority (Duruma Göre)

| Kod | Modül Adı | Dosya | Ne İnceler? | Token |
|-----|-----------|-------|-------------|-------|
| **TEST** | Testing | testing-strategy.md | Coverage, test quality | ~1500 |
| **A11Y** | Accessibility | accessibility-analysis.md | WCAG, keyboard nav, screen readers | ~1800 |
| **I18N** | Internationalization | i18n-analysis.md | Multi-language support | ~1200 |
| **MOBILE** | Mobile/Responsive | mobile-responsive.md | Responsive design | ~800 |
| **BROWSER** | Browser Compat | browser-compatibility.md | Cross-browser issues | ~600 |

### �??� P3 - Optional (İhtiyaçlara Göre)

| Kod | Modül Adı | Dosya | Ne İnceler? | Token |
|-----|-----------|-------|-------------|-------|
| **SEO** | SEO | seo-analysis.md | Meta tags, sitemap | ~800 |
| **ANALYTICS** | Analytics | analytics-analysis.md | Tracking, metrics | ~400 |
| **INFRA** | Infrastructure | infrastructure.md | Deployment, CI/CD | ~1500 |
| **MONITOR** | Monitoring | monitoring-observability.md | Logging, alerts | ~1000 |

### �??� Specialized (�?zel Durumlar)

| Kod | Modül Adı | Dosya | Ne İnceler? | Token |
|-----|-----------|-------|-------------|-------|
| **HG** | Hidden Gems | hidden-gems-deep-scan.md | Zombie code, bus factor, mı�? gibi | ~2500 |
| **AI** | AI Code Quality | ai-assisted-dev-analysis.md | AI-generated code issues | ~2000 |
| **FG** | Feature Gap | feature-gap-analysis.md | Missing features, competitors | ~1800 |
| **TR** | Turkish Market | turkish-market.md | KVKK, e-Devlet, taksit | ~1500 |

### �??�️ Tech Stack Specific

| Kod | Modül Adı | Dosya | Ne İnceler? | Token |
|-----|-----------|-------|-------------|-------|
| **REACT** | React/TypeScript | react-typescript.md | React patterns, hooks | ~600 |
| **DOTNET** | .NET Core | dotnet-core.md | .NET best practices | ~400 |
| **STATE** | State Management | state-management.md | Redux, Context, Zustand | ~800 |
| **REFACTOR** | Refactoring | refactoring-guide.md | Code smells, patterns | ~600 |

---

## �??� Preset Kombinasyonlar (Hazır Paketler)

Sık kullanılan kombinasyonlar için kısa kodlar:

| Kod | Modüller | Açıklama | Total Token |
|-----|----------|----------|-------------|
| **BASIC** | FS+SEC+PERF | Temel analiz paketi | ~8000 |
| **FE-FULL** | FS+PERF+UI+A11Y+MOBILE+REACT | Full frontend paketi | ~9700 |
| **BE-FULL** | FS+SEC+API+DB+DOTNET | Full backend paketi | ~9700 |
| **FULLSTACK** | FS+SEC+PERF+API+DB+UI+DX | Full-stack projeler | ~14600 |
| **TEST-FULL** | TEST-GEN+UI-TEST+COLLAB-TEST+TEST | Complete testing suite | ~13500 |
| **QUALITY** | TEST-GEN+AI+HG+REFACTOR | Code quality + testing | ~10500 |
| **UI-COMPLETE** | UI-TEST+A11Y+MOBILE+BROWSER+UI | Complete UI testing | ~10900 |
| **ALGO-SUITE** | ALGO-COMPLETE+TEST-GEN+PERF | Algorithm validation suite | ~14500 |
| **AUDIT** | Tüm P0+P1+P2 | Comprehensive audit | ~23000 |
| **QUICK** | FS+SEC | Hızlı scan (15 dk) | ~5500 |
| **DEEP** | AUDIT+HG+AI | En derin analiz | ~27500 |
| **TR-ECOM** | FULLSTACK+TR+FG | Türk e-ticaret | ~17900 |
| **AI-FOCUS** | FS+SEC+PERF+HG+AI | AI-generated code focus | ~12500 |

---

## �??� Kullanım �?rnekleri

### �?rnek 1: Basit Güvenlik Taraması

```markdown
"SEC koduyla security analizi yap"
```

**Sistem Yorumu**: `security-analysis.md` modülünü yükler, OWASP Top 10 kontrolü yapar.

---

### �?rnek 2: Frontend Performance Paketi

```markdown
"FE-FULL koduyla frontend analizi yap"
```

**Yüklenen Modüller**:
- file-structure-analysis.md
- performance-analysis.md
- ui-ux-analysis.md
- accessibility-analysis.md
- mobile-responsive.md
- react-typescript.md

---

### �?rnek 3: �?zel Kombinasyon

```markdown
"FS+SEC+API+DB+TR kodlarıyla Türk pazarı için backend analizi yap.
Mode 2, aksiyon planı olu�?tur."
```

**Yüklenen Modüller**:
- file-structure-analysis.md
- security-analysis.md
- api-design-analysis.md
- database-analysis.md
- turkish-market.md

**�?ıktı**: Mode 2 (Analyze + Plan) ile sprint breakdown

---

### �?rnek 4: Full Audit

```markdown
"AUDIT koduyla projeyi comprehensive audit et.
Türkçe rapor, P0-P1-P2-P3 sıralı."
```

**Yüklenen**: Tüm P0, P1, P2 modülleri (~23K token)

---

### �?rnek 5: AI-Generated Code Focus

```markdown
"AI-FOCUS koduyla AI'nın yazdı�?ı kodları incele.
'Mı�? gibi' pattern'leri, hallucination'ları tespit et."
```

---

### �?rnek 6: Quick Win Hunting

```markdown
"QUICK koduyla 15 dakikada quick wins bul.
Mode 2, task breakdown yap."
```

---

## �??? Mode Kombinasyonları

Kodları mode'larla birle�?tirin:

```markdown
# Mode 1: Sadece Analiz
"SEC+PERF koduyla Mode 1 analizi - sadece rapor"

# Mode 2: Analiz + Plan
"FE-FULL koduyla Mode 2 - aksiyon planı olu�?tur"

# Mode 3: Auto-Fix
"BASIC koduyla Mode 3 - P0 sorunları otomatik düzelt"
```

---

## �??� İleri Seviye Kullanım

### Birden Fazla Preset Birle�?tirme

```markdown
"FE-FULL+TR koduyla Türk pazarı için frontend analizi"
```

**Yüklenen**: Frontend Full + Turkish Market

---

### Modül �?ıkarma (Exclusion)

```markdown
"FULLSTACK -TEST koduyla analiz (testing hariç)"
```

**Yüklenen**: Full-stack modülleri, testing-strategy hariç

---

### Sadece Belirli �?ncelikler

```markdown
"P0-ONLY koduyla sadece kritik sorunlar"
"P0+P1 koduyla yüksek öncelikli analiz"
```

---

## �??? Modül Kombinasyon Stratejileri

### Küçük Proje (< 10K LOC)

```markdown
�?nerilen: BASIC veya QUICK
Token: ~5500-8000
Süre: 15-30 dakika
```

### Orta Proje (10K-50K LOC)

```markdown
�?nerilen: FE-FULL veya BE-FULL veya FULLSTACK
Token: ~9700-14600
Süre: 45-90 dakika
```

### Büyük Proje (> 50K LOC)

```markdown
�?nerilen: Bölümlere ayır
Sprint 1: QUICK (P0 bulguları)
Sprint 2: FE-FULL veya BE-FULL
Sprint 3: AUDIT (comprehensive)
```

---

## �??? Hızlı Ba�?vuru Kartları

### Security Odaklı

```markdown
"SEC+API+DB koduyla security-first analiz"
```

### Performance Odaklı

```markdown
"PERF+DX+INFRA koduyla performance optimization"
```

### Quality Odaklı

```markdown
"FS+TEST+REFACTOR+AI koduyla code quality analizi"
```

### Business Odaklı

```markdown
"FG+TR+SEO koduyla market fit analizi"
```

---

## �??� Token Bütçesi Yönetimi

| Durum | �?nerilen Kod | Token | Süre |
|-------|--------------|-------|------|
| Hızlı scan | QUICK | ~5500 | 15 dk |
| Standart analiz | BASIC | ~8000 | 30 dk |
| Orta derinlik | FE-FULL veya BE-FULL | ~10000 | 60 dk |
| Full audit | FULLSTACK | ~14600 | 90 dk |
| Maximum | AUDIT | ~23000 | 120 dk |
| Derin kazı | DEEP | ~27500 | 150+ dk |

---

## �?�️ Dikkat Edilmesi Gerekenler

1. **Token Limiti**: Claude'un context window'u ~200K. DEEP bile sorun de�?il.
2. **Zaman**: AUDIT ve DEEP 2+ saat sürebilir.
3. **Alakasız Modüller**: Frontend projesinde DOTNET yüklemeyin.
4. **�?ncelik**: P0 > P1 > P2 > P3 sırasıyla yükleyin.

---

## �??? Ek Kaynaklar

- **Detaylı Kullanım**: USAGE_GUIDE.md
- **Mode Açıklamaları**: MODE_TRANSITIONS.md
- **Türkçe Prompt �?rnekleri**: TURKISH_PROMPTS.md
- **Effective Prompts**: USAGE_GUIDE.md

---

## �??? �?rnek Workflow

### Senaryo: Yeni bir e-ticaret projesi analiz ediyorsunuz

**Adım 1: Quick Scan**
```markdown
"QUICK koduyla hızlı scan yap"
�?? 15 dakika, kritik sorunlar
```

**Adım 2: Full Analysis**
```markdown
"TR-ECOM koduyla full analiz"
�?? 90 dakika, comprehensive
```

**Adım 3: Specific Deep Dive**
```markdown
"SEC+PERF koduyla P0 sorunlara deep dive"
�?? 45 dakika, specific
```

**Adım 4: Auto-Fix**
```markdown
"BASIC koduyla Mode 3 - P0 düzelt"
�?? Otomatik düzeltme
```

---

**Modül Kodlama Sistemi ile analiz artık çok kolay!** �???

**Not**: Sistemin otomatik modül seçimi de var ama manuel kod kullanımı %100 kontrol sa�?lar.

---

*Olu�?turulma: Aralık 2024*
*Versiyon: 1.0*
