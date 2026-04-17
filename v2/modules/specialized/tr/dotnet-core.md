# Module: .NET Core & ASP.NET Analysis

**Priority**: P1 (Teknoloji Stack — .NET Ekosistemi)
**Tokens**: ~1800
**Analysis Time**: `.csproj`, `*.sln` veya `asp.net` tespit edildiğinde otonom yüklenir

---

## Purpose
ASP.NET Core, Entity Framework Core ve Microsoft ekosisteminin best practice'lerini temel alarak projenin mimari sağlığını, EF Core sorgu kalitesini, güvenlik yapılandırmasını ve asenkron kod antipatternlerini analiz eder.

---

## ASP.NET Core Yapısal Analiz

### Katman Ayrımı (Layered Architecture)
Proje içindeki kodun temiz bir katman ayrımına (Separation of Concerns) uyup uymadığı kontrol edilmelidir:

```yaml
layer_structure:
  expected:
    - "Controller → Sadece HTTP request/response yönetimi"
    - "Service Layer → İş mantığı (Business Logic)"
    - "Repository Layer → Veritabanı erişimi (Data Access)"
  antipatterns:
    - "Controller içinde doğrudan DbContext kullanımı"
    - "Repository içine iş mantığı yazılması"
    - "View içinde SQL sorgusu çalıştırılması"
```

### Dependency Injection (DI) Doğruluğu
.NET'in yerleşik DI altyapısının doğru kullanıldığı kontrol edilmelidir:
*   **Scoped vs Singleton:** `DbContext`'in `Singleton` olarak kaydedilmesi kritik bir hatadır.
*   **ServiceLocator antipattern:** `HttpContext.RequestServices.GetService<T>()` kullanımı DI prensibini ihlal eder.

### Middleware Pipeline Değerlendirmesi
`Program.cs` veya `Startup.cs` içerisindeki middleware sıralaması okunup analiz edilmelidir:
*   `app.UseAuthentication()` mutlaka `app.UseAuthorization()`'dan önce gelmeli.
*   Özel (Custom) middleware'ler `try-catch` içermeli.

---

## Entity Framework Core Analizi

### N+1 Query Sorunu (Kritik Performans)
EF Core'da en yaygın ve en maliyetli antipattern, N+1 sorgusudur:

```csharp
// ❌ YANLIŞ: Her Order için ayrı bir SELECT çalışır (N+1)
var orders = context.Orders.ToList();
foreach (var order in orders)
{
    Console.WriteLine(order.Customer.Name); // Lazy loading = N adet extra sorgu
}

// ✅ DOĞRU: Tek bir JOIN sorgusuyla çözülür
var orders = context.Orders.Include(o => o.Customer).ToList();
```

### Migration Yönetimi
*   Migration'ların `pending` olup olmadığı kontrol edilmelidir.
*   Production veritabanına `EnsureCreated()` yerine `Migrate()` kullanılmalıdır.

---

## .NET'e Özgü Güvenlik

```yaml
security_checks:
  authorization:
    - "[Authorize] attribute eksik controller/action'lar tespit edilmeli"
    - "Global AuthorizationFilter'ın kayıtlı olup olmadığı kontrol edilmeli"
  anti_forgery:
    - "Form tabanlı POST işlemlerinde [ValidateAntiForgeryToken] kullanımı"
  cors:
    - "AllowAnyOrigin() production'da ASLA kullanılmamalı"
  secrets:
    - "appsettings.json içindeki connection string'lerin şifreli olup olmadığı"
    - "Secret Manager veya Azure Key Vault kullanımı"
```

---

## Asenkron Kod Antipatternleri (async/await)

.NET'te `async/await` yanlış kullanıldığında performansı düşürmekten öte sistem kilitlenmelerine (Deadlock) yol açabilir:

*   **`.Result` veya `.Wait()` kullanımı:** Asenkron metot üzerinde senkron bekleme yapmak Deadlock'a neden olabilir.
*   **`async void` kullanımı:** Event handler dışında `async void` kullanılmamalıdır; hataları yakalayıp yönetmek imkânsız olur.
*   **`await Task.Run()` içinde `await`:** Gereksiz thread havuzu tüketimi.

---

## Scoring

```yaml
scoring:
  excellent: "Temiz katman ayrımı, N+1 query yok, DI doğru, async/await kusursuz, CORS kısıtlı."
  good: "Genel yapı sağlam, ufak DI hataları veya birkaç lazy loading var."
  attention: "Controller şişkin (Fat Controller), N+1 tespiti var, bazı sayfalar authorize edilmemiş."
  critical: ".Result/.Wait() deadlock riski, AllowAnyOrigin() production'da açık, DbContext Singleton kayıtlı."
```

---

## Output Format

```markdown
## ⚙️ .NET Core / ASP.NET Analiz Raporu

### Mimari (Katman Ayrımı)
- **Durum:** [Açıklama ve Skor]

### Entity Framework Core
- **N+1 Riski:** [Tespit Edilen Yerler]
- **Migration Durumu:** [Pending var mı?]

### Güvenlik
- **[Authorize] Eksiklikleri:** [Controller/Action listesi]
- **CORS:** [Yapılandırma durumu]
```
