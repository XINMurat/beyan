# Setup Wizard - Ä°nteraktif Kurulum Rehberi

**Version**: 1.0  
**Purpose**: KullanÄ±cÄ±yÄ± adÄ±m adÄ±m optimal setup'a yÃ¶nlendirme  
**Format**: Soru-cevap bazlÄ± interaktif flow

---

## ðŸ§™ Kurulum SihirbazÄ±

Bu rehber seni **6 adÄ±mda** optimal kuruluma gÃ¶tÃ¼rÃ¼r.

---

## ADIM 1: Proje Tipin Nedir?

**Soru**: Hangi tÃ¼r projeyi analiz edeceksin?

```
A. ðŸŒ Web/Frontend Projesi (React, Vue, Angular)
B. âš™ï¸  Backend API (Node.js, .NET, Python)
C. ðŸ“± Mobile App (React Native, Flutter)
D. ðŸŽ¯ Full-stack Proje (Frontend + Backend)
E. ðŸ¤· Emin DeÄŸilim / KarÄ±ÅŸÄ±k
```

**SeÃ§imine gÃ¶re yÃ¼klenmesi gereken dosyalar**:

### SeÃ§im A: Web/Frontend
```yaml
required_files:
  core:
    - package.json âœ… (Mutlaka)
    - src/ klasÃ¶rÃ¼ âœ…
    
  recommended:
    - tsconfig.json (TypeScript varsa)
    - .eslintrc.* (kod kalitesi iÃ§in)
    - vite.config.* veya webpack.config.* (build iÃ§in)
    
  optional:
    - public/ (assets iÃ§in)
    - tests/ (test analizi iÃ§in)

auto_load_modules:
  - ui-ux-analysis
  - performance-analysis
  - accessibility-analysis
  - react-typescript-analysis (React + TS ise)
  
estimated_analysis_time: "5-10 dakika"
```

### SeÃ§im B: Backend API
```yaml
required_files:
  core:
    - *.csproj veya package.json âœ…
    - Controllers/ veya routes/ âœ…
    
  recommended:
    - appsettings.json (.NET iÃ§in)
    - Services/, Models/ klasÃ¶rleri
    - Database migrations
    
  optional:
    - Startup.cs, Program.cs
    - Tests/

auto_load_modules:
  - api-design-analysis
  - database-analysis
  - security-analysis
  - dotnet-core-analysis (.NET ise)
  
estimated_analysis_time: "8-15 dakika"
```

### SeÃ§im C: Mobile App
```yaml
required_files:
  core:
    - package.json veya pubspec.yaml âœ…
    - src/ veya lib/ âœ…
    
  recommended:
    - App.tsx (React Native)
    - android/, ios/ klasÃ¶rleri
    
  optional:
    - app.json (RN iÃ§in)

auto_load_modules:
  - ui-ux-analysis
  - performance-analysis
  - mobile-responsive-analysis
  
estimated_analysis_time: "10-15 dakika"
```

### SeÃ§im D: Full-stack
```yaml
required_files:
  frontend:
    - client/package.json âœ…
    - client/src/ âœ…
  
  backend:
    - server/package.json veya *.csproj âœ…
    - server/controllers/ âœ…

auto_load_modules:
  - ALL_MODULES (comprehensive scan)
  
estimated_analysis_time: "15-25 dakika"
warning: "BÃ¼yÃ¼k context window gerektirir"
```

### SeÃ§im E: KarÄ±ÅŸÄ±k/Emin DeÄŸilim
```yaml
action: "Otomatik algÄ±lama yapÄ±lacak"
strategy: "DosyalarÄ± yÃ¼kle, sistem algÄ±lasÄ±n"

auto_detection_rules:
  - package.json + src/ â†’ Web App
  - *.csproj + Controllers/ â†’ .NET API
  - App.tsx + ios/ â†’ React Native
  - pubspec.yaml â†’ Flutter
```

---

## ADIM 2: Analiz DerinliÄŸi

**Soru**: Ne kadar detaylÄ± analiz istiyorsun?

