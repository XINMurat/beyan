# ModÃ¼l Kodlama Sistemi - HÄ±zlÄ± Prompt OluÅŸturma

**AmaÃ§**: KarmaÅŸÄ±k modÃ¼l kombinasyonlarÄ±nÄ± kÄ±sa kodlarla ifade ederek prompt oluÅŸturmayÄ± kolaylaÅŸtÄ±rmak.

---

## ðŸŽ¯ NasÄ±l KullanÄ±lÄ±r?

**Basit YÃ¶ntem**: KodlarÄ± birleÅŸtirerek istediÄŸiniz analizi talep edin.

```markdown
# Ã–rnek 1: Security + Performance
"SEC+PERF kodlarÄ±yla analiz yap"

# Ã–rnek 2: Full Frontend
"FE-FULL kodlarÄ±yla analiz yap"

# Ã–rnek 3: Ã–zel Kombinasyon
"FS+SEC+PERF+API+DB kodlarÄ±yla deep analysis yap"
```

---

## ðŸ“Š ModÃ¼l Kod Tablosu

### ðŸ”´ P0 - Critical (Her Projede Ã–nerilir)

| Kod | ModÃ¼l AdÄ± | Dosya | Ne Ä°nceler? | Token |
|-----|-----------|-------|-------------|-------|
| **PROJECT-INTEL** | Project Intelligence | project-intelligence.md | Meta-orchestrator, auto-analysis, module recommendation | ~5000 |
| **FS** | File Structure | file-structure-analysis.md | God files, circular deps, klasÃ¶r yapÄ±sÄ± | ~2000 |
| **SEC** | Security | security-analysis.md | OWASP Top 10, secrets, auth/authz | ~3500 |
| **PERF** | Performance | performance-analysis.md | Bundle size, N+1, lazy loading | ~2500 |

### ðŸŸ  P1 - High Priority (Ã‡oÄŸu Projede Ã–nerilir)

| Kod | ModÃ¼l AdÄ± | Dosya | Ne Ä°nceler? | Token |
|-----|-----------|-------|-------------|-------|
| **API** | API Design | api-design-analysis.md | REST conventions, status codes | ~2000 |
| **DB** | Database | database-analysis.md | Queries, indexing, N+1 | ~1800 |
| **UI** | UI/UX | ui-ux-analysis.md | Design consistency, UX patterns | ~2500 |
| **DX** | Developer Experience | developer-experience.md | Build time, hot reload, setup | ~1800 |
| **TEST-GEN** | Test Generation | test-generation.md | BDD scenarios, Gherkin, executable tests | ~4000 |
| **UI-TEST** | UI Interaction Test | ui-interaction-test.md | Visual builders, Cypress, Playwright, canvas | ~4500 |
| **COLLAB-TEST** | Collaboration Test | collaboration-test.md | Real-time, WebSocket, multi-user sync | ~3500 |
| **ALGO-COMPLETE** | Algorithm Testing | ALGO-COMPLETE.md | Mathematical validation, property-based testing | ~8000 |

### ðŸŸ¡ P2 - Medium Priority (Duruma GÃ¶re)

| Kod | ModÃ¼l AdÄ± | Dosya | Ne Ä°nceler? | Token |
|-----|-----------|-------|-------------|-------|
| **TEST** | Testing | testing-strategy.md | Coverage, test quality | ~1500 |
| **A11Y** | Accessibility | accessibility-analysis.md | WCAG, keyboard nav, screen readers | ~1800 |
| **I18N** | Internationalization | i18n-analysis.md | Multi-language support | ~1200 |
| **MOBILE** | Mobile/Responsive | mobile-responsive.md | Responsive design | ~800 |
| **BROWSER** | Browser Compat | browser-compatibility.md | Cross-browser issues | ~600 |

### ðŸŸ¢ P3 - Optional (Ä°htiyaÃ§lara GÃ¶re)

| Kod | ModÃ¼l AdÄ± | Dosya | Ne Ä°nceler? | Token |
|-----|-----------|-------|-------------|-------|
| **SEO** | SEO | seo-analysis.md | Meta tags, sitemap | ~800 |
| **ANALYTICS** | Analytics | analytics-analysis.md | Tracking, metrics | ~400 |
| **INFRA** | Infrastructure | infrastructure.md | Deployment, CI/CD | ~1500 |
| **MONITOR** | Monitoring | monitoring-observability.md | Logging, alerts | ~1000 |

### ðŸŽ¨ Specialized (Ã–zel Durumlar)

| Kod | ModÃ¼l AdÄ± | Dosya | Ne Ä°nceler? | Token |
|-----|-----------|-------|-------------|-------|
| **HG** | Hidden Gems | hidden-gems-deep-scan.md | Zombie code, bus factor, mÄ±ÅŸ gibi | ~2500 |
| **AI** | AI Code Quality | ai-assisted-dev-analysis.md | AI-generated code issues | ~2000 |
| **FG** | Feature Gap | feature-gap-analysis.md | Missing features, competitors | ~1800 |
| **TR** | Turkish Market | turkish-market.md | KVKK, e-Devlet, taksit | ~1500 |

