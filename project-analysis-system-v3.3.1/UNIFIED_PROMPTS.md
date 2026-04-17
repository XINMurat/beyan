# Kapsamlı Prompt Rehberi - v4.0 (Birleştirilmiş)

**EFFECTIVE_PROMPTS.md + TURKISH_PROMPTS.md → Tek Dosyada**

**Amaç**: Sistemin tüm özelliklerini kullanarak en etkili prompt'ları yazmak için kapsamlı rehber.

---

## 📑 İçindekiler

1. [Modül Kodlama Sistemi](#modül-kodlama-sistemi)
2. [Mode Seçimi](#mode-seçimi)
3. [Türkçe Prompt Örnekleri](#türkçe-prompt-örnekleri)
4. [Kapsamlı Analiz Stratejileri](#kapsamlı-analiz-stratejileri)
5. [Vizyon Kayması Analizi](#vizyon-kayması-analizi)
6. [Proje Tipine Göre Örnekler](#proje-tipine-göre-örnekler)
7. [İleri Seviye Kombinasyonlar](#i̇leri-seviye-kombinasyonlar)

---

## 🎯 Modül Kodlama Sistemi

**Yeni Özellik!** Modülleri kısa kodlarla belirtin.

```markdown
# Temel Kullanım
"SEC+PERF koduyla analiz yap"
"FE-FULL koduyla frontend analizi"
"AUDIT koduyla comprehensive audit"
```

**Detaylı bilgi için**: `MODULE_CODES.md` dosyasına bakın.

### Hızlı Referans

| Kod | Modül | Kod | Modül |
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
- **AUDIT** = Tüm P0+P1+P2 modüller
- **TR-ECOM** = FULLSTACK+TR+FG

---

## 🎚️ Mode Seçimi (Hızlı Başvuru)

| Ne İstiyorsun? | Hangi Mode? | Örnek Prompt |
|----------------|-------------|--------------|
| Sadece rapor | **Mode 1** | "Projeyi analiz et" |
| Rapor + Plan | **Mode 2** | "Aksiyon planı oluştur" |
| Otomatik fix | **Mode 3** | "P0 sorunları düzelt" |

### Mode 1: Analyze Only (Sadece Analiz)

```markdown
"Projeyi analiz et"
"SEC+PERF koduyla security ve performance analizi"
"Mevcut durumu değerlendir, hiçbir değişiklik yapma"
```

### Mode 2: Analyze + Plan

```markdown
"Aksiyon planı oluştur"
"FULLSTACK koduyla analiz yap ve 3 sprint'lik plan hazırla"
"P0 sorunları için implementation roadmap çıkar"
```

### Mode 3: Full Flow (Semi-Autonomous)

```markdown
"P0 sorunları düzelt"
"BASIC koduyla Mode 3 - kritik sorunları otomatik çöz"
"Security vulnerabilities'i fix et, ama her checkpoint'te sor"
```

---

## 🇹🇷 Türkçe Prompt Örnekleri (100+)

### 1️⃣ Mode 1: Sadece Analiz

#### Genel Analiz

```markdown
"Projeyi analiz et"
"Proje sağlık raporu ver"
"Mevcut durumu deÄŸerlendir"
"Hızlı bir scan yap"
"Deep analysis yap"
"AUDIT koduyla comprehensive audit çalıştır"
```

#### Spesifik Alan Analizi

```markdown
"SEC koduyla security audit yap"
"PERF koduyla performans analizi çalıştır"
"DB koduyla database sorunlarını tespit et"
"UI koduyla UI/UX analizi yap"
"A11Y koduyla erişilebilirlik kontrolü yap"
"API koduyla API design review yap"
"HG koduyla hidden gem'leri bul"
"Technical debt hesapla"
"Code quality metrics ver"
```

#### Türk Piyasası Odaklı

```markdown
"TR koduyla KVKK uyumluluÄŸunu kontrol et"
"TR-ECOM koduyla Türk e-ticaret piyasası analizi"
"e-Devlet entegrasyonunu incele"
"Taksit sistemini deÄŸerlendir"
"Türkçe desteğini kontrol et"
```

#### AI-Generated Code Analizi

```markdown
"AI koduyla AI'nın yazdığı kodu incele"
"HG+AI koduyla 'mış gibi' pattern'leri bul"
"AI hallucination'larını tespit et"
"ChatGPT code smell'lerini ara"
```

#### Öncelik Bazlı

```markdown
"Sadece P0 sorunları göster"
"Kritik ve yüksek öncelikli sorunlar"
"Quick win'leri bul"
"En kolay düzeltilebilir sorunlar"
"En kritik 5 sorunu göster"
```

---

### 2️⃣ Mode 2: Analyze + Plan

#### Aksiyon Planı

```markdown
"Projeyi analiz et ve aksiyon planı oluştur"
"FULLSTACK koduyla aksiyon planı hazırla"
"Sprint planning yap"
"Task breakdown oluÅŸtur"
"Implementation plan hazırla"
"Execution roadmap çıkar"
```

#### Sprint Planning

```markdown
"Bu hafta için sprint planı"
"2 haftalık sprint oluştur"
"Sprint 1 için task'leri belirle"
"Bu sprint'te ne yapmalıyız?"
"Öncelikli task'leri sırala"
```

#### Roadmap

```markdown
"3 aylık roadmap hazırla"
"Q1 için plan oluştur"
"6 aylık teknik strateji"
"Yıllık iyileştirme planı"
"Milestone'ları belirle"
```

#### Epic & Story Breakdown

```markdown
"Epic'lere ayır"
"Story breakdown yap"
"Task hierarchy oluÅŸtur"
"Epic → Story → Task dönüşümü"
"Backlog organization yap"
```

#### Effort Estimation

```markdown
"Toplam çaba tahmini ver"
"Her task için süre belirle"
"Sprint capacity planning"
"Resource allocation öner"
"Team assignment planı"
```

---

### 3️⃣ Mode 3: Full Flow (Semi-Autonomous)

**⚠️ DİKKAT**: Kod yazar ve dosya değiştirir!

#### Genel Auto-Fix

```markdown
"P0 sorunları düzelt"
"Kritik sorunları otomatik çöz"
"SEC koduyla security vulnerabilities'i fix et"
"PERF koduyla performans sorunlarını düzelt"
"Tüm otomatik düzeltilebilir sorunları çöz"
```

#### Checkpoint Control

```markdown
"P0 düzelt, ama checkpoint'lerde sor"
"Full autonomous mode, ama onayımı al"
"Otomatik düzelt, önemli noktalarda dur"
"Her adımda bana sor"
```

#### Spesifik Sorun Fix

```markdown
"SQL injection'ları düzelt"
"Tüm exposed secrets'ı temizle"
"Missing authorization'ları ekle"
"N+1 query'leri optimize et"
"Bundle size'ı küçült"
"Build süresini optimize et"
```

#### Scope Limited

```markdown
"Sadece OrderService.cs'i düzelt"
"Backend security sorunlarını çöz"
"Frontend performance'ı optimize et"
"Sadece bu klasörde çalış: src/services/"
```

#### Batch Operations

```markdown
"Tüm P0 ve P1 sorunları düzelt"
"SEC+PERF koduyla güvenlik ve performans sorunlarını çöz"
"Frontend ve backend sorunlarını birlikte fix et"
```

#### Test-Only Mode

```markdown
"Kod yaz ve test et, ama commit etme"
"Fix'leri hazırla, ben commit edeceğim"
"DeÄŸiÅŸiklikleri stage'le ama push'lama"
```

#### Dry-Run Mode

```markdown
"Ne yapacağını göster ama değişiklik yapma"
"Simulation mode'da çalış"
"Kod yaz ama dosyalara dokunma"
"Preview mode"
```

---

## 📊 Kapsamlı Analiz Stratejileri

### Strateji 1: Tüm Modülleri Zorla Yüklet

```markdown
"Projeyi TÜM modüllerle kapsamlı analiz et. 
AUDIT koduyla P0, P1, P2, P3 ve SPECIALIZED modüllerin hepsini yükle. 
Her alanı kontrol et:
- Dosya yapısı (FS)
- Performans (PERF)
- UI/UX (UI)
- Güvenlik (SEC) - OWASP Top 10
- API tasarımı (API)
- Veritabanı (DB)
- EriÅŸilebilirlik (A11Y)
- Test stratejisi (TEST)
- Hidden gems (HG)
- AI-üretilmiş kod kalitesi (AI)

Deep analysis yap, hiçbir şeyi atlama."
```

---

### Strateji 2: Kategorileri Tek Tek Belirt

```markdown
"Projeyi analiz et ve şu alanları detaylı incele:
1. 📁 Dosya yapısı (FS kodu: god files, circular deps)
2. 🔒 Security (SEC kodu: SQL injection, secrets, auth)
3. âš¡ Performance (PERF kodu: bundle size, N+1 queries, build time)
4. 🎨 UI/UX (UI kodu: erişilebilirlik, responsive)
5. 🔌 API design (API kodu: REST conventions, error handling)
6. 💾 Database (DB kodu: queries, indexing)
7. 🧪 Testing (TEST kodu: coverage, test quality)
8. 🧟 Hidden gems (HG kodu: zombie code, unused features)
9. 🤖 AI code quality (AI kodu: mış gibi patterns)

Her kategori için ayrı skor ver."
```

---

### Strateji 3: Full Audit Modu

```markdown
"AUDIT koduyla full audit çalıştır. 
Maximum derinlikte analiz yap.
Tüm P0, P1, P2 sorunlarını tespit et.

Her bulgu için:
- Dosya yolu ve satır numarası
- Risk seviyesi
- Çözüm önerisi
- Tahmini süre

Hiçbir alanı atlama, comprehensive olsun.
Türkçe rapor ver."
```

---

### Strateji 4: Spesifik Tech Stack

```markdown
"Bu bir React + TypeScript + .NET Core projesi.
FE-FULL+BE-FULL kodlarıyla analiz yap:

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

Her modül için detaylı analiz yap."
```

---

### Strateji 5: En Kapsamlı Tek Prompt (Önerilen)

```markdown
"Bu projeyi DEEP koduyla analiz et (FULL AUDIT + Hidden Gems + AI Quality).

YÜKLENECEK MODÜLLER (hepsi):
FS, PERF, UI, SEC, HG, API, DB, TEST, AI, DX, A11Y, I18N, TR, FG

HER MODÜL İÇİN:
1. Mevcut durumu skorla (0-10)
2. Kritik bulguları listele (dosya yolu + satır)
3. Kod örnekleri göster (mevcut vs önerilen)
4. Çözüm öner
5. Tahmini süre ver

ÇIKTI:
- Türkçe
- P0, P1, P2, P3 öncelik sıralaması
- Executive summary
- Detaylı bulgular
- Aksiyon planı
- Quick wins ayrı listele

Hiçbir alanı atlama, kapsamlı ol."
```

---

## 🔍 Vizyon Kayması (Vision Drift) Analizi

Projenin orijinal vizyonu ile mevcut implementasyon arasındaki tutarsızlıkları tespit etmek için:

### 1. Temel Vizyon Analizi

```markdown
"HG koduyla projenin vizyon kaymasını (vision drift) analiz et.

KONTROL ET:
1. README ve dokümantasyondaki vaatler vs gerçek implementasyon
2. Başlangıçtaki mimari kararlar vs mevcut durum
3. Planlanan özellikler vs implementasyon durumu
4. Eski dokümantasyon vs yeni kod tutarsızlıkları

ÇIKTI:
- Vizyon uyum skoru (0-10)
- Tutarsızlıklar listesi
- Kayma noktaları (dosya + satır)
- Öneriler

Türkçe, detaylı rapor."
```

---

### 2. Detaylı Vizyon Hizalama Raporu

```markdown
"HG koduyla kapsamlı vizyon hizalama (vision alignment) raporu oluştur.

KARÅžILAÅžTIR:
- README.md'deki hedefler ↔ Mevcut kod
- Roadmap'teki planlar ↔ Gerçekleşenler
- Performans hedefleri ↔ Gerçek metrikler
- Mimari diyagramlar ↔ Gerçek yapı

HER TUTARSIZLIK İÇİN:
1. Orijinal vizyon ne diyordu?
2. Mevcut durum ne?
3. Kayma ne zaman başlamış olabilir?
4. Kritiklik seviyesi (düşük/orta/yüksek)
5. Düzeltme önerisi

Türkçe, detaylı rapor ver."
```

---

### 3. Hidden Gems + Vision Drift Combo

```markdown
"HG+AI kodlarıyla projeyi şu açılardan analiz et:

1. HIDDEN GEMS (Gizli Potansiyel):
   - Kullanılmayan/undocumented özellikler
   - Optimize edilmemiş fırsatlar
   - Eksik kalan implementasyonlar

2. VISION DRIFT (Vizyon Kayması):
   - Dokümantasyon vs kod tutarsızlıkları
   - Planlanan vs gerçekleşen farkları
   - Eski mimari kararlar vs ÅŸimdiki durum

3. ZOMBIE CODE:
   - Artık kullanılmayan kod
   - Dead imports
   - Orphan fonksiyonlar

4. AI CODE QUALITY:
   - 'Mış gibi' pattern'ler
   - AI hallucinations
   - Copy-paste code smell'leri

Her bulgu için:
- Konum (dosya:satır)
- Orijinal vizyon referansı
- Mevcut durum
- Etki analizi
- Aksiyon önerisi"
```

---

### 4. Dokümantasyon-Kod Senkronizasyonu

```markdown
"Dokümantasyon-kod senkronizasyonunu kontrol et.

KARÅžILAÅžTIR:
- docs/*.md ↔ packages/*/src/
- API.md ↔ Gerçek API'ler
- README örnekleri ↔ Çalışan kod
- JSDoc yorumları ↔ Fonksiyon davranışları

HER TUTARSIZLIK:
- [ ] Dokümantasyon güncel değil
- [ ] Kod dokümante edilmemiş
- [ ] Yanlış örnek/açıklama
- [ ] Eksik API referansı

Öncelik sıralaması ile listele.
Türkçe rapor."
```

---

## 🎯 Proje Tipine Göre Örnekler

### Frontend Projesi (React/Vue/Angular)

```markdown
"FE-FULL koduyla frontend-focused analiz yap:
- UI/UX (UI)
- Performance (PERF)
- Accessibility (A11Y)
- State Management (STATE)
- React/TypeScript (REACT)
- Browser Compatibility (BROWSER)

Türkçe rapor, quick wins odaklı."
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

Türkçe rapor, P0-P1-P2 sıralı."
```

---

### Full-Stack Projesi

```markdown
"FULLSTACK koduyla full-stack analiz yap:
Tüm P0, P1 modüllerini yükle.
Frontend ve backend'i ayrı ayrı skorla.
Entegrasyon noktalarını kontrol et.

Türkçe rapor:
- Executive summary
- Frontend skor: X/10
- Backend skor: Y/10
- Integration skor: Z/10"
```

---

### E-Ticaret Projesi (Türk Pazarı)

```markdown
"TR-ECOM koduyla Türk e-ticaret projesi analizi:
- Fullstack analiz (FULLSTACK)
- Türk piyasası (TR: KVKK, e-Devlet, taksit)
- Feature gap (FG: Trendyol, Hepsiburada karşılaştırması)

Türkçe rapor:
- Rakip analizi
- Eksik özellikler (MoSCoW)
- Uyumluluk skorları
- 6 aylık roadmap"
```

---

### SaaS Dashboard Projesi

```markdown
"FE-FULL+API+DB+FG kodlarıyla SaaS dashboard analizi:
- Frontend (modern UI/UX patterns)
- API (RESTful design)
- Database (query optimization)
- Feature Gap (Notion, Asana karşılaştırması)

Türkçe rapor:
- Competitive analysis
- Missing features
- UX improvement suggestions"
```

---

## 🎭 İleri Seviye Kombinasyonlar

### Selective Autonomous

```markdown
"SEC koduyla security sorunlarını Mode 3'te otomatik düzelt, 
ama PERF koduyla performance için Mode 2'de plan oluştur"
```

→ Mode 3 for security, Mode 2 for performance

---

### Iterative Refinement

```markdown
# Adım 1:
"QUICK koduyla hızlı scan yap" (Mode 1)

# Adım 2:
"P0 için plan oluştur" (Mode 2)

# Adım 3:
"P0 düzelt" (Mode 3)

# Adım 4:
"Sonuçları analiz et" (Mode 1)

# Adım 5:
"P1 için plan" (Mode 2)
```

---

### Hybrid Control

```markdown
"BASIC koduyla Mode 3'te kod yaz ama her dosya deÄŸiÅŸikliÄŸinde onay al"
```

→ Mode 3 with granular checkpoints

---

### Focus + Expand Strategy

```markdown
# Step 1: Focused Analysis
"SEC+PERF kodlarıyla sadece kritik alanlar"

# Step 2: Expand
"AUDIT koduyla comprehensive analysis"

# Step 3: Deep Dive
"HG+AI kodlarıyla hidden issues"
```

---

## 💡 Prompt İyileştirme Direktifleri

Herhangi bir prompt'un sonuna eklenebilir:

```markdown
"Analiz yaparken:
✅ Her dosyayı tek tek incele
✅ Satır numarası ver
✅ Kod örnekleri göster (mevcut vs önerilen)
✅ Confidence level belirt (high/medium/low)
✅ Quick wins'leri ayrı listele
✅ Türkçe çıktı ver
✅ Execution time tahmini ver
✅ P0-P1-P2-P3 öncelik sıralaması yap"
```

---

## 🔄 Eksik Alanı Tamamlama

Eğer bir analiz sonrasında belirli bir alan eksik kalmışsa:

```markdown
"Önceki analizde [ALAN ADI] eksik kaldı.
Şimdi sadece [KOD] koduyla [ALAN ADI] için deep dive yap.
Detaylı bulgular, kod örnekleri ve çözüm önerileri ver.
Türkçe rapor."

# Örnek:
"Önceki analizde security eksik kaldı.
Şimdi sadece SEC koduyla security için deep dive yap."
```

---

## 📋 Gerçek Dünya Senaryoları

### Senaryo 1: Yeni Proje Onboarding

```markdown
# Hafta 1: Quick Scan
"QUICK koduyla hızlı scan yap, P0 bul"

# Hafta 2: Deep Dive
"FULLSTACK koduyla comprehensive analiz"

# Hafta 3: Turkish Market
"TR koduyla Türk piyasası compliance"

# Hafta 4: Planning
"AUDIT koduyla Mode 2 - Q1 roadmap"
```

---

### Senaryo 2: Production Deploy Öncesi

```markdown
"Production-ready mi kontrol et:
SEC koduyla security scan
PERF koduyla performance regression check
Breaking change var mı?
Rollback planı değerlendir

Mode 1 (sadece rapor), hiçbir değişiklik yapma."
```

---

### Senaryo 3: Legacy Code Migration

```markdown
# Step 1: Health Check
"HG+AI kodlarıyla legacy code health check"

# Step 2: Refactoring Plan
"REFACTOR koduyla Mode 2 - migration roadmap"

# Step 3: Gradual Fix
"Mode 3 - P0'dan baÅŸla, incremental fix"
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

Türkçe, sprint planning formatında."
```

---

### Senaryo 5: Competitive Analysis

```markdown
"FG+TR kodlarıyla competitive analysis:
- Türk e-ticaret pazarında konumlandırma
- Trendyol, Hepsiburada, N11 karşılaştırması
- Eksik özellikler (MoSCoW)
- Market opportunity gaps
- 6 aylık feature roadmap

Türkçe business raporu."
```

---

## ✅ İyi Prompt Örnekleri vs ❌ Kötü Prompt Örnekleri

### ✅ İyi Prompt Örnekleri

```markdown
✅ "SEC+PERF kodlarıyla P0 security ve performance sorunlarını düzelt"
   → Spesifik, net, scope belirli

✅ "FE-FULL koduyla bu sprint için aksiyon planı, task'leri önceliklendir"
   → Hem kod hem mode hem output formatı belirtilmiş

✅ "QUICK koduyla sadece frontend performance analizi"
   → Scope sınırlı, net

✅ "API koduyla OrderService.cs'i analiz et, SQL injection var mı bak"
   → Spesifik dosya, spesifik sorun

✅ "TR-ECOM koduyla Mode 2 - Q1 için e-ticaret roadmap hazırla"
   → Net kod, net mode, net timeline
```

---

### ❌ Kötü Prompt Örnekleri

```markdown
❌ "Düzelt"
   → Ne düzeltilecek? Hangi modül? Hangi mode?

❌ "Bir şeyler yap"
   → Vague, actionable değil

❌ "Kodları oku"
   → Ne amaçla? Mode belirsiz

❌ "Fix it"
   → İngilizce + vague

❌ "Projeyi incele" (çok genel, hangi modüller?)
   → Modül belirtilmemiş, detay yok
```

---

### 🎯 Net Olmanın Önemi

```markdown
Vague:   "Performance sorunları var"
Better:  "PERF koduyla performance analizi yap" (Mode 1)
Best:    "PERF koduyla performance sorunları için sprint planı" (Mode 2)
Perfect: "PERF koduyla bundle size ve N+1 query'leri düzelt" (Mode 3)
```

---

## 🚀 Hızlı Başvuru Kartları

### Security Odaklı Analiz

```markdown
"SEC+API+DB kodlarıyla security-first analiz
OWASP Top 10 kontrol et
SQL injection, XSS, CSRF var mı?
Secrets exposed mı?
Auth/Authz düzgün mü?
Türkçe rapor, P0-P1-P2 sıralı"
```

---

### Performance Odaklı Analiz

```markdown
"PERF+DX+INFRA kodlarıyla performance optimization
Bundle size > 500KB var mı?
N+1 query'ler?
Build time > 60s?
Lazy loading eksik mi?
Core Web Vitals skorları?
Türkçe rapor, quick wins önce"
```

---

### Quality Odaklı Analiz

```markdown
"FS+TEST+REFACTOR+AI kodlarıyla code quality analizi
God files var mı?
Test coverage < %80?
Code smells?
AI-generated code issues?
Circular dependencies?
Türkçe rapor, refactoring plan dahil"
```

---

### Business Odaklı Analiz

```markdown
"FG+TR+SEO kodlarıyla market fit analizi
Feature completeness vs rakipler
Türk piyasası compliance (KVKK, e-Devlet)
SEO optimization durumu
Eksik özellikler (MoSCoW prioritization)
6 aylık product roadmap
Türkçe business raporu"
```

---

## ⚠️ Dikkat Edilmesi Gerekenler

### Token Bütçesi

| Kod | Token | Süre |
|-----|-------|------|
| QUICK | ~5.5K | 15 dk |
| BASIC | ~8K | 30 dk |
| FE-FULL | ~10K | 60 dk |
| FULLSTACK | ~14.6K | 90 dk |
| AUDIT | ~23K | 120 dk |
| DEEP | ~27.5K | 150+ dk |

### Zaman Yönetimi

1. **Hızlı Decision**: QUICK (15 dk)
2. **Standart Analiz**: BASIC veya FULLSTACK (60-90 dk)
3. **Comprehensive**: AUDIT (2 saat)
4. **Deep Investigation**: DEEP (2.5+ saat)

### Öneri

- **Küçük proje** (< 10K LOC): QUICK veya BASIC
- **Orta proje** (10-50K LOC): FE-FULL veya BE-FULL
- **Büyük proje** (> 50K LOC): Bölümlere ayır, iterative yap

---

## 📚 Ek Kaynaklar

- **Modül Kodları**: `MODULE_CODES.md`
- **Detaylı Kullanım**: `USAGE_GUIDE.md`
- **Mode Geçişleri**: `MODE_TRANSITIONS.md`
- **Güvenlik Kuralları**: `SAFETY_GATES.md`
- **Agent Entegrasyonu**: `AGENTIC_WORKFLOW.md`

---

## 🎓 Final Checklist: İyi Prompt Yazmak İçin

```markdown
[ ] Hangi modülleri istediğimi belirttim mi? (kodlarla)
[ ] Hangi mode'u istediÄŸimi belirttim mi? (1/2/3)
[ ] Output formatını belirttim mi? (Türkçe, öncelik sıralı, vb)
[ ] Scope'u net belirttim mi? (hangi dosyalar, hangi alanlar)
[ ] Spesifik beklentilerimi ekledim mi? (quick wins, roadmap, vb)
```

**Mükemmel bir prompt örneği**:

```markdown
"FE-FULL+TR kodlarıyla Türk pazarı için frontend analizi yap.
Mode 2: Aksiyon planı oluştur, 3 sprint'lik breakdown.
P0-P1 öncelikli, quick wins ayrı listele.
Türkçe rapor:
- Executive summary
- Detaylı bulgular (dosya:satır)
- Sprint 1/2/3 task'leri
- Effort estimation (saat)
- MoSCoW prioritization"
```

---

**Artık sistemi maksimum verimle kullanabilirsiniz!** 🚀

**Not**: Bu dosya, EFFECTIVE_PROMPTS.md ve TURKISH_PROMPTS.md dosyalarının birleştirilmiş ve genişletilmiş halidir. Modül kodlama sistemi eklenerek kullanım kolaylığı artırılmıştır.

---

*Oluşturulma: Aralık 2024*
*Versiyon: 4.0 (Merged + Enhanced)*
*Son Güncelleme: Modül Kodlama Sistemi eklendi*