```
A. âš¡ HÄ±zlÄ± Scan (5 dakika)
B. ðŸ“Š Standart Analiz (15 dakika) âœ… Ã–nerilen
C. ðŸ” Derin Analiz (30+ dakika)
```

### SeÃ§im A: HÄ±zlÄ± Scan
```yaml
purpose: "GÃ¼nlÃ¼k health check, hÄ±zlÄ± durum raporu"
modules: 
  - file-structure-analysis
  - Proje tipine gÃ¶re 1-2 kritik modÃ¼l
token_budget: 8000
output: "Genel skor + Top 5 sorun"
best_for: 
  - Daily standup reports
  - Quick status check
  - First-time users
```

### SeÃ§im B: Standart Analiz â­
```yaml
purpose: "KapsamlÄ± analiz, aksiyon planÄ± oluÅŸturma"
modules:
  - file-structure-analysis
  - performance-analysis
  - api-design-analysis (backend iÃ§in)
  - ui-ux-analysis (frontend iÃ§in)
  - security-analysis
token_budget: 15000
output: "DetaylÄ± rapor + P0-P3 sorunlar"
best_for:
  - Sprint planning
  - Quarterly reviews
  - Most users âœ…
```

### SeÃ§im C: Derin Analiz
```yaml
purpose: "Her ÅŸeyi tarama, hidden gems, technical debt"
modules: ALL (24 modÃ¼l)
token_budget: 28000
output: "Comprehensive report + roadmap + hidden gems"
best_for:
  - Major refactoring planning
  - M&A due diligence
  - Annual audits
warning: "Uzun sÃ¼rer, bÃ¼yÃ¼k raporlar"
```

---

## ADIM 3: Ã–ncelik OdaÄŸÄ±

**Soru**: Hangi alanlar sana en Ã¶nemli?

```
SeÃ§ (birden fazla seÃ§ebilirsin):

â–¡ ðŸ”’ GÃ¼venlik (Security)
â–¡ âš¡ Performans (Performance)
â–¡ â™¿ EriÅŸilebilirlik (Accessibility)
â–¡ ðŸ—„ï¸  VeritabanÄ± (Database)
â–¡ ðŸŽ¨ UI/UX (User Experience)
â–¡ ðŸ“± Mobil Uyumluluk (Responsive)
â–¡ ðŸŒ TÃ¼rk PiyasasÄ± (KVKK, e-Devlet)
â–¡ ðŸ¤– AI Kod Kalitesi (AI-assisted dev)
```

**SeÃ§imlerine gÃ¶re modÃ¼l yÃ¼kleme**:

```yaml
security_focus:
  modules: 
    - security-analysis (OWASP)
    - api-design-analysis (auth/authz)
  priority_boost: "Security issues â†’ P0"

performance_focus:
  modules:
    - performance-analysis
    - database-analysis (query optimization)
  metrics: "LCP, FCP, TTI, bundle size"

accessibility_focus:
  modules:
    - accessibility-analysis (WCAG)
    - ui-ux-analysis
  compliance: "WCAG AA minimum"

turkish_market_focus:
  modules:
    - turkish-market (KVKK, e-Devlet)
    - i18n-analysis (TR karakterler)
  checks: "KVKK compliance, Turkish lang support"
```

---

## ADIM 4: Ã‡alÄ±ÅŸma Modu SeÃ§imi

**Soru**: Sistemden ne yapmasÄ±nÄ± istiyorsun?

```
A. ðŸ“„ Sadece Rapor (Mode 1) - GÃ¼venli âœ…
B. ðŸ“‹ Rapor + Aksiyon PlanÄ± (Mode 2) - Ã–nerilen
C. ðŸ¤– Otomatik DÃ¼zeltme (Mode 3) - Ä°leri Seviye
```

### Mode 1: Analyze Only
```yaml
what_it_does:
  - Projeyi analiz eder
  - TÃ¼rkÃ§e rapor oluÅŸturur
  - HiÃ§bir deÄŸiÅŸiklik YAPMAZ âœ…

best_for:
  - Ä°lk kullanÄ±cÄ±lar
  - Read-only eriÅŸim
  - Audit/compliance raporlarÄ±

risk_level: "Yok (zero risk)"
output_files:
  - analysis-report.md

time: "5-15 dakika"
```

