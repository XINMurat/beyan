# Güvenlik Sorunları Düzeltme Rehberi

Bu dosya, güvenlik analizi sonucu bulunan sorunları nasıl düzeltece�?inizi adım adım açıklar.

---

## 1. SQL Injection Düzeltme

### �? Sorun �?rne�?i

```csharp
// VULNERABLE: String concatenation
var sql = $"SELECT * FROM Orders WHERE CustomerId = {customerId}";
var orders = _context.Database.ExecuteSqlRaw(sql);
```

### �?? �?özüm: Adım Adım

#### Adım 1: Sorunu Tespit Et

```bash
# Tüm projede SQL injection riski ara
git grep "ExecuteSqlRaw.*+" -r src/
git grep "FromSqlRaw.*+" -r src/
git grep "\$\".*SELECT" -r src/
```

#### Adım 2: Test Yaz (�?nce Test!)

```csharp
[Test]
public void GetOrders_WithMaliciousInput_ShouldNotExecute()
{
    // Arrange
    var maliciousId = "1 OR 1=1; DROP TABLE Orders--";
    
    // Act & Assert
    Assert.Throws<FormatException>(() => 
        orderService.GetOrders(maliciousId)
    );
}
```

#### Adım 3: Kodu Düzelt

```csharp
// �?? SAFE: Parameterized query
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();

// VEYA raw SQL gerekiyorsa:
var orders = _context.Orders
    .FromSqlRaw("SELECT * FROM Orders WHERE CustomerId = {0}", customerId)
    .ToList();
```

#### Adım 4: Test Et

```bash
dotnet test --filter "GetOrders"
```

#### Adım 5: Commit & PR

```bash
git add .
git commit -m "fix: SQL injection vulnerability in OrderService"
git push origin fix/sql-injection
# Pull request aç
```

**Checklist**:
- [ ] Vulnerability tespit edildi
- [ ] Test yazıldı
- [ ] Kod düzeltildi
- [ ] Testler geçti
- [ ] Code review yapıldı
- [ ] Production'a deploy edildi

---

## 2. Exposed Secrets (Git'te Secret) Düzeltme

### �? Sorun

`.env` dosyası Git'e commit edilmi�?, içinde secrets var.

### �?? �?özüm: Adım Adım

#### Adım 1: Git Geçmi�?inden Sil

```bash
# Git history'den tamamen sil
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (DİKKAT: Takıma bildir!)
git push origin --force --all
```

#### Adım 2: Secrets'ları Rotate Et

```bash
# Eski secrets artık public, hepsini de�?i�?tir:
# 1. Database password
# 2. API keys (OpenAI, Stripe, etc.)
# 3. JWT secret
# 4. OAuth client secrets
```

**Her Secret İçin**:
1. Yeni secret olu�?tur
2. Environment variable'a ekle
3. Eski secret'ı revoke et
4. Test et

#### Adım 3: .gitignore Güncelle

```bash
# .gitignore dosyasına ekle
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
echo ".env.production" >> .gitignore
echo "*.pem" >> .gitignore
echo "*.key" >> .gitignore

git add .gitignore
git commit -m "chore: add secrets to .gitignore"
```

#### Adım 4: .env.example Olu�?tur

```bash
# .env.example (template, secret'sız)
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
OPENAI_API_KEY=sk-...your-key-here
JWT_SECRET=your-secret-here
```

```bash
git add .env.example
git commit -m "docs: add .env.example template"
```

#### Adım 5: README Güncelle

```markdown
## Setup

1. Copy environment template:
   ```bash
   cp .env.example .env
   ```

2. Fill in your secrets in `.env`

3. Never commit `.env` to Git!
```

**Checklist**:
- [ ] Secrets Git'ten silindi
- [ ] Tüm secrets rotate edildi
- [ ] .gitignore güncellendi
- [ ] .env.example olu�?turuldu
- [ ] README güncellendi
- [ ] Takıma bilgilendirme yapıldı

---

## 3. Missing Authorization Düzeltme

### �? Sorun

Admin endpoint'lerde authorization check yok.

### �?? �?özüm: Adım Adım

#### Adım 1: Sorunlu Endpoint'leri Bul

