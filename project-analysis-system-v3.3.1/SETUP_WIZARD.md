# Setup Wizard - İnteraktif Kurulum Rehberi

**Version**: 1.0  
**Purpose**: Kullanıcıyı adım adım optimal setup'a yönlendirme  
**Format**: Soru-cevap bazlı interaktif flow

---

## �?�? Kurulum Sihirbazı

Bu rehber seni **6 adımda** optimal kuruluma götürür.

---

## ADIM 1: Proje Tipin Nedir?

**Soru**: Hangi tür projeyi analiz edeceksin?

```
A. �??� Web/Frontend Projesi (React, Vue, Angular)
B. �??️  Backend API (Node.js, .NET, Python)
C. �??� Mobile App (React Native, Flutter)
D. �??� Full-stack Proje (Frontend + Backend)
E. �?�� Emin De�?ilim / Karı�?ık
```

**Seçimine göre yüklenmesi gereken dosyalar**:

### Seçim A: Web/Frontend
```yaml
required_files:
  core:
    - package.json �?? (Mutlaka)
    - src/ klasörü �??
    
  recommended:
    - tsconfig.json (TypeScript varsa)
    - .eslintrc.* (kod kalitesi için)
    - vite.config.* veya webpack.config.* (build için)
    
  optional:
    - public/ (assets için)
    - tests/ (test analizi için)

auto_load_modules:
  - ui-ux-analysis
  - performance-analysis
  - accessibility-analysis
  - react-typescript-analysis (React + TS ise)
  
estimated_analysis_time: "5-10 dakika"
```

### Seçim B: Backend API
```yaml
required_files:
  core:
    - *.csproj veya package.json �??
    - Controllers/ veya routes/ �??
    
  recommended:
    - appsettings.json (.NET için)
    - Services/, Models/ klasörleri
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

### Seçim C: Mobile App
```yaml
required_files:
  core:
    - package.json veya pubspec.yaml �??
    - src/ veya lib/ �??
    
  recommended:
    - App.tsx (React Native)
    - android/, ios/ klasörleri
    
  optional:
    - app.json (RN için)

auto_load_modules:
  - ui-ux-analysis
  - performance-analysis
  - mobile-responsive-analysis
  
estimated_analysis_time: "10-15 dakika"
```

### Seçim D: Full-stack
```yaml
required_files:
  frontend:
    - client/package.json �??
    - client/src/ �??
  
  backend:
    - server/package.json veya *.csproj �??
    - server/controllers/ �??

auto_load_modules:
  - ALL_MODULES (comprehensive scan)
  
estimated_analysis_time: "15-25 dakika"
warning: "Büyük context window gerektirir"
```

### Seçim E: Karı�?ık/Emin De�?ilim
```yaml
action: "Otomatik algılama yapılacak"
strategy: "Dosyaları yükle, sistem algılasın"

auto_detection_rules:
  - package.json + src/ �?? Web App
  - *.csproj + Controllers/ �?? .NET API
  - App.tsx + ios/ �?? React Native
  - pubspec.yaml �?? Flutter
```

---

## ADIM 2: Analiz Derinli�?i

**Soru**: Ne kadar detaylı analiz istiyorsun?

```
A. �?� Hızlı Scan (5 dakika)
B. �??? Standart Analiz (15 dakika) �?? �?nerilen
C. �??� Derin Analiz (30+ dakika)
```

### Seçim A: Hızlı Scan
```yaml
purpose: "Günlük health check, hızlı durum raporu"
modules: 
  - file-structure-analysis
  - Proje tipine göre 1-2 kritik modül
token_budget: 8000
output: "Genel skor + Top 5 sorun"
best_for: 
  - Daily standup reports
  - Quick status check
  - First-time users
```

### Seçim B: Standart Analiz ⭐
```yaml
purpose: "Kapsamlı analiz, aksiyon planı olu�?turma"
modules:
  - file-structure-analysis
  - performance-analysis
  - api-design-analysis (backend için)
  - ui-ux-analysis (frontend için)
  - security-analysis
token_budget: 15000
output: "Detaylı rapor + P0-P3 sorunlar"
best_for:
  - Sprint planning
  - Quarterly reviews
  - Most users �??