### Mode 2: Analyze + Plan
```yaml
what_it_does:
  - Analiz + Mode 1
  - Aksiyon planÄ± oluÅŸturur
  - Sprint breakdown
  - Task assignment Ã¶nerileri
  - HiÃ§bir deÄŸiÅŸiklik YAPMAZ âœ…

best_for:
  - Sprint planning
  - Roadmap oluÅŸturma
  - Team coordination

risk_level: "Yok (zero risk)"
output_files:
  - analysis-report.md
  - action-plan.md
  - sprint-breakdown.md
  - roadmap-Q1-2025.md

time: "10-20 dakika"
```

### Mode 3: Full Flow (Autonomous)
```yaml
what_it_does:
  - Analiz + Plan + Mode 1-2
  - KOD YAZAR âš ï¸
  - DOSYALARI DEÄžÄ°ÅžTÄ°RÄ°R âš ï¸
  - 3 checkpoint ile onay ister âœ…

safety_features:
  - Pre-execution checks
  - 3 human approval points
  - Auto-rollback on failure
  - Safety gates

best_for:
  - Experienced users
  - Trusted environments
  - Bulk fixes (P0 issues)

risk_level: "Orta (kontrollÃ¼)"
requirements:
  - Git branch (not main)
  - Backup available
  - Test coverage >50%

time: "15-30 dakika (includes execution)"
```

**Ä°lk kez kullanÄ±yorsan**: Mode 1 veya Mode 2 ile baÅŸla âœ…

---

## ADIM 5: Dosya SeÃ§imi

**Soru**: Hangi dosyalarÄ± yÃ¼klemeliyim?

### Otomatik Ã–neri (Proje Tipine GÃ¶re)

**SeÃ§im**: "OtomatiÄŸe gÃ¼veniyorum" âœ…

Sistem ÅŸunu sÃ¶yler:
```
Proje tipin: React + TypeScript
Ã–nerilen dosyalar:
  âœ… package.json
  âœ… tsconfig.json
  âœ… src/ (tÃ¼m klasÃ¶r)
  âœ… public/index.html
  âšª tests/ (opsiyonel ama Ã¶nerilen)

Toplam: ~25-30 dosya
Context kullanÄ±mÄ±: ~12,000 tokens
```

### Manuel SeÃ§im

**Minimum Setup** (yeni kullanÄ±cÄ±lar):
```
5-10 dosya:
- package.json veya *.csproj
- Ana klasÃ¶rler (src/, controllers/)
- Config dosyalarÄ±
```

**Recommended Setup**:
```
20-40 dosya:
- Minimum + test dosyalarÄ±
- Build configs
- Ã–nemli component'ler
```

**Full Project**:
```
50-100+ dosya:
- Her ÅŸey (tÃ¼m proje)
- Not: Context limit var (200MB)
```

---

## ADIM 6: Final Checklist âœ…

**Kurulum tamamlanmadan Ã¶nce kontrol et**:

```yaml
setup_checklist:
  proje_files: âœ… En az 5 dosya yÃ¼klendi
  prompt_files: âœ… ORCHESTRATOR + BASE yÃ¼klendi
  project_type: âœ… SeÃ§im yapÄ±ldÄ± (A/B/C/D)
  analysis_depth: âœ… HÄ±zlÄ±/Standart/Derin seÃ§ildi
  mode_selected: âœ… Mode 1/2/3 seÃ§ildi
  
ready_to_start: true
```

**Hepsi âœ… ise ÅŸunu yaz**:

```markdown
"Setup tamamlandÄ±, analiz baÅŸlat"
```

Sistem:
```markdown
âœ… Setup doÄŸrulandÄ±
ðŸ“Š ModÃ¼ller yÃ¼kleniyor: [security, performance, ui-ux]
ðŸ” Analiz baÅŸlÄ±yor...

[5 saniye sonra]

# Proje SaÄŸlÄ±k Raporu
...
```