### ðŸ› ï¸ Tech Stack Specific

| Kod | ModÃ¼l AdÄ± | Dosya | Ne Ä°nceler? | Token |
|-----|-----------|-------|-------------|-------|
| **REACT** | React/TypeScript | react-typescript.md | React patterns, hooks | ~600 |
| **DOTNET** | .NET Core | dotnet-core.md | .NET best practices | ~400 |
| **STATE** | State Management | state-management.md | Redux, Context, Zustand | ~800 |
| **REFACTOR** | Refactoring | refactoring-guide.md | Code smells, patterns | ~600 |

---

## ðŸŽ­ Preset Kombinasyonlar (HazÄ±r Paketler)

SÄ±k kullanÄ±lan kombinasyonlar iÃ§in kÄ±sa kodlar:

| Kod | ModÃ¼ller | AÃ§Ä±klama | Total Token |
|-----|----------|----------|-------------|
| **BASIC** | FS+SEC+PERF | Temel analiz paketi | ~8000 |
| **FE-FULL** | FS+PERF+UI+A11Y+MOBILE+REACT | Full frontend paketi | ~9700 |
| **BE-FULL** | FS+SEC+API+DB+DOTNET | Full backend paketi | ~9700 |
| **FULLSTACK** | FS+SEC+PERF+API+DB+UI+DX | Full-stack projeler | ~14600 |
| **TEST-FULL** | TEST-GEN+UI-TEST+COLLAB-TEST+TEST | Complete testing suite | ~13500 |
| **QUALITY** | TEST-GEN+AI+HG+REFACTOR | Code quality + testing | ~10500 |
| **UI-COMPLETE** | UI-TEST+A11Y+MOBILE+BROWSER+UI | Complete UI testing | ~10900 |
| **ALGO-SUITE** | ALGO-COMPLETE+TEST-GEN+PERF | Algorithm validation suite | ~14500 |
| **AUDIT** | TÃ¼m P0+P1+P2 | Comprehensive audit | ~23000 |
| **QUICK** | FS+SEC | HÄ±zlÄ± scan (15 dk) | ~5500 |
| **DEEP** | AUDIT+HG+AI | En derin analiz | ~27500 |
| **TR-ECOM** | FULLSTACK+TR+FG | TÃ¼rk e-ticaret | ~17900 |
| **AI-FOCUS** | FS+SEC+PERF+HG+AI | AI-generated code focus | ~12500 |

---

## ðŸ“ KullanÄ±m Ã–rnekleri

### Ã–rnek 1: Basit GÃ¼venlik TaramasÄ±

```markdown
"SEC koduyla security analizi yap"
```

**Sistem Yorumu**: `security-analysis.md` modÃ¼lÃ¼nÃ¼ yÃ¼kler, OWASP Top 10 kontrolÃ¼ yapar.

---

### Ã–rnek 2: Frontend Performance Paketi

```markdown
"FE-FULL koduyla frontend analizi yap"
```

**YÃ¼klenen ModÃ¼ller**:
- file-structure-analysis.md
- performance-analysis.md
- ui-ux-analysis.md
- accessibility-analysis.md
- mobile-responsive.md
- react-typescript.md

---

### Ã–rnek 3: Ã–zel Kombinasyon

```markdown
"FS+SEC+API+DB+TR kodlarÄ±yla TÃ¼rk pazarÄ± iÃ§in backend analizi yap.
Mode 2, aksiyon planÄ± oluÅŸtur."
```

**YÃ¼klenen ModÃ¼ller**:
- file-structure-analysis.md
- security-analysis.md
- api-design-analysis.md
- database-analysis.md
- turkish-market.md

**Ã‡Ä±ktÄ±**: Mode 2 (Analyze + Plan) ile sprint breakdown

---

### Ã–rnek 4: Full Audit

```markdown
"AUDIT koduyla projeyi comprehensive audit et.
TÃ¼rkÃ§e rapor, P0-P1-P2-P3 sÄ±ralÄ±."
```

**YÃ¼klenen**: TÃ¼m P0, P1, P2 modÃ¼lleri (~23K token)

---

### Ã–rnek 5: AI-Generated Code Focus

```markdown
"AI-FOCUS koduyla AI'nÄ±n yazdÄ±ÄŸÄ± kodlarÄ± incele.
'MÄ±ÅŸ gibi' pattern'leri, hallucination'larÄ± tespit et."
```

---

### Ã–rnek 6: Quick Win Hunting

```markdown
"QUICK koduyla 15 dakikada quick wins bul.
Mode 2, task breakdown yap."
```

---

## ðŸ”„ Mode KombinasyonlarÄ±

KodlarÄ± mode'larla birleÅŸtirin:

```markdown
# Mode 1: Sadece Analiz
"SEC+PERF koduyla Mode 1 analizi - sadece rapor"

# Mode 2: Analiz + Plan
"FE-FULL koduyla Mode 2 - aksiyon planÄ± oluÅŸtur"

# Mode 3: Auto-Fix
"BASIC koduyla Mode 3 - P0 sorunlarÄ± otomatik dÃ¼zelt"
```

