# Agentic Workflow - Trae IDE Integration

**Özel**: Trae IDE agent yapısı için optimize edilmiş

---

## 🤖 Trae IDE Agent Yapısı

```
Orchestrator (Ana Beyin)
├─ 📐 Architect Guardian (Mimari Gözetim)
├─ 🎨 Frontend Agent (UI/UX)
├─ ⚙️ Backend Agent (API/DB)
├─ 🔗 Integration Agent (API Integration)
└─ 👤 Human (Checkpoint'ler)
```

---

## 🎯 Agent Görev Dağılımı

### Architect Guardian
**Sorumluluk**: Mimari kararlar, UMT uyumluluğu, genel koordinasyon

**Görevler**:
- Analiz sonuçlarını değerlendir
- Hangi agent hangi sorunu çözsün planla
- rules.md uyumluluğunu kontrol et
- Agent'lar arası çakışmaları çöz

**Örnek**:
```
P0: SQL Injection (OrderService.cs)
├─ Architect: "Backend agent düzeltsin"
├─ Backend: Kodu yaz
├─ Architect: "UMT'ye uygun mu?" → ✅
└─ Devam et
```

---

### Frontend Agent
**Sorumluluk**: UI, UX, accessibility, performance (frontend)

**Çözdüğü Sorunlar**:
- Alt text eksiklikleri
- Renk kontrastı sorunları
- Bundle size optimizasyonu
- Lazy loading implementasyonu
- Responsive design sorunları

**Örnek**:
```tsx
// Frontend Agent - Alt text ekleme
<img src="product.jpg" alt="Mavi kot pantolon, slim fit, beden 32" />
```

---

### Backend Agent
**Sorumluluk**: API, database, security (backend)

**Çözdüğü Sorunlar**:
- SQL injection
- N+1 query'ler
- Authorization eksiklikleri
- Password hashing
- API design sorunları

**Örnek**:
```csharp
// Backend Agent - SQL injection fix
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();
```

---

### Integration Agent
**Sorumluluk**: API entegrasyonları, third-party servisler

**Çözdüğü Sorunlar**:
- CORS konfigürasyonu
- External API hata yönetimi
- Webhook implementasyonları
- Rate limiting

**Örnek**:
```csharp
// Integration Agent - CORS fix
builder.Services.AddCors(options => {
    options.AddPolicy("Production", builder => {
        builder.WithOrigins("https://app.example.com")
               .AllowCredentials();
    });
});
```

---

## 🔄 Workflow: Adım Adım

### 1. Analysis Phase (Orchestrator)

```markdown
Orchestrator:
├─ BASE_PROMPT.md yükle
├─ İlgili modülleri seç
├─ Analiz çalıştır
└─ Rapor oluştur

Output: analysis-report.md
```

---

### 2. Planning Phase (Architect Guardian)

```markdown
Architect Guardian:
├─ Raporu incele
├─ Sorunları kategorize et
│   ├─ Frontend → Frontend Agent
│   ├─ Backend → Backend Agent
│   └─ Integration → Integration Agent
│
├─ Önceliklendirme (P0, P1, P2)
├─ Dependencies tespit et
│   └─ "SQL injection fix önce, sonra N+1"
│
└─ Aksiyon planı oluştur

Output: action-plan.md
```

**Checkpoint #1**: Plan onayı

---

### 3. Implementation Phase (Agents)

#### 3.1 Backend Agent İş Başında

```markdown
Backend Agent receives: Task #1 (SQL Injection)

Adım 1: Implementation guide oku
├─ /IMPLEMENTATION_GUIDES/security-fixes.md
└─ SQL Injection bölümünü bul

Adım 2: Mevcut kodu analiz et
├─ OrderService.cs:45 oku
└─ Sorunu tespit et

Adım 3: Test yaz (TDD)
```csharp
[Test]
public void GetOrders_WithMaliciousInput_ShouldThrow()
{
    var maliciousId = "1 OR 1=1";
    Assert.Throws<FormatException>(() => 
        orderService.GetOrders(maliciousId)
    );
}
```

Adım 4: Kodu düzelt
```csharp
// Parameterized query
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();
```

Adım 5: Test çalıştır
├─ dotnet test
└─ ✅ Geçti

Adım 6: Architect'e bildir
└─ "Task #1 tamamlandı, review?"

Architect Guardian:
├─ Kodu incele
├─ rules.md'ye uygun mu? ✅
├─ UMT principles ihlal etmiş mi? ❌
└─ Onayla
```

#### 3.2 Frontend Agent İş Başında

```markdown
Frontend Agent receives: Task #5 (Bundle Size)

Adım 1: Bundle analiz et
├─ webpack-bundle-analyzer çalıştır
└─ moment.js çok büyük (67 KB)

Adım 2: Implementation guide oku
├─ /IMPLEMENTATION_GUIDES/performance-optimization.md
└─ "Moment.js → date-fns" bölümü

Adım 3: Değiştir
```typescript
// Öncesi
import moment from 'moment';
const formatted = moment(date).format('DD.MM.YYYY');

// Sonrası
import { format } from 'date-fns';
import { tr } from 'date-fns/locale';
const formatted = format(date, 'dd.MM.yyyy', { locale: tr });
```

Adım 4: Test et
├─ npm test
├─ npm run build
└─ Bundle size: 847 KB → 780 KB ✅

Adım 5: Architect'e bildir
```

#### 3.3 Agent Coordination (Çakışma Durumu)

