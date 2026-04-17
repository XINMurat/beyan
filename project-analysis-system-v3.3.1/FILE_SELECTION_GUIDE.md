# File Selection Guide - Hangi Dosyalar Kritik?

**Version**: 1.0  
**Purpose**: Kullanıcıya hangi dosyaları yüklemesi gerektiğini gösterme  
**Format**: Proje tipine göre önceliklendirilmiş liste

---

## 🎯 Temel Prensip

**"Kalite > Miktar"**

✅ **DOĞRU**: 20 kritik dosya yükle  
❌ **YANLIŞ**: 200 rastgele dosya yükle

---

## 📊 Dosya Öncelik Seviyeleri

| Seviye | Açıklama | Yükle? |
|--------|----------|--------|
| 🔴 **P0 - Kritik** | Analiz için mutlaka gerekli | ✅ MUTLAKA |
| 🟡 **P1 - Önemli** | Kaliteli analiz için önerilen | ✅ Önerilen |
| 🟢 **P2 - Faydalı** | İlave context sağlar | ⚪ Opsiyonel |
| ⚪ **P3 - Opsiyonel** | Nice-to-have | ⬜ Gerekirse |

---

## 🌐 WEB / FRONTEND PROJELERİ

### React + TypeScript

#### 🔴 P0 - Kritik (Mutlaka Yükle)
```yaml
package.json:
  why: "Dependencies, scripts, project metadata"
  analysis: "Tech stack detection, dependency audit"
  
tsconfig.json:
  why: "TypeScript config, strictness level"
  analysis: "Code quality standards, compiler options"
  
src/App.tsx:
  why: "Ana component, app structure"
  analysis: "Component architecture, routing"
  
src/index.tsx:
  why: "Entry point"
  analysis: "Root setup, providers, global config"

public/index.html:
  why: "HTML template, meta tags"
  analysis: "SEO, accessibility, performance hints"
```

#### 🟡 P1 - Önemli (Önerilen)
```yaml
.eslintrc.* veya eslint.config.*:
  why: "Code quality rules"
  analysis: "Linting standards, code conventions"
  
vite.config.ts / webpack.config.js:
  why: "Build config"
  analysis: "Bundle optimization, build process"
  
src/components/ (5-10 önemli component):
  why: "Component architecture"
  analysis: "Reusability, patterns, complexity"
  suggested:
    - Header/Navigation
    - Main layout components
    - Complex business logic components
  
src/services/ veya src/api/:
  why: "API interaction logic"
  analysis: "API design, error handling, state management"
  
src/types/ veya src/interfaces/:
  why: "TypeScript type definitions"
  analysis: "Type coverage, API contracts"
```

#### 🟢 P2 - Faydalı (Opsiyonel)
```yaml
src/utils/:
  why: "Helper functions"
  analysis: "Code reusability, DRY violations"
  
src/hooks/:
  why: "Custom React hooks"
  analysis: "Hook quality, dependency arrays"
  
src/contexts/:
  why: "State management"
  analysis: "Context usage, prop drilling"
  
tests/ veya __tests__/:
  why: "Test files"
  analysis: "Test coverage, test quality"
```

#### ⚪ P3 - Opsiyonel
```yaml
src/assets/:
  why: "Images, fonts"
  analysis: "Asset optimization (opsiyonel)"
  note: "Sadece image optimization analizi istiyorsan"
  
.github/:
  why: "CI/CD workflows"
  analysis: "DevOps maturity"
  
docs/:
  why: "Documentation"
  analysis: "Documentation quality"
```

---

### React + JavaScript (TypeScript olmadan)

Aynı ama şunlar yerine:
```yaml
# Yerine:
tsconfig.json → .eslintrc.*
src/types/ → Geçerli değil
*.tsx → *.jsx

# Ekstra önemli:
src/propTypes/:
  why: "Runtime type checking (TS olmadan)"
  priority: P1
```

---

### Vue.js Projeleri

#### 🔴 P0 - Kritik
```yaml
package.json: ✅
vite.config.js / vue.config.js: ✅
src/App.vue: ✅
src/main.js: ✅
public/index.html: ✅
```

#### 🟡 P1 - Önemli
```yaml
src/components/ (5-10 .vue files)
src/router/ veya src/routes/
src/store/ (Vuex/Pinia)
src/views/ (page components)
```

---

## ⚙️ BACKEND / API PROJELERİ

### .NET Core API

#### 🔴 P0 - Kritik
```yaml
*.csproj:
  why: "Project file, dependencies"
  analysis: "NuGet packages, target framework"
  
Startup.cs / Program.cs:
  why: "App configuration, middleware"
  analysis: "DI setup, middleware pipeline, CORS"
  
Controllers/ (tüm controller'lar):
  why: "API endpoints"
  analysis: "Routing, authorization, input validation"
  priority: P0
  
appsettings.json:
  why: "Configuration"
  analysis: "Security (secrets?), connection strings"
```

#### 🟡 P1 - Önemli
```yaml
Services/:
  why: "Business logic"
  analysis: "Separation of concerns, dependency injection"
  
Models/ veya DTOs/:
  why: "Data models"
  analysis: "Data validation, mapping"
  
Data/ veya Persistence/:
  why: "Database context, repositories"
  analysis: "DB design, queries, N+1 issues"
  
Migrations/:
  why: "Database schema evolution"
  analysis: "Migration safety, rollback capability"
```

#### 🟢 P2 - Faydalı
```yaml
Filters/:
  why: "Action filters, exception handling"
  
Middleware/:
  why: "Custom middleware"
  
Extensions/:
  why: "Helper extensions"
  
Tests/:
  why: "Unit/integration tests"
```

---

### Node.js / Express API