```bash
# Authorization attribute olmayan controller'ları bul
grep -r "public.*ActionResult" src/Controllers/ | grep -v "Authorize"
```

#### Adım 2: Authorization Ekle

```csharp
// �? �?ncesi: Authorization yok
[HttpDelete("/api/admin/users/{id}")]
public IActionResult DeleteUser(int id)
{
    _userService.DeleteUser(id);
    return Ok();
}

// �?? Sonrası: Admin role gerekli
[Authorize(Roles = "Admin")]
[HttpDelete("/api/admin/users/{id}")]
public IActionResult DeleteUser(int id)
{
    _logger.LogWarning("Admin {Admin} deleting user {UserId}", 
        User.Identity.Name, id);
    
    _userService.DeleteUser(id);
    return Ok();
}
```

#### Adım 3: Test Yaz

```csharp
[Test]
public async Task DeleteUser_WithoutAdminRole_Returns403()
{
    // Arrange: Non-admin user
    var token = GetNonAdminToken();
    _client.DefaultRequestHeaders.Authorization = 
        new AuthenticationHeaderValue("Bearer", token);
    
    // Act
    var response = await _client.DeleteAsync("/api/admin/users/123");
    
    // Assert
    Assert.Equal(HttpStatusCode.Forbidden, response.StatusCode);
}

[Test]
public async Task DeleteUser_WithAdminRole_Returns200()
{
    // Arrange: Admin user
    var token = GetAdminToken();
    _client.DefaultRequestHeaders.Authorization = 
        new AuthenticationHeaderValue("Bearer", token);
    
    // Act
    var response = await _client.DeleteAsync("/api/admin/users/123");
    
    // Assert
    Assert.Equal(HttpStatusCode.OK, response.StatusCode);
}
```

#### Adım 4: Test Et

```bash
dotnet test --filter "DeleteUser"
```

**Checklist**:
- [ ] Tüm admin endpoint'ler belirlendi
- [ ] Authorization attribute eklendi
- [ ] Logging eklendi
- [ ] Test yazıldı
- [ ] Testler geçti

---

## 4. Vulnerable Dependencies Güncelleme

### �? Sorun

12 vulnerable npm package tespit edildi.

### �?? �?özüm: Adım Adım

#### Adım 1: Audit �?alı�?tır

```bash
npm audit
# veya
npm audit --json > npm-audit.json
```

#### Adım 2: Otomatik Fix Dene

```bash
npm audit fix

# E�?er breaking change varsa:
npm audit fix --force
```

#### Adım 3: Manuel Fix (Otomatik çözemedi�?ini)

```bash
# �?rnek: axios 0.21.1 �?? 1.6.2
npm install axios@1.6.2

# Test et
npm test
```

#### Adım 4: Alternatif Package Ara�?tır

E�?er güncel version yok veya breaking change çok fazla:

```bash
# Alternatif ara
npm search [package-name] alternative

# �?rnek: moment.js �?? date-fns
npm uninstall moment
npm install date-fns
```

#### Adım 5: CI/CD'ye Otomatik Scan Ekle

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run npm audit
        run: npm audit --audit-level=high
```

**Checklist**:
- [ ] npm audit çalı�?tırıldı
- [ ] Critical/High vulnerabilities fix edildi
- [ ] Testler geçti
- [ ] CI/CD'ye scan eklendi

---

## 5. CORS Misconfiguration Düzeltme

### �? Sorun

`AllowAnyOrigin()` kullanılıyor - güvenlik riski.

### �?? �?özüm: Adım Adım

#### Adım 1: Mevcut Konfigürasyonu Bul

```csharp
// Sorunlu kod
builder.Services.AddCors(options => {
    options.AddPolicy("AllowAll", builder => {
        builder.AllowAnyOrigin()
               .AllowAnyMethod()
               .AllowAnyHeader();
    });
});
```

#### Adım 2: Düzelt

```csharp
// appsettings.json
{
  "Cors": {
    "AllowedOrigins": [
      "https://yourdomain.com",
      "https://app.yourdomain.com"
    ]
  }
}

// Program.cs
var allowedOrigins = builder.Configuration
    .GetSection("Cors:AllowedOrigins")
    .Get<string[]>();