---

## ðŸŽ¯ Ä°leri Seviye KullanÄ±m

### Birden Fazla Preset BirleÅŸtirme

```markdown
"FE-FULL+TR koduyla TÃ¼rk pazarÄ± iÃ§in frontend analizi"
```

**YÃ¼klenen**: Frontend Full + Turkish Market

---

### ModÃ¼l Ã‡Ä±karma (Exclusion)

```markdown
"FULLSTACK -TEST koduyla analiz (testing hariÃ§)"
```

**YÃ¼klenen**: Full-stack modÃ¼lleri, testing-strategy hariÃ§

---

### Sadece Belirli Ã–ncelikler

```markdown
"P0-ONLY koduyla sadece kritik sorunlar"
"P0+P1 koduyla yÃ¼ksek Ã¶ncelikli analiz"
```

---

## ðŸ“‹ ModÃ¼l Kombinasyon Stratejileri

### KÃ¼Ã§Ã¼k Proje (< 10K LOC)

```markdown
Ã–nerilen: BASIC veya QUICK
Token: ~5500-8000
SÃ¼re: 15-30 dakika
```

### Orta Proje (10K-50K LOC)

```markdown
Ã–nerilen: FE-FULL veya BE-FULL veya FULLSTACK
Token: ~9700-14600
SÃ¼re: 45-90 dakika
```

### BÃ¼yÃ¼k Proje (> 50K LOC)

```markdown
Ã–nerilen: BÃ¶lÃ¼mlere ayÄ±r
Sprint 1: QUICK (P0 bulgularÄ±)
Sprint 2: FE-FULL veya BE-FULL
Sprint 3: AUDIT (comprehensive)
```

---

## ðŸš€ HÄ±zlÄ± BaÅŸvuru KartlarÄ±

### Security OdaklÄ±

```markdown
"SEC+API+DB koduyla security-first analiz"
```

### Performance OdaklÄ±

```markdown
"PERF+DX+INFRA koduyla performance optimization"
```

### Quality OdaklÄ±

```markdown
"FS+TEST+REFACTOR+AI koduyla code quality analizi"
```

### Business OdaklÄ±

```markdown
"FG+TR+SEO koduyla market fit analizi"
```

---

## ðŸ”§ Token BÃ¼tÃ§esi YÃ¶netimi

| Durum | Ã–nerilen Kod | Token | SÃ¼re |
|-------|--------------|-------|------|
| HÄ±zlÄ± scan | QUICK | ~5500 | 15 dk |
| Standart analiz | BASIC | ~8000 | 30 dk |
| Orta derinlik | FE-FULL veya BE-FULL | ~10000 | 60 dk |
| Full audit | FULLSTACK | ~14600 | 90 dk |
| Maximum | AUDIT | ~23000 | 120 dk |
| Derin kazÄ± | DEEP | ~27500 | 150+ dk |

---

## âš ï¸ Dikkat Edilmesi Gerekenler

1. **Token Limiti**: Claude'un context window'u ~200K. DEEP bile sorun deÄŸil.
2. **Zaman**: AUDIT ve DEEP 2+ saat sÃ¼rebilir.
3. **AlakasÄ±z ModÃ¼ller**: Frontend projesinde DOTNET yÃ¼klemeyin.
4. **Ã–ncelik**: P0 > P1 > P2 > P3 sÄ±rasÄ±yla yÃ¼kleyin.

---

## ðŸ“š Ek Kaynaklar

- **DetaylÄ± KullanÄ±m**: USAGE_GUIDE.md
- **Mode AÃ§Ä±klamalarÄ±**: MODE_TRANSITIONS.md
- **TÃ¼rkÃ§e Prompt Ã–rnekleri**: TURKISH_PROMPTS.md
- **Effective Prompts**: EFFECTIVE_PROMPTS.md

---

## ðŸŽ“ Ã–rnek Workflow

### Senaryo: Yeni bir e-ticaret projesi analiz ediyorsunuz

**AdÄ±m 1: Quick Scan**
```markdown
"QUICK koduyla hÄ±zlÄ± scan yap"
â†’ 15 dakika, kritik sorunlar
```

**AdÄ±m 2: Full Analysis**
```markdown
"TR-ECOM koduyla full analiz"
â†’ 90 dakika, comprehensive
```

**AdÄ±m 3: Specific Deep Dive**
```markdown
"SEC+PERF koduyla P0 sorunlara deep dive"
â†’ 45 dakika, specific
```

**AdÄ±m 4: Auto-Fix**
```markdown
"BASIC koduyla Mode 3 - P0 dÃ¼zelt"
â†’ Otomatik dÃ¼zeltme
```

---

**ModÃ¼l Kodlama Sistemi ile analiz artÄ±k Ã§ok kolay!** ðŸš€

**Not**: Sistemin otomatik modÃ¼l seÃ§imi de var ama manuel kod kullanÄ±mÄ± %100 kontrol saÄŸlar.

---

*OluÅŸturulma: AralÄ±k 2024*
*Versiyon: 1.0*