```markdown
Senaryo: Backend ve Frontend agent aynı dosyada çalışıyor

Backend Agent: OrderService.cs → SQL injection fix
Frontend Agent: OrderList.tsx → API call değişikliği

Çakışma Riski:
Backend API'yi değiştirirse, Frontend'in API call'u bozulabilir

Architect Guardian çözümü:
├─ Backend agent'ı önce çalıştır
├─ API contract'ı kontrol et
│   └─ Breaking change var mı?
│
├─ Varsa:
│   ├─ Versioning ekle (/api/v2/orders)
│   └─ Frontend'e bildir
│
└─ Frontend agent'ı çalıştır
    └─ Yeni API'ye göre update et
```

---

### 4. Testing Phase (All Agents + Orchestrator)

```markdown
Orchestrator:
├─ Tüm agent'ların işi bitti mi? ✅
├─ Unit tests çalıştır
│   ├─ Backend tests: ✅
│   ├─ Frontend tests: ✅
│   └─ Integration tests: ✅
│
├─ Build
│   ├─ Backend: dotnet build ✅
│   └─ Frontend: npm run build ✅
│
├─ Security scan
│   ├─ npm audit ✅
│   └─ Semgrep ✅
│
└─ Performance check
    ├─ Build time: 85s → 28s ✅
    └─ Bundle size: 847KB → 320KB ✅
```

**Checkpoint #2**: Test sonuçları onayı

---

### 5. Commit Phase (Orchestrator)

```markdown
Orchestrator:
├─ git add .
├─ Commit message hazırla (tüm agent'ların işini kapsa)
└─ git commit

Commit Message:
─────────────────────────────────
fix: resolve P0 security and performance issues

Backend (Backend Agent):
- Fix SQL injection in OrderService
- Add authorization to admin endpoints

Frontend (Frontend Agent):
- Replace moment.js with date-fns
- Add lazy loading to admin routes

Integration (Integration Agent):
- Fix CORS configuration

Co-authored-by: Backend Agent <backend@trae.ai>
Co-authored-by: Frontend Agent <frontend@trae.ai>
Co-authored-by: Integration Agent <integration@trae.ai>
─────────────────────────────────
```

**Checkpoint #3**: Commit onayı

---

## 🎛️ Agent Konfigürasyonu (rules.md)

Trae IDE'de zaten var olan agent rules:

```markdown
# Backend Agent Rules
- Always use parameterized queries
- Entity Framework .Include() for N+1
- [Authorize] for protected endpoints
- Async/await for DB operations

# Frontend Agent Rules
- TypeScript strict mode
- React functional components
- Tailwind for styling
- Lazy load heavy components

# Integration Agent Rules
- CORS: Specific origins only
- Rate limiting: 100 req/min
- Error handling: Retry 3x with backoff
```

Orchestrator bu rules'ları enforce eder.

---

## 🚨 Conflict Resolution

### Senaryo 1: İki Agent Aynı Dosyaya Dokunuyor

```markdown
Conflict:
Backend Agent: UserService.cs (SQL fix)
Integration Agent: UserService.cs (API retry logic)

Çözüm (Architect Guardian):
1. Dependency check → Backend first
2. Backend agent çalışır
3. Integration agent backend'in değişikliklerini görür
4. Integration agent merge eder
5. Test et
```

### Senaryo 2: Breaking Change

```markdown
Problem:
Backend API'de breaking change
Frontend henüz update edilmedi

Çözüm (Architect Guardian):
1. API versioning ekle
   ├─ /api/v1/orders (eski, deprecated)
   └─ /api/v2/orders (yeni)
2. Frontend'i v2'ye geçir
3. v1'i 2 hafta sonra kaldır
```

---

## 📊 Agent Performance Tracking

```markdown
# Agent Performans Raporu

Backend Agent:
├─ Tasks completed: 3
├─ Lines changed: +145 / -78
├─ Tests written: 6
├─ Success rate: 100%
└─ Avg time/task: 42s

Frontend Agent:
├─ Tasks completed: 2
├─ Lines changed: +89 / -123
├─ Tests written: 4
├─ Success rate: 100%
└─ Avg time/task: 38s

Integration Agent:
├─ Tasks completed: 1
├─ Lines changed: +23 / -12
├─ Tests written: 2
├─ Success rate: 100%
└─ Avg time/task: 25s

Architect Guardian:
├─ Conflicts resolved: 0
├─ Rules violations: 0
└─ Coordination time: 15s
```

---

## 🎯 Best Practices

### 1. Agent İletişimi
```
❌ Kötü: Agent'lar birbirinden habersiz çalışır
✅ İyi: Architect Guardian koordine eder
```

### 2. Context Sharing
```
❌ Kötü: Her agent sıfırdan analiz yapar
✅ İyi: Ortak analiz, paylaşılmış context
```

### 3. Testing
```
❌ Kötü: Her agent ayrı test eder
✅ İyi: Integration test + unit test
```

---

## 🔄 Feedback Loop

```markdown
After execution:
├─ Başarı oranı %100 → Agent'lar iyi çalıştı
├─ Başarı oranı <%80 → Analiz:
│   ├─ Hangi agent başarısız?
│   ├─ Neden?
│   └─ Rules.md güncelle
│
└─ Improvement loop
    ├─ Agent rules.md'yi güncelle
    └─ Sonraki execution'da daha iyi
```

---

**Trae IDE agent'larıyla seamless entegrasyon! 🚀**