builder.Services.AddCors(options => {
    options.AddPolicy("Production", builder => {
        builder.WithOrigins(allowedOrigins)
               .AllowCredentials()
               .AllowMethods("GET", "POST", "PUT", "DELETE")
               .AllowHeaders("Authorization", "Content-Type");
    });
});

app.UseCors("Production");
```

#### Adım 3: Test Et

```bash
# Frontend'den API'ye istek at
curl -H "Origin: https://yourdomain.com" \
     -H "Access-Control-Request-Method: POST" \
     -X OPTIONS https://api.yourdomain.com/api/users

# Response'da Access-Control-Allow-Origin header'ı olmalı
```

**Checklist**:
- [ ] Allowed origins belirlendi
- [ ] CORS policy güncellendi
- [ ] Test edildi (frontend + backend)
- [ ] Production'da deploy edildi

---

## 6. Weak Password Hashing Düzeltme

### �? Sorun

SHA256 kullanılıyor (brute force riski).

### �?? �?özüm: Adım Adım

#### Adım 1: Bcrypt Package Ekle

```bash
dotnet add package BCrypt.Net-Next
```

#### Adım 2: Yeni Hash Fonksiyonu

```csharp
using BCrypt.Net;

public class AuthService
{
    // Yeni password hash
    public string HashPassword(string password)
    {
        return BCrypt.HashPassword(password, workFactor: 12);
    }
    
    // Password verify
    public bool VerifyPassword(string password, string hash)
    {
        return BCrypt.Verify(password, hash);
    }
}
```

#### Adım 3: Migration Stratejisi

```csharp
// Users tablosuna yeni column ekle
public class User
{
    public string PasswordHash { get; set; }  // Eski (SHA256)
    public string PasswordHashV2 { get; set; }  // Yeni (Bcrypt)
    public int HashVersion { get; set; }  // 1: SHA256, 2: Bcrypt
}

// Login sırasında lazy migration
public async Task<bool> LoginAsync(string email, string password)
{
    var user = await _context.Users.FirstOrDefaultAsync(u => u.Email == email);
    
    if (user.HashVersion == 1)  // Eski hash
    {
        // SHA256 ile verify
        if (VerifyOldHash(password, user.PasswordHash))
        {
            // Do�?ru password, yeni hash'e upgrade et
            user.PasswordHashV2 = BCrypt.HashPassword(password);
            user.HashVersion = 2;
            await _context.SaveChangesAsync();
            return true;
        }
    }
    else  // Yeni hash
    {
        return BCrypt.Verify(password, user.PasswordHashV2);
    }
    
    return false;
}
```

#### Adım 4: Test Et

```csharp
[Test]
public void HashPassword_ShouldGenerateBcryptHash()
{
    var password = "MyPassword123!";
    var hash = _authService.HashPassword(password);
    
    Assert.That(hash, Does.StartWith("$2"));  // Bcrypt format
    Assert.True(_authService.VerifyPassword(password, hash));
}
```

**Checklist**:
- [ ] Bcrypt package eklendi
- [ ] Yeni hash fonksiyonu yazıldı
- [ ] Migration stratejisi belirlendi
- [ ] Test yazıldı
- [ ] Kullanıcılara bilgi verildi (de�?i�?iklik yok)

---

## �??? Genel Güvenlik Best Practices

### Her PR'de Kontrol Et

- [ ] Yeni secrets hardcoded de�?il mi?
- [ ] User input validate ediliyor mu?
- [ ] Authorization check var mı?
- [ ] Error mesajları hassas bilgi sızdırmıyor mu?
- [ ] Logging'de PII yok mu?

### Otomatik Security Scan

```yaml
# .github/workflows/security.yml
name: Security
on: [push, pull_request]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run Trivy (container scan)
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          severity: 'CRITICAL,HIGH'
      
      - name: Run npm audit
        run: npm audit --audit-level=high
      
      - name: Run Semgrep (SAST)
        uses: returntocorp/semgrep-action@v1
```

---

## �??? Referanslar

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [Bcrypt Documentation](https://github.com/BcryptNet/bcrypt.net)
- [ASP.NET Core Security](https://docs.microsoft.com/en-us/aspnet/core/security/)

---

**Son Güncelleme**: Aralık 2024