---

## ðŸ”„ Setup'Ä± DeÄŸiÅŸtirme

**Analiz sÄ±rasÄ±nda fikrin deÄŸiÅŸirse**:

```markdown
"Daha derin analiz yap, tÃ¼m modÃ¼lleri yÃ¼kle"
â†’ Sistem modÃ¼l ekler, yeniden tarar

"Sadece gÃ¼venlik odaklan"
â†’ DiÄŸer alanlarÄ± pas geÃ§er

"Mode 3'e geÃ§"
â†’ GÃ¼venlik kontrolleri yapar, geÃ§iÅŸe izin verir
```

---

## ðŸ’¡ Wizard Ä°puÃ§larÄ±

### ðŸŽ¯ Ä°lk Defa KullanÄ±yorsan
```
1. Proje tipi: SeÃ§ (A/B/C/D)
2. Derinlik: Standart
3. Mod: Mode 1 (sadece rapor)
4. Dosyalar: Otomatik Ã¶neri
```

### âš¡ HÄ±zlÄ± Health Check Ä°stiyorsan
```
1. Proje tipi: AlgÄ±la (E)
2. Derinlik: HÄ±zlÄ±
3. Mod: Mode 1
4. Dosyalar: Minimum (5-10)
```

### ðŸš€ Sprint Planning YapÄ±yorsan
```
1. Proje tipi: SeÃ§
2. Derinlik: Standart
3. Mod: Mode 2 (plan + report)
4. Dosyalar: Recommended (20-40)
```

### ðŸ”§ Otomatik Fix Ä°stiyorsan
```
1. Proje tipi: SeÃ§
2. Derinlik: Standart
3. Mod: Mode 3 âš ï¸
4. Dosyalar: Full (50+)
Ek: Git branch check yap!
```

---

## ðŸ“Š Setup Summary

**Wizard sonunda Ã¶zet**:

```markdown
# Setup Ã–zeti

**Proje Tipi**: React + TypeScript Web App
**Analiz DerinliÄŸi**: Standart (15 min)
**Mod**: Mode 2 (Analyze + Plan)
**Odak Alanlar**: Security, Performance, Accessibility

**YÃ¼klenecek ModÃ¼ller**: 8
- âœ… file-structure-analysis
- âœ… ui-ux-analysis
- âœ… performance-analysis
- âœ… security-analysis
- âœ… accessibility-analysis
- âœ… react-typescript-analysis
- âœ… code-quality-patterns
- âœ… hidden-gems-deep-scan

**Token Budget**: 14,200 / 30,000 (47% kullanÄ±m)
**Tahmini SÃ¼re**: 12-15 dakika

**Ã‡Ä±ktÄ±lar**:
- analysis-report.md
- action-plan.md
- sprint-breakdown.md

â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”

ðŸš€ BaÅŸlamaya hazÄ±r!

Devam etmek iÃ§in yaz: "Analiz baÅŸlat"
Setup'Ä± deÄŸiÅŸtir: "Setup'Ä± dÃ¼zenle"
```

---

## ðŸ†˜ Wizard'da Sorun mu Var?

**"Proje tipimi bilmiyorum"**
â†’ SeÃ§enek E: Otomatik algÄ±lama

**"Hangi dosyalarÄ± yÃ¼kleyeceÄŸimi bilmiyorum"**
â†’ Otomatik Ã¶neriye gÃ¼ven

**"Context window doldu"**
â†’ Daha az dosya yÃ¼kle veya HÄ±zlÄ± Scan seÃ§

**"Setup Ã§ok karmaÅŸÄ±k"**
â†’ `QUICK_START.md`'ye bak (5 dakika)

---

## ðŸ“š Related Documents

- `QUICK_START.md` - 5 dakikada baÅŸla (wizard'sÄ±z)
- `FILE_SELECTION_GUIDE.md` - Hangi dosyalar kritik?
- `PROJECT_TYPE_DETECTION.md` - Otomatik algÄ±lama

---

**Wizard ile kurulum Ã§ok daha kolay!** ðŸ§™âœ¨