```

### Seçim C: Derin Analiz
```yaml
purpose: "Her �?eyi tarama, hidden gems, technical debt"
modules: ALL (24 modül)
token_budget: 28000
output: "Comprehensive report + roadmap + hidden gems"
best_for:
  - Major refactoring planning
  - M&A due diligence
  - Annual audits
warning: "Uzun sürer, büyük raporlar"
```

---

## ADIM 3: �?ncelik Oda�?ı

**Soru**: Hangi alanlar sana en önemli?

```
Seç (birden fazla seçebilirsin):

�?� �??? Güvenlik (Security)
�?� �?� Performans (Performance)
�?� �?� Eri�?ilebilirlik (Accessibility)
�?� �???️  Veritabanı (Database)
�?� �??� UI/UX (User Experience)
�?� �??� Mobil Uyumluluk (Responsive)
�?� �??� Türk Piyasası (KVKK, e-Devlet)
�?� �?�? AI Kod Kalitesi (AI-assisted dev)
```

**Seçimlerine göre modül yükleme**:

```yaml
security_focus:
  modules: 
    - security-analysis (OWASP)
    - api-design-analysis (auth/authz)
  priority_boost: "Security issues �?? P0"

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

## ADIM 4: �?alı�?ma Modu Seçimi

**Soru**: Sistemden ne yapmasını istiyorsun?

```
A. �??? Sadece Rapor (Mode 1) - Güvenli �??
B. �??? Rapor + Aksiyon Planı (Mode 2) - �?nerilen
C. �?�? Otomatik Düzeltme (Mode 3) - İleri Seviye
```

### Mode 1: Analyze Only
```yaml
what_it_does:
  - Projeyi analiz eder
  - Türkçe rapor olu�?turur
  - Hiçbir de�?i�?iklik YAPMAZ �??

best_for:
  - İlk kullanıcılar
  - Read-only eri�?im
  - Audit/compliance raporları

risk_level: "Yok (zero risk)"
output_files:
  - analysis-report.md

time: "5-15 dakika"
```

### Mode 2: Analyze + Plan
```yaml
what_it_does:
  - Analiz + Mode 1
  - Aksiyon planı olu�?turur
  - Sprint breakdown
  - Task assignment önerileri
  - Hiçbir de�?i�?iklik YAPMAZ �??

best_for:
  - Sprint planning
  - Roadmap olu�?turma
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
  - KOD YAZAR �?�️
  - DOSYALARI DE�?İ�?TİRİR �?�️
  - 3 checkpoint ile onay ister �??

safety_features:
  - Pre-execution checks
  - 3 human approval points
  - Auto-rollback on failure
  - Safety gates

best_for:
  - Experienced users
  - Trusted environments
  - Bulk fixes (P0 issues)

risk_level: "Orta (kontrollü)"
requirements:
  - Git branch (not main)
  - Backup available
  - Test coverage >50%

time: "15-30 dakika (includes execution)"
```

**İlk kez kullanıyorsan**: Mode 1 veya Mode 2 ile ba�?la �??

---

## ADIM 5: Dosya Seçimi

**Soru**: Hangi dosyaları yüklemeliyim?

### Otomatik �?neri (Proje Tipine Göre)

**Seçim**: "Otomati�?e güveniyorum" �??

Sistem �?unu söyler:
```
Proje tipin: React + TypeScript
�?nerilen dosyalar:
  �?? package.json
  �?? tsconfig.json
  �?? src/ (tüm klasör)
  �?? public/index.html
  �?� tests/ (opsiyonel ama önerilen)

Toplam: ~25-30 dosya
Context kullanımı: ~12,000 tokens
```

### Manuel Seçim

**Minimum Setup** (yeni kullanıcılar):
```
5-10 dosya:
- package.json veya *.csproj
- Ana klasörler (src/, controllers/)
- Config dosyaları
```

**Recommended Setup**:
```
20-40 dosya:
- Minimum + test dosyaları
- Build configs
- �?nemli component'ler
```

**Full Project**:
```
50-100+ dosya:
- Her �?ey (tüm proje)
- Not: Context limit var (200MB)
```

---

