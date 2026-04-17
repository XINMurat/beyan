# KapsamlÃ„Â± Prompt Rehberi - v4.0 (BirleÃ…Å¸tirilmiÃ…Å¸)

**EFFECTIVE_PROMPTS.md + TURKISH_PROMPTS.md Ã¢â€ â€™ Tek Dosyada**

**AmaÃƒÂ§**: Sistemin tÃƒÂ¼m ÃƒÂ¶zelliklerini kullanarak en etkili prompt'larÃ„Â± yazmak iÃƒÂ§in kapsamlÃ„Â± rehber.

---

## Ã°Å¸â€œâ€˜ Ã„Â°ÃƒÂ§indekiler

1. [ModÃƒÂ¼l Kodlama Sistemi](#modÃƒÂ¼l-kodlama-sistemi)
2. [Mode SeÃƒÂ§imi](#mode-seÃƒÂ§imi)
3. [TÃƒÂ¼rkÃƒÂ§e Prompt Ãƒâ€“rnekleri](#tÃƒÂ¼rkÃƒÂ§e-prompt-ÃƒÂ¶rnekleri)
4. [KapsamlÃ„Â± Analiz Stratejileri](#kapsamlÃ„Â±-analiz-stratejileri)
5. [Vizyon KaymasÃ„Â± Analizi](#vizyon-kaymasÃ„Â±-analizi)
6. [Proje Tipine GÃƒÂ¶re Ãƒâ€“rnekler](#proje-tipine-gÃƒÂ¶re-ÃƒÂ¶rnekler)
7. [Ã„Â°leri Seviye Kombinasyonlar](#iÃŒâ€¡leri-seviye-kombinasyonlar)

---

## Ã°Å¸Å½Â¯ ModÃƒÂ¼l Kodlama Sistemi

**Yeni Ãƒâ€“zellik!** ModÃƒÂ¼lleri kÃ„Â±sa kodlarla belirtin.

```markdown
# Temel KullanÃ„Â±m
"SEC+PERF koduyla analiz yap"
"FE-FULL koduyla frontend analizi"
"AUDIT koduyla comprehensive audit"
```

**DetaylÃ„Â± bilgi iÃƒÂ§in**: `MODULE_CODES.md` dosyasÃ„Â±na bakÃ„Â±n.

### HÃ„Â±zlÃ„Â± Referans

| Kod | ModÃƒÂ¼l | Kod | ModÃƒÂ¼l |
|-----|-------|-----|-------|
| **FS** | File Structure | **SEC** | Security |
| **PERF** | Performance | **API** | API Design |
| **DB** | Database | **UI** | UI/UX |
| **DX** | Dev Experience | **TEST** | Testing |
| **A11Y** | Accessibility | **HG** | Hidden Gems |
| **AI** | AI Code Quality | **FG** | Feature Gap |
| **TR** | Turkish Market | **REACT** | React/TS |

**Preset Paketler**:
- **BASIC** = FS+SEC+PERF
- **FE-FULL** = FS+PERF+UI+A11Y+MOBILE+REACT
- **BE-FULL** = FS+SEC+API+DB+DOTNET
- **FULLSTACK** = FS+SEC+PERF+API+DB+UI+DX
- **AUDIT** = TÃƒÂ¼m P0+P1+P2 modÃƒÂ¼ller
- **TR-ECOM** = FULLSTACK+TR+FG

---

## Ã°Å¸Å½Å¡Ã¯Â¸Â Mode SeÃƒÂ§imi (HÃ„Â±zlÃ„Â± BaÃ…Å¸vuru)

| Ne Ã„Â°stiyorsun? | Hangi Mode? | Ãƒâ€“rnek Prompt |
|----------------|-------------|--------------|
| Sadece rapor | **Mode 1** | "Projeyi analiz et" |
| Rapor + Plan | **Mode 2** | "Aksiyon planÃ„Â± oluÃ…Å¸tur" |
| Otomatik fix | **Mode 3** | "P0 sorunlarÃ„Â± dÃƒÂ¼zelt" |

### Mode 1: Analyze Only (Sadece Analiz)

```markdown
"Projeyi analiz et"
"SEC+PERF koduyla security ve performance analizi"
"Mevcut durumu deÃ„Å¸erlendir, hiÃƒÂ§bir deÃ„Å¸iÃ…Å¸iklik yapma"
```

### Mode 2: Analyze + Plan

```markdown
"Aksiyon planÃ„Â± oluÃ…Å¸tur"
"FULLSTACK koduyla analiz yap ve 3 sprint'lik plan hazÃ„Â±rla"
"P0 sorunlarÃ„Â± iÃƒÂ§in implementation roadmap ÃƒÂ§Ã„Â±kar"
```

### Mode 3: Full Flow (Semi-Autonomous)

```markdown
"P0 sorunlarÃ„Â± dÃƒÂ¼zelt"
"BASIC koduyla Mode 3 - kritik sorunlarÃ„Â± otomatik ÃƒÂ§ÃƒÂ¶z"
"Security vulnerabilities'i fix et, ama her checkpoint'te sor"
```

---

## Ã°Å¸â€¡Â¹Ã°Å¸â€¡Â· TÃƒÂ¼rkÃƒÂ§e Prompt Ãƒâ€“rnekleri (100+)

### 1Ã¯Â¸ÂÃ¢Æ’Â£ Mode 1: Sadece Analiz

#### Genel Analiz

```markdown
"Projeyi analiz et"
"Proje saÃ„Å¸lÃ„Â±k raporu ver"
"Mevcut durumu deÃ„Å¸erlendir"
"HÃ„Â±zlÃ„Â± bir scan yap"
"Deep analysis yap"
"AUDIT koduyla comprehensive audit ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±r"
```

#### Spesifik Alan Analizi

```markdown
"SEC koduyla security audit yap"
"PERF koduyla performans analizi ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±r"
"DB koduyla database sorunlarÃ„Â±nÃ„Â± tespit et"
"UI koduyla UI/UX analizi yap"
"A11Y koduyla eriÃ…Å¸ilebilirlik kontrolÃƒÂ¼ yap"
"API koduyla API design review yap"
"HG koduyla hidden gem'leri bul"
"Technical debt hesapla"
"Code quality metrics ver"
```

#### TÃƒÂ¼rk PiyasasÃ„Â± OdaklÃ„Â±

```markdown
"TR koduyla KVKK uyumluluÃ„Å¸unu kontrol et"
"TR-ECOM koduyla TÃƒÂ¼rk e-ticaret piyasasÃ„Â± analizi"
"e-Devlet entegrasyonunu incele"
"Taksit sistemini deÃ„Å¸erlendir"
"TÃƒÂ¼rkÃƒÂ§e desteÃ„Å¸ini kontrol et"
```

#### AI-Generated Code Analizi

```markdown
"AI koduyla AI'nÃ„Â±n yazdÃ„Â±Ã„Å¸Ã„Â± kodu incele"
"HG+AI koduyla 'mÃ„Â±Ã…Å¸ gibi' pattern'leri bul"
"AI hallucination'larÃ„Â±nÃ„Â± tespit et"
"ChatGPT code smell'lerini ara"
```

#### Ãƒâ€“ncelik BazlÃ„Â±

```markdown
"Sadece P0 sorunlarÃ„Â± gÃƒÂ¶ster"
"Kritik ve yÃƒÂ¼ksek ÃƒÂ¶ncelikli sorunlar"
"Quick win'leri bul"
"En kolay dÃƒÂ¼zeltilebilir sorunlar"
"En kritik 5 sorunu gÃƒÂ¶ster"
```

---

### 2Ã¯Â¸ÂÃ¢Æ’Â£ Mode 2: Analyze + Plan

#### Aksiyon PlanÃ„Â±

```markdown
"Projeyi analiz et ve aksiyon planÃ„Â± oluÃ…Å¸tur"
"FULLSTACK koduyla aksiyon planÃ„Â± hazÃ„Â±rla"
"Sprint planning yap"
"Task breakdown oluÃ…Å¸tur"
"Implementation plan hazÃ„Â±rla"
"Execution roadmap ÃƒÂ§Ã„Â±kar"
```

#### Sprint Planning

```markdown
"Bu hafta iÃƒÂ§in sprint planÃ„Â±"
"2 haftalÃ„Â±k sprint oluÃ…Å¸tur"
"Sprint 1 iÃƒÂ§in task'leri belirle"
"Bu sprint'te ne yapmalÃ„Â±yÃ„Â±z?"
"Ãƒâ€“ncelikli task'leri sÃ„Â±rala"
```

#### Roadmap

```markdown
"3 aylÃ„Â±k roadmap hazÃ„Â±rla"
"Q1 iÃƒÂ§in plan oluÃ…Å¸tur"
"6 aylÃ„Â±k teknik strateji"
"YÃ„Â±llÃ„Â±k iyileÃ…Å¸tirme planÃ„Â±"
"Milestone'larÃ„Â± belirle"
```

#### Epic & Story Breakdown

```markdown
"Epic'lere ayÃ„Â±r"
"Story breakdown yap"
"Task hierarchy oluÃ…Å¸tur"
"Epic Ã¢â€ â€™ Story Ã¢â€ â€™ Task dÃƒÂ¶nÃƒÂ¼Ã…Å¸ÃƒÂ¼mÃƒÂ¼"
"Backlog organization yap"
```

#### Effort Estimation

```markdown
"Toplam ÃƒÂ§aba tahmini ver"
"Her task iÃƒÂ§in sÃƒÂ¼re belirle"
"Sprint capacity planning"
"Resource allocation ÃƒÂ¶ner"
"Team assignment planÃ„Â±"
```

---

### 3Ã¯Â¸ÂÃ¢Æ’Â£ Mode 3: Full Flow (Semi-Autonomous)

**Ã¢Å¡Â Ã¯Â¸Â DÃ„Â°KKAT**: Kod yazar ve dosya deÃ„Å¸iÃ…Å¸tirir!

#### Genel Auto-Fix

```markdown
"P0 sorunlarÃ„Â± dÃƒÂ¼zelt"
"Kritik sorunlarÃ„Â± otomatik ÃƒÂ§ÃƒÂ¶z"
"SEC koduyla security vulnerabilities'i fix et"
"PERF koduyla performans sorunlarÃ„Â±nÃ„Â± dÃƒÂ¼zelt"
"TÃƒÂ¼m otomatik dÃƒÂ¼zeltilebilir sorunlarÃ„Â± ÃƒÂ§ÃƒÂ¶z"
```

#### Checkpoint Control

```markdown
"P0 dÃƒÂ¼zelt, ama checkpoint'lerde sor"
"Full autonomous mode, ama onayÃ„Â±mÃ„Â± al"
"Otomatik dÃƒÂ¼zelt, ÃƒÂ¶nemli noktalarda dur"
"Her adÃ„Â±mda bana sor"
```

#### Spesifik Sorun Fix

```markdown
"SQL injection'larÃ„Â± dÃƒÂ¼zelt"
"TÃƒÂ¼m exposed secrets'Ã„Â± temizle"
"Missing authorization'larÃ„Â± ekle"
"N+1 query'leri optimize et"
"Bundle size'Ã„Â± kÃƒÂ¼ÃƒÂ§ÃƒÂ¼lt"
"Build sÃƒÂ¼resini optimize et"
```

#### Scope Limited

```markdown
"Sadece OrderService.cs'i dÃƒÂ¼zelt"
"Backend security sorunlarÃ„Â±nÃ„Â± ÃƒÂ§ÃƒÂ¶z"
"Frontend performance'Ã„Â± optimize et"
"Sadece bu klasÃƒÂ¶rde ÃƒÂ§alÃ„Â±Ã…Å¸: src/services/"
```

#### Batch Operations

```markdown
"TÃƒÂ¼m P0 ve P1 sorunlarÃ„Â± dÃƒÂ¼zelt"
"SEC+PERF koduyla gÃƒÂ¼venlik ve performans sorunlarÃ„Â±nÃ„Â± ÃƒÂ§ÃƒÂ¶z"
"Frontend ve backend sorunlarÃ„Â±nÃ„Â± birlikte fix et"
```

#### Test-Only Mode

```markdown
"Kod yaz ve test et, ama commit etme"
"Fix'leri hazÃ„Â±rla, ben commit edeceÃ„Å¸im"
"DeÃ„Å¸iÃ…Å¸iklikleri stage'le ama push'lama"
```

#### Dry-Run Mode

```markdown
"Ne yapacaÃ„Å¸Ã„Â±nÃ„Â± gÃƒÂ¶ster ama deÃ„Å¸iÃ…Å¸iklik yapma"
"Simulation mode'da ÃƒÂ§alÃ„Â±Ã…Å¸"
"Kod yaz ama dosyalara dokunma"
"Preview mode"
```

---

## Ã°Å¸â€œÅ  KapsamlÃ„Â± Analiz Stratejileri

### Strateji 1: TÃƒÂ¼m ModÃƒÂ¼lleri Zorla YÃƒÂ¼klet

```markdown
"Projeyi TÃƒÅ“M modÃƒÂ¼llerle kapsamlÃ„Â± analiz et. 
AUDIT koduyla P0, P1, P2, P3 ve SPECIALIZED modÃƒÂ¼llerin hepsini yÃƒÂ¼kle. 
Her alanÃ„Â± kontrol et:
- Dosya yapÃ„Â±sÃ„Â± (FS)
- Performans (PERF)
- UI/UX (UI)
- GÃƒÂ¼venlik (SEC) - OWASP Top 10
- API tasarÃ„Â±mÃ„Â± (API)
- VeritabanÃ„Â± (DB)
- EriÃ…Å¸ilebilirlik (A11Y)
- Test stratejisi (TEST)
- Hidden gems (HG)
- AI-ÃƒÂ¼retilmiÃ…Å¸ kod kalitesi (AI)

Deep analysis yap, hiÃƒÂ§bir Ã…Å¸eyi atlama."
```

---

### Strateji 2: Kategorileri Tek Tek Belirt

```markdown
"Projeyi analiz et ve Ã…Å¸u alanlarÃ„Â± detaylÃ„Â± incele:
1. Ã°Å¸â€œÂ Dosya yapÃ„Â±sÃ„Â± (FS kodu: god files, circular deps)
2. Ã°Å¸â€â€™ Security (SEC kodu: SQL injection, secrets, auth)
3. Ã¢Å¡Â¡ Performance (PERF kodu: bundle size, N+1 queries, build time)
4. Ã°Å¸Å½Â¨ UI/UX (UI kodu: eriÃ…Å¸ilebilirlik, responsive)
5. Ã°Å¸â€Å’ API design (API kodu: REST conventions, error handling)
6. Ã°Å¸â€™Â¾ Database (DB kodu: queries, indexing)
7. Ã°Å¸Â§Âª Testing (TEST kodu: coverage, test quality)
8. Ã°Å¸Â§Å¸ Hidden gems (HG kodu: zombie code, unused features)
9. Ã°Å¸Â¤â€“ AI code quality (AI kodu: mÃ„Â±Ã…Å¸ gibi patterns)

Her kategori iÃƒÂ§in ayrÃ„Â± skor ver."
```

---

### Strateji 3: Full Audit Modu

```markdown
"AUDIT koduyla full audit ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±r. 
Maximum derinlikte analiz yap.
TÃƒÂ¼m P0, P1, P2 sorunlarÃ„Â±nÃ„Â± tespit et.

Her bulgu iÃƒÂ§in:
- Dosya yolu ve satÃ„Â±r numarasÃ„Â±
- Risk seviyesi
- Ãƒâ€¡ÃƒÂ¶zÃƒÂ¼m ÃƒÂ¶nerisi
- Tahmini sÃƒÂ¼re

HiÃƒÂ§bir alanÃ„Â± atlama, comprehensive olsun.
TÃƒÂ¼rkÃƒÂ§e rapor ver."
```

---

### Strateji 4: Spesifik Tech Stack

```markdown
"Bu bir React + TypeScript + .NET Core projesi.
FE-FULL+BE-FULL kodlarÃ„Â±yla analiz yap:

Frontend:
- REACT (React patterns, hooks)
- UI (UI/UX)
- PERF (Performance)
- A11Y (Accessibility)

Backend:
- DOTNET (.NET best practices)
- API (API design)
- DB (Database)
- SEC (Security)

Her modÃƒÂ¼l iÃƒÂ§in detaylÃ„Â± analiz yap."
```

---

### Strateji 5: En KapsamlÃ„Â± Tek Prompt (Ãƒâ€“nerilen)

```markdown
"Bu projeyi DEEP koduyla analiz et (FULL AUDIT + Hidden Gems + AI Quality).

YÃƒÅ“KLENECEK MODÃƒÅ“LLER (hepsi):
FS, PERF, UI, SEC, HG, API, DB, TEST, AI, DX, A11Y, I18N, TR, FG

HER MODÃƒÅ“L Ã„Â°Ãƒâ€¡Ã„Â°N:
1. Mevcut durumu skorla (0-10)
2. Kritik bulgularÃ„Â± listele (dosya yolu + satÃ„Â±r)
3. Kod ÃƒÂ¶rnekleri gÃƒÂ¶ster (mevcut vs ÃƒÂ¶nerilen)
4. Ãƒâ€¡ÃƒÂ¶zÃƒÂ¼m ÃƒÂ¶ner
5. Tahmini sÃƒÂ¼re ver

Ãƒâ€¡IKTI:
- TÃƒÂ¼rkÃƒÂ§e
- P0, P1, P2, P3 ÃƒÂ¶ncelik sÃ„Â±ralamasÃ„Â±
- Executive summary
- DetaylÃ„Â± bulgular
- Aksiyon planÃ„Â±
- Quick wins ayrÃ„Â± listele

HiÃƒÂ§bir alanÃ„Â± atlama, kapsamlÃ„Â± ol."
```

---

## Ã°Å¸â€Â Vizyon KaymasÃ„Â± (Vision Drift) Analizi

Projenin orijinal vizyonu ile mevcut implementasyon arasÃ„Â±ndaki tutarsÃ„Â±zlÃ„Â±klarÃ„Â± tespit etmek iÃƒÂ§in:

### 1. Temel Vizyon Analizi

```markdown
"HG koduyla projenin vizyon kaymasÃ„Â±nÃ„Â± (vision drift) analiz et.

KONTROL ET:
1. README ve dokÃƒÂ¼mantasyondaki vaatler vs gerÃƒÂ§ek implementasyon
2. BaÃ…Å¸langÃ„Â±ÃƒÂ§taki mimari kararlar vs mevcut durum
3. Planlanan ÃƒÂ¶zellikler vs implementasyon durumu
4. Eski dokÃƒÂ¼mantasyon vs yeni kod tutarsÃ„Â±zlÃ„Â±klarÃ„Â±

Ãƒâ€¡IKTI:
- Vizyon uyum skoru (0-10)
- TutarsÃ„Â±zlÃ„Â±klar listesi
- Kayma noktalarÃ„Â± (dosya + satÃ„Â±r)
- Ãƒâ€“neriler

TÃƒÂ¼rkÃƒÂ§e, detaylÃ„Â± rapor."
```

---

### 2. DetaylÃ„Â± Vizyon Hizalama Raporu

```markdown
"HG koduyla kapsamlÃ„Â± vizyon hizalama (vision alignment) raporu oluÃ…Å¸tur.

KARÃ…Å¾ILAÃ…Å¾TIR:
- README.md'deki hedefler Ã¢â€ â€ Mevcut kod
- Roadmap'teki planlar Ã¢â€ â€ GerÃƒÂ§ekleÃ…Å¸enler
- Performans hedefleri Ã¢â€ â€ GerÃƒÂ§ek metrikler
- Mimari diyagramlar Ã¢â€ â€ GerÃƒÂ§ek yapÃ„Â±

HER TUTARSIZLIK Ã„Â°Ãƒâ€¡Ã„Â°N:
1. Orijinal vizyon ne diyordu?
2. Mevcut durum ne?
3. Kayma ne zaman baÃ…Å¸lamÃ„Â±Ã…Å¸ olabilir?
4. Kritiklik seviyesi (dÃƒÂ¼Ã…Å¸ÃƒÂ¼k/orta/yÃƒÂ¼ksek)
5. DÃƒÂ¼zeltme ÃƒÂ¶nerisi

TÃƒÂ¼rkÃƒÂ§e, detaylÃ„Â± rapor ver."
```

---

### 3. Hidden Gems + Vision Drift Combo

```markdown
"HG+AI kodlarÃ„Â±yla projeyi Ã…Å¸u aÃƒÂ§Ã„Â±lardan analiz et:

1. HIDDEN GEMS (Gizli Potansiyel):
   - KullanÃ„Â±lmayan/undocumented ÃƒÂ¶zellikler
   - Optimize edilmemiÃ…Å¸ fÃ„Â±rsatlar
   - Eksik kalan implementasyonlar

2. VISION DRIFT (Vizyon KaymasÃ„Â±):
   - DokÃƒÂ¼mantasyon vs kod tutarsÃ„Â±zlÃ„Â±klarÃ„Â±
   - Planlanan vs gerÃƒÂ§ekleÃ…Å¸en farklarÃ„Â±
   - Eski mimari kararlar vs Ã…Å¸imdiki durum

3. ZOMBIE CODE:
   - ArtÃ„Â±k kullanÃ„Â±lmayan kod
   - Dead imports
   - Orphan fonksiyonlar

4. AI CODE QUALITY:
   - 'MÃ„Â±Ã…Å¸ gibi' pattern'ler
   - AI hallucinations
   - Copy-paste code smell'leri

Her bulgu iÃƒÂ§in:
- Konum (dosya:satÃ„Â±r)
- Orijinal vizyon referansÃ„Â±
- Mevcut durum
- Etki analizi
- Aksiyon ÃƒÂ¶nerisi"
```

---

### 4. DokÃƒÂ¼mantasyon-Kod Senkronizasyonu

```markdown
"DokÃƒÂ¼mantasyon-kod senkronizasyonunu kontrol et.

KARÃ…Å¾ILAÃ…Å¾TIR:
- docs/*.md Ã¢â€ â€ packages/*/src/
- API.md Ã¢â€ â€ GerÃƒÂ§ek API'ler
- README ÃƒÂ¶rnekleri Ã¢â€ â€ Ãƒâ€¡alÃ„Â±Ã…Å¸an kod
- JSDoc yorumlarÃ„Â± Ã¢â€ â€ Fonksiyon davranÃ„Â±Ã…Å¸larÃ„Â±

HER TUTARSIZLIK:
- [ ] DokÃƒÂ¼mantasyon gÃƒÂ¼ncel deÃ„Å¸il
- [ ] Kod dokÃƒÂ¼mante edilmemiÃ…Å¸
- [ ] YanlÃ„Â±Ã…Å¸ ÃƒÂ¶rnek/aÃƒÂ§Ã„Â±klama
- [ ] Eksik API referansÃ„Â±

Ãƒâ€“ncelik sÃ„Â±ralamasÃ„Â± ile listele.
TÃƒÂ¼rkÃƒÂ§e rapor."
```

---

## Ã°Å¸Å½Â¯ Proje Tipine GÃƒÂ¶re Ãƒâ€“rnekler

### Frontend Projesi (React/Vue/Angular)

```markdown
"FE-FULL koduyla frontend-focused analiz yap:
- UI/UX (UI)
- Performance (PERF)
- Accessibility (A11Y)
- State Management (STATE)
- React/TypeScript (REACT)
- Browser Compatibility (BROWSER)

TÃƒÂ¼rkÃƒÂ§e rapor, quick wins odaklÃ„Â±."
```

---

### Backend Projesi (.NET/Node.js)

```markdown
"BE-FULL koduyla backend-focused analiz yap:
- API Design (API)
- Database (DB)
- Security (SEC)
- Performance (PERF)
- .NET Core (DOTNET) veya ilgili stack

TÃƒÂ¼rkÃƒÂ§e rapor, P0-P1-P2 sÃ„Â±ralÃ„Â±."
```

---

### Full-Stack Projesi

```markdown
"FULLSTACK koduyla full-stack analiz yap:
TÃƒÂ¼m P0, P1 modÃƒÂ¼llerini yÃƒÂ¼kle.
Frontend ve backend'i ayrÃ„Â± ayrÃ„Â± skorla.
Entegrasyon noktalarÃ„Â±nÃ„Â± kontrol et.

TÃƒÂ¼rkÃƒÂ§e rapor:
- Executive summary
- Frontend skor: X/10
- Backend skor: Y/10
- Integration skor: Z/10"
```

---

### E-Ticaret Projesi (TÃƒÂ¼rk PazarÃ„Â±)

```markdown
"TR-ECOM koduyla TÃƒÂ¼rk e-ticaret projesi analizi:
- Fullstack analiz (FULLSTACK)
- TÃƒÂ¼rk piyasasÃ„Â± (TR: KVKK, e-Devlet, taksit)
- Feature gap (FG: Trendyol, Hepsiburada karÃ…Å¸Ã„Â±laÃ…Å¸tÃ„Â±rmasÃ„Â±)

TÃƒÂ¼rkÃƒÂ§e rapor:
- Rakip analizi
- Eksik ÃƒÂ¶zellikler (MoSCoW)
- Uyumluluk skorlarÃ„Â±
- 6 aylÃ„Â±k roadmap"
```

---

### SaaS Dashboard Projesi

```markdown
"FE-FULL+API+DB+FG kodlarÃ„Â±yla SaaS dashboard analizi:
- Frontend (modern UI/UX patterns)
- API (RESTful design)
- Database (query optimization)
- Feature Gap (Notion, Asana karÃ…Å¸Ã„Â±laÃ…Å¸tÃ„Â±rmasÃ„Â±)

TÃƒÂ¼rkÃƒÂ§e rapor:
- Competitive analysis
- Missing features
- UX improvement suggestions"
```

---

## Ã°Å¸Å½Â­ Ã„Â°leri Seviye Kombinasyonlar

### Selective Autonomous

```markdown
"SEC koduyla security sorunlarÃ„Â±nÃ„Â± Mode 3'te otomatik dÃƒÂ¼zelt, 
ama PERF koduyla performance iÃƒÂ§in Mode 2'de plan oluÃ…Å¸tur"
```

Ã¢â€ â€™ Mode 3 for security, Mode 2 for performance

---

### Iterative Refinement

```markdown
# AdÃ„Â±m 1:
"QUICK koduyla hÃ„Â±zlÃ„Â± scan yap" (Mode 1)

# AdÃ„Â±m 2:
"P0 iÃƒÂ§in plan oluÃ…Å¸tur" (Mode 2)

# AdÃ„Â±m 3:
"P0 dÃƒÂ¼zelt" (Mode 3)

# AdÃ„Â±m 4:
"SonuÃƒÂ§larÃ„Â± analiz et" (Mode 1)

# AdÃ„Â±m 5:
"P1 iÃƒÂ§in plan" (Mode 2)
```

---

### Hybrid Control

```markdown
"BASIC koduyla Mode 3'te kod yaz ama her dosya deÃ„Å¸iÃ…Å¸ikliÃ„Å¸inde onay al"
```

Ã¢â€ â€™ Mode 3 with granular checkpoints

---

### Focus + Expand Strategy

```markdown
# Step 1: Focused Analysis
"SEC+PERF kodlarÃ„Â±yla sadece kritik alanlar"

# Step 2: Expand
"AUDIT koduyla comprehensive analysis"

# Step 3: Deep Dive
"HG+AI kodlarÃ„Â±yla hidden issues"
```

---

## Ã°Å¸â€™Â¡ Prompt Ã„Â°yileÃ…Å¸tirme Direktifleri

Herhangi bir prompt'un sonuna eklenebilir:

```markdown
"Analiz yaparken:
Ã¢Å“â€¦ Her dosyayÃ„Â± tek tek incele
Ã¢Å“â€¦ SatÃ„Â±r numarasÃ„Â± ver
Ã¢Å“â€¦ Kod ÃƒÂ¶rnekleri gÃƒÂ¶ster (mevcut vs ÃƒÂ¶nerilen)
Ã¢Å“â€¦ Confidence level belirt (high/medium/low)
Ã¢Å“â€¦ Quick wins'leri ayrÃ„Â± listele
Ã¢Å“â€¦ TÃƒÂ¼rkÃƒÂ§e ÃƒÂ§Ã„Â±ktÃ„Â± ver
Ã¢Å“â€¦ Execution time tahmini ver
Ã¢Å“â€¦ P0-P1-P2-P3 ÃƒÂ¶ncelik sÃ„Â±ralamasÃ„Â± yap"
```

---

## Ã°Å¸â€â€ž Eksik AlanÃ„Â± Tamamlama

EÃ„Å¸er bir analiz sonrasÃ„Â±nda belirli bir alan eksik kalmÃ„Â±Ã…Å¸sa:

```markdown
"Ãƒâ€“nceki analizde [ALAN ADI] eksik kaldÃ„Â±.
Ã…Å¾imdi sadece [KOD] koduyla [ALAN ADI] iÃƒÂ§in deep dive yap.
DetaylÃ„Â± bulgular, kod ÃƒÂ¶rnekleri ve ÃƒÂ§ÃƒÂ¶zÃƒÂ¼m ÃƒÂ¶nerileri ver.
TÃƒÂ¼rkÃƒÂ§e rapor."

# Ãƒâ€“rnek:
"Ãƒâ€“nceki analizde security eksik kaldÃ„Â±.
Ã…Å¾imdi sadece SEC koduyla security iÃƒÂ§in deep dive yap."
```

---

## Ã°Å¸â€œâ€¹ GerÃƒÂ§ek DÃƒÂ¼nya SenaryolarÃ„Â±

### Senaryo 1: Yeni Proje Onboarding

```markdown
# Hafta 1: Quick Scan
"QUICK koduyla hÃ„Â±zlÃ„Â± scan yap, P0 bul"

# Hafta 2: Deep Dive
"FULLSTACK koduyla comprehensive analiz"

# Hafta 3: Turkish Market
"TR koduyla TÃƒÂ¼rk piyasasÃ„Â± compliance"

# Hafta 4: Planning
"AUDIT koduyla Mode 2 - Q1 roadmap"
```

---

### Senaryo 2: Production Deploy Ãƒâ€“ncesi

```markdown
"Production-ready mi kontrol et:
SEC koduyla security scan
PERF koduyla performance regression check
Breaking change var mÃ„Â±?
Rollback planÃ„Â± deÃ„Å¸erlendir

Mode 1 (sadece rapor), hiÃƒÂ§bir deÃ„Å¸iÃ…Å¸iklik yapma."
```

---

### Senaryo 3: Legacy Code Migration

```markdown
# Step 1: Health Check
"HG+AI kodlarÃ„Â±yla legacy code health check"

# Step 2: Refactoring Plan
"REFACTOR koduyla Mode 2 - migration roadmap"

# Step 3: Gradual Fix
"Mode 3 - P0'dan baÃ…Å¸la, incremental fix"
```

---

### Senaryo 4: Sprint Planning

```markdown
"FULLSTACK koduyla Mode 2 analiz:
- Current sprint achievements review
- Next sprint task breakdown
- P0-P1 prioritization
- Effort estimation (story points)
- Team capacity planning

TÃƒÂ¼rkÃƒÂ§e, sprint planning formatÃ„Â±nda."
```

---

### Senaryo 5: Competitive Analysis

```markdown
"FG+TR kodlarÃ„Â±yla competitive analysis:
- TÃƒÂ¼rk e-ticaret pazarÃ„Â±nda konumlandÃ„Â±rma
- Trendyol, Hepsiburada, N11 karÃ…Å¸Ã„Â±laÃ…Å¸tÃ„Â±rmasÃ„Â±
- Eksik ÃƒÂ¶zellikler (MoSCoW)
- Market opportunity gaps
- 6 aylÃ„Â±k feature roadmap

TÃƒÂ¼rkÃƒÂ§e business raporu."
```

---

## Ã¢Å“â€¦ Ã„Â°yi Prompt Ãƒâ€“rnekleri vs Ã¢ÂÅ’ KÃƒÂ¶tÃƒÂ¼ Prompt Ãƒâ€“rnekleri

### Ã¢Å“â€¦ Ã„Â°yi Prompt Ãƒâ€“rnekleri

```markdown
Ã¢Å“â€¦ "SEC+PERF kodlarÃ„Â±yla P0 security ve performance sorunlarÃ„Â±nÃ„Â± dÃƒÂ¼zelt"
   Ã¢â€ â€™ Spesifik, net, scope belirli

Ã¢Å“â€¦ "FE-FULL koduyla bu sprint iÃƒÂ§in aksiyon planÃ„Â±, task'leri ÃƒÂ¶nceliklendir"
   Ã¢â€ â€™ Hem kod hem mode hem output formatÃ„Â± belirtilmiÃ…Å¸

Ã¢Å“â€¦ "QUICK koduyla sadece frontend performance analizi"
   Ã¢â€ â€™ Scope sÃ„Â±nÃ„Â±rlÃ„Â±, net

Ã¢Å“â€¦ "API koduyla OrderService.cs'i analiz et, SQL injection var mÃ„Â± bak"
   Ã¢â€ â€™ Spesifik dosya, spesifik sorun

Ã¢Å“â€¦ "TR-ECOM koduyla Mode 2 - Q1 iÃƒÂ§in e-ticaret roadmap hazÃ„Â±rla"
   Ã¢â€ â€™ Net kod, net mode, net timeline
```

---

### Ã¢ÂÅ’ KÃƒÂ¶tÃƒÂ¼ Prompt Ãƒâ€“rnekleri

```markdown
Ã¢ÂÅ’ "DÃƒÂ¼zelt"
   Ã¢â€ â€™ Ne dÃƒÂ¼zeltilecek? Hangi modÃƒÂ¼l? Hangi mode?

Ã¢ÂÅ’ "Bir Ã…Å¸eyler yap"
   Ã¢â€ â€™ Vague, actionable deÃ„Å¸il

Ã¢ÂÅ’ "KodlarÃ„Â± oku"
   Ã¢â€ â€™ Ne amaÃƒÂ§la? Mode belirsiz

Ã¢ÂÅ’ "Fix it"
   Ã¢â€ â€™ Ã„Â°ngilizce + vague

Ã¢ÂÅ’ "Projeyi incele" (ÃƒÂ§ok genel, hangi modÃƒÂ¼ller?)
   Ã¢â€ â€™ ModÃƒÂ¼l belirtilmemiÃ…Å¸, detay yok
```

---

### Ã°Å¸Å½Â¯ Net OlmanÃ„Â±n Ãƒâ€“nemi

```markdown
Vague:   "Performance sorunlarÃ„Â± var"
Better:  "PERF koduyla performance analizi yap" (Mode 1)
Best:    "PERF koduyla performance sorunlarÃ„Â± iÃƒÂ§in sprint planÃ„Â±" (Mode 2)
Perfect: "PERF koduyla bundle size ve N+1 query'leri dÃƒÂ¼zelt" (Mode 3)
```

---

## Ã°Å¸Å¡â‚¬ HÃ„Â±zlÃ„Â± BaÃ…Å¸vuru KartlarÃ„Â±

### Security OdaklÃ„Â± Analiz

```markdown
"SEC+API+DB kodlarÃ„Â±yla security-first analiz
OWASP Top 10 kontrol et
SQL injection, XSS, CSRF var mÃ„Â±?
Secrets exposed mÃ„Â±?
Auth/Authz dÃƒÂ¼zgÃƒÂ¼n mÃƒÂ¼?
TÃƒÂ¼rkÃƒÂ§e rapor, P0-P1-P2 sÃ„Â±ralÃ„Â±"
```

---

### Performance OdaklÃ„Â± Analiz

```markdown
"PERF+DX+INFRA kodlarÃ„Â±yla performance optimization
Bundle size > 500KB var mÃ„Â±?
N+1 query'ler?
Build time > 60s?
Lazy loading eksik mi?
Core Web Vitals skorlarÃ„Â±?
TÃƒÂ¼rkÃƒÂ§e rapor, quick wins ÃƒÂ¶nce"
```

---

### Quality OdaklÃ„Â± Analiz

```markdown
"FS+TEST+REFACTOR+AI kodlarÃ„Â±yla code quality analizi
God files var mÃ„Â±?
Test coverage < %80?
Code smells?
AI-generated code issues?
Circular dependencies?
TÃƒÂ¼rkÃƒÂ§e rapor, refactoring plan dahil"
```

---

### Business OdaklÃ„Â± Analiz

```markdown
"FG+TR+SEO kodlarÃ„Â±yla market fit analizi
Feature completeness vs rakipler
TÃƒÂ¼rk piyasasÃ„Â± compliance (KVKK, e-Devlet)
SEO optimization durumu
Eksik ÃƒÂ¶zellikler (MoSCoW prioritization)
6 aylÃ„Â±k product roadmap
TÃƒÂ¼rkÃƒÂ§e business raporu"
```

---

## Ã¢Å¡Â Ã¯Â¸Â Dikkat Edilmesi Gerekenler

### Token BÃƒÂ¼tÃƒÂ§esi

| Kod | Token | SÃƒÂ¼re |
|-----|-------|------|
| QUICK | ~5.5K | 15 dk |
| BASIC | ~8K | 30 dk |
| FE-FULL | ~10K | 60 dk |
| FULLSTACK | ~14.6K | 90 dk |
| AUDIT | ~23K | 120 dk |
| DEEP | ~27.5K | 150+ dk |

### Zaman YÃƒÂ¶netimi

1. **HÃ„Â±zlÃ„Â± Decision**: QUICK (15 dk)
2. **Standart Analiz**: BASIC veya FULLSTACK (60-90 dk)
3. **Comprehensive**: AUDIT (2 saat)
4. **Deep Investigation**: DEEP (2.5+ saat)

### Ãƒâ€“neri

- **KÃƒÂ¼ÃƒÂ§ÃƒÂ¼k proje** (< 10K LOC): QUICK veya BASIC
- **Orta proje** (10-50K LOC): FE-FULL veya BE-FULL
- **BÃƒÂ¼yÃƒÂ¼k proje** (> 50K LOC): BÃƒÂ¶lÃƒÂ¼mlere ayÃ„Â±r, iterative yap

---

## Ã°Å¸â€œÅ¡ Ek Kaynaklar

- **ModÃƒÂ¼l KodlarÃ„Â±**: `MODULE_CODES.md`
- **DetaylÃ„Â± KullanÃ„Â±m**: `USAGE_GUIDE.md`
- **Mode GeÃƒÂ§iÃ…Å¸leri**: `MODE_TRANSITIONS.md`
- **GÃƒÂ¼venlik KurallarÃ„Â±**: `SAFETY_GATES.md`
- **Agent Entegrasyonu**: `AGENTIC_WORKFLOW.md`

---

## Ã°Å¸Å½â€œ Final Checklist: Ã„Â°yi Prompt Yazmak Ã„Â°ÃƒÂ§in

```markdown
[ ] Hangi modÃƒÂ¼lleri istediÃ„Å¸imi belirttim mi? (kodlarla)
[ ] Hangi mode'u istediÃ„Å¸imi belirttim mi? (1/2/3)
[ ] Output formatÃ„Â±nÃ„Â± belirttim mi? (TÃƒÂ¼rkÃƒÂ§e, ÃƒÂ¶ncelik sÃ„Â±ralÃ„Â±, vb)
[ ] Scope'u net belirttim mi? (hangi dosyalar, hangi alanlar)
[ ] Spesifik beklentilerimi ekledim mi? (quick wins, roadmap, vb)
```

**MÃƒÂ¼kemmel bir prompt ÃƒÂ¶rneÃ„Å¸i**:

```markdown
"FE-FULL+TR kodlarÃ„Â±yla TÃƒÂ¼rk pazarÃ„Â± iÃƒÂ§in frontend analizi yap.
Mode 2: Aksiyon planÃ„Â± oluÃ…Å¸tur, 3 sprint'lik breakdown.
P0-P1 ÃƒÂ¶ncelikli, quick wins ayrÃ„Â± listele.
TÃƒÂ¼rkÃƒÂ§e rapor:
- Executive summary
- DetaylÃ„Â± bulgular (dosya:satÃ„Â±r)
- Sprint 1/2/3 task'leri
- Effort estimation (saat)
- MoSCoW prioritization"
```

---

**ArtÃ„Â±k sistemi maksimum verimle kullanabilirsiniz!** Ã°Å¸Å¡â‚¬

**Not**: Bu dosya, EFFECTIVE_PROMPTS.md ve TURKISH_PROMPTS.md dosyalarÃ„Â±nÃ„Â±n birleÃ…Å¸tirilmiÃ…Å¸ ve geniÃ…Å¸letilmiÃ…Å¸ halidir. ModÃƒÂ¼l kodlama sistemi eklenerek kullanÃ„Â±m kolaylÃ„Â±Ã„Å¸Ã„Â± artÃ„Â±rÃ„Â±lmÃ„Â±Ã…Å¸tÃ„Â±r.

---

*OluÃ…Å¸turulma: AralÃ„Â±k 2024*
*Versiyon: 4.0 (Merged + Enhanced)*
*Son GÃƒÂ¼ncelleme: ModÃƒÂ¼l Kodlama Sistemi eklendi*