#### 🔴 P0 - Kritik
```yaml
package.json: ✅
src/index.js veya app.js: ✅
src/routes/ veya routes/: ✅
  
.env.example:
  why: "Required env vars (not actual .env!)"
  analysis: "Configuration requirements"
```

#### 🟡 P1 - Önemli
```yaml
src/controllers/:
  why: "Route handlers"
  
src/services/:
  why: "Business logic"
  
src/models/:
  why: "Data models (Mongoose, Sequelize)"
  
src/middleware/:
  why: "Auth, validation, error handling"
  
src/config/:
  why: "App configuration"
```

---

## 📱 MOBILE PROJELERİ

### React Native

#### 🔴 P0 - Kritik
```yaml
package.json: ✅
App.tsx veya App.js: ✅
app.json: ✅
  
src/navigation/:
  why: "Screen flow, routing"
  priority: P0
  
src/screens/ (major screens):
  why: "Main UI components"
  suggested: "Home, Profile, Main flow screens"
```

#### 🟡 P1 - Önemli
```yaml
src/components/:
  why: "Reusable components"
  
src/services/ veya src/api/:
  why: "API integration"
  
src/store/ veya src/context/:
  why: "State management"
  
ios/ veya android/ (native configs):
  why: "Platform-specific analysis"
  suggested: "Build configs, permissions"
```

---

## 🎯 FULL-STACK PROJELERİ

### Monorepo (Frontend + Backend)

```yaml
# Her iki taraftan da yükle

Frontend (client/):
  priority: P0
  files:
    - client/package.json
    - client/src/App.tsx
    - client/src/components/ (5-10)
    
Backend (server/):
  priority: P0
  files:
    - server/package.json veya *.csproj
    - server/src/routes/
    - server/src/controllers/
    
Shared:
  priority: P1
  files:
    - shared/types/ (ortak type'lar)
    - root package.json (workspace config)
```

---

## 🚫 YÜKLEMEMEN GEREKEN DOSYALAR

```yaml
❌ node_modules/:
  why: "Çok büyük, gereksiz"
  instead: "package.json yeter"
  
❌ .git/:
  why: "Git history gereksiz"
  instead: ".gitignore yeterli"
  
❌ dist/ veya build/:
  why: "Build output, geçici"
  instead: "Source dosyaları yeter"
  
❌ .env:
  why: "Secrets içerir! 🔒"
  instead: ".env.example kullan"
  
❌ coverage/:
  why: "Test coverage raporu, geçici"
  
❌ .next/, .nuxt/:
  why: "Framework cache, gereksiz"
```

---

## 📊 Dosya Sayısı Önerileri

### Proje Büyüklüğüne Göre

| Proje Tipi | Minimum | Önerilen | Maksimum |
|------------|---------|----------|----------|
| **Küçük** (<5K LOC) | 5-10 | 15-25 | 40 |
| **Orta** (5-50K LOC) | 10-20 | 30-50 | 100 |
| **Büyük** (>50K LOC) | 20-30 | 50-80 | 150 |

### Context Budget İçin

```yaml
quick_scan:
  files: "5-15"
  budget: "8,000 tokens"
  
standard_analysis:
  files: "20-50"
  budget: "15,000 tokens"
  
deep_analysis:
  files: "50-100"
  budget: "28,000 tokens"
  
hard_limit:
  max_files: "200"
  max_size: "200MB total"
```

---

## 🎯 Akıllı Seçim Stratejileri

### Strateji 1: "Core First"
```
1. Config dosyaları (package.json, tsconfig, etc.)
2. Entry points (App.tsx, index.tsx, main.ts)
3. Ana klasörler (components/, services/)
4. Eğer yer varsa: Tests, utils
```

### Strateji 2: "Problem-Focused"
```
Güvenlik analizi istiyorsan:
  → Controllers, API routes, auth logic
  
Performans analizi istiyorsan:
  → Components, build configs, queries
  
UI/UX analizi istiyorsan:
  → Components, pages, stylesheets
```

### Strateji 3: "Sampling"
```
Her klasörden representative dosyalar:
- components/: 5-10 örnek
- services/: 3-5 örnek
- utils/: 2-3 örnek

Total: 15-20 dosya ama tüm alanları temsil eder
```

---

## 🔍 Dosya Seçim Checklist

**Yüklemeden önce sor**:

```yaml
✅ Bu dosya projenin core'unda mı?
✅ Analiz için kritik bilgi içeriyor mu?
✅ Dosya boyutu makul mü? (<1MB ideal)
✅ Secrets/credentials yok mu? (kontrol et!)

❌ Build output mu? (dist/, build/)
❌ Dependencies mi? (node_modules/)
❌ Cache mi? (.next/, .cache/)
❌ Çok büyük mü? (>5MB)
```

---

## 💡 Pro Tips

### Tip 1: Klasör Yapısını Koru
```
✅ DOĞRU:
/src
  /components
    - Header.tsx
    - Footer.tsx
  /services
    - api.ts

Dosya isimleri klasör yapısını yansıtmalı
```

### Tip 2: Config Dosyalarını Unutma
```
Çoğu kişi unutur:
- .eslintrc.*
- tsconfig.json
- vite.config.ts

Ama bunlar code quality için kritik!
```

### Tip 3: Örnek Seç, Hepsini Değil
```
❌ components/ klasöründen 50 dosya
✅ components/ klasöründen 10 representative dosya

Sistem pattern'leri zaten anlayacaktır
```

---

## 📚 Related Documents

- `QUICK_START.md` - Hızlı başlangıç
- `SETUP_WIZARD.md` - İnteraktif kurulum
- `PROJECT_TYPE_DETECTION.md` - Otomatik algılama

---

**Doğru dosyaları seçersen, analiz kalitesi artar!** 📈