## ADIM 6: Final Checklist �??

**Kurulum tamamlanmadan önce kontrol et**:

```yaml
setup_checklist:
  proje_files: �?? En az 5 dosya yüklendi
  prompt_files: �?? ORCHESTRATOR + BASE yüklendi
  project_type: �?? Seçim yapıldı (A/B/C/D)
  analysis_depth: �?? Hızlı/Standart/Derin seçildi
  mode_selected: �?? Mode 1/2/3 seçildi
  
ready_to_start: true
```

**Hepsi �?? ise �?unu yaz**:

```markdown
"Setup tamamlandı, analiz ba�?lat"
```

Sistem:
```markdown
�?? Setup do�?rulandı
�??? Modüller yükleniyor: [security, performance, ui-ux]
�??� Analiz ba�?lıyor...

[5 saniye sonra]

# Proje Sa�?lık Raporu
...
```

---

## �??? Setup'ı De�?i�?tirme

**Analiz sırasında fikrin de�?i�?irse**:

```markdown
"Daha derin analiz yap, tüm modülleri yükle"
�?? Sistem modül ekler, yeniden tarar

"Sadece güvenlik odaklan"
�?? Di�?er alanları pas geçer

"Mode 3'e geç"
�?? Güvenlik kontrolleri yapar, geçi�?e izin verir
```

---

## �??� Wizard İpuçları

### �??� İlk Defa Kullanıyorsan
```
1. Proje tipi: Seç (A/B/C/D)
2. Derinlik: Standart
3. Mod: Mode 1 (sadece rapor)
4. Dosyalar: Otomatik öneri
```

### �?� Hızlı Health Check İstiyorsan
```
1. Proje tipi: Algıla (E)
2. Derinlik: Hızlı
3. Mod: Mode 1
4. Dosyalar: Minimum (5-10)
```

### �??? Sprint Planning Yapıyorsan
```
1. Proje tipi: Seç
2. Derinlik: Standart
3. Mod: Mode 2 (plan + report)
4. Dosyalar: Recommended (20-40)
```

### �??� Otomatik Fix İstiyorsan
```
1. Proje tipi: Seç
2. Derinlik: Standart
3. Mod: Mode 3 �?�️
4. Dosyalar: Full (50+)
Ek: Git branch check yap!
```

---

## �??? Setup Summary

**Wizard sonunda özet**:

```markdown
# Setup �?zeti

**Proje Tipi**: React + TypeScript Web App
**Analiz Derinli�?i**: Standart (15 min)
**Mod**: Mode 2 (Analyze + Plan)
**Odak Alanlar**: Security, Performance, Accessibility

**Yüklenecek Modüller**: 8
- �?? file-structure-analysis
- �?? ui-ux-analysis
- �?? performance-analysis
- �?? security-analysis
- �?? accessibility-analysis
- �?? react-typescript-analysis
- �?? code-quality-patterns
- �?? hidden-gems-deep-scan

**Token Budget**: 14,200 / 30,000 (47% kullanım)
**Tahmini Süre**: 12-15 dakika

**�?ıktılar**:
- analysis-report.md
- action-plan.md
- sprint-breakdown.md

�?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?��?�

�??? Ba�?lamaya hazır!

Devam etmek için yaz: "Analiz ba�?lat"
Setup'ı de�?i�?tir: "Setup'ı düzenle"
```

---

## �??? Wizard'da Sorun mu Var?

**"Proje tipimi bilmiyorum"**
�?? Seçenek E: Otomatik algılama

**"Hangi dosyaları yükleyece�?imi bilmiyorum"**
�?? Otomatik öneriye güven

**"Context window doldu"**
�?? Daha az dosya yükle veya Hızlı Scan seç

**"Setup çok karma�?ık"**
�?? `QUICK_START.md`'ye bak (5 dakika)

---

## �??? Related Documents

- `QUICK_START.md` - 5 dakikada ba�?la (wizard'sız)
- `FILE_SELECTION_GUIDE.md` - Hangi dosyalar kritik?
- `PROJECT_TYPE_DETECTION.md` - Otomatik algılama

---

**Wizard ile kurulum çok daha kolay!** �?�?�?�
