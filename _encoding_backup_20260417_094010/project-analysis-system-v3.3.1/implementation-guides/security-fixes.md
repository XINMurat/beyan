# GÃ¼venlik SorunlarÄ± DÃ¼zeltme Rehberi

Bu dosya, gÃ¼venlik analizi sonucu bulunan sorunlarÄ± nasÄ±l dÃ¼zelteceÄŸinizi adÄ±m adÄ±m aÃ§Ä±klar.

---

## 1. SQL Injection DÃ¼zeltme

### âŒ Sorun Ã–rneÄŸi

```csharp
// VULNERABLE: String concatenation
var sql = $"SELECT * FROM Orders WHERE CustomerId = {customerId}";
var orders = _context.Database.ExecuteSqlRaw(sql);
```

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Sorunu Tespit Et

```bash
# TÃ¼m projede SQL injection riski ara
git grep "ExecuteSqlRaw.*+" -r src/
git grep "FromSqlRaw.*+" -r src/
git grep "\$\".*SELECT" -r src/
```

#### AdÄ±m 2: Test Yaz (Ã–nce Test!)

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

#### AdÄ±m 3: Kodu DÃ¼zelt

```csharp
// âœ… SAFE: Parameterized query
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();

// VEYA raw SQL gerekiyorsa:
var orders = _context.Orders
    .FromSqlRaw("SELECT * FROM Orders WHERE CustomerId = {0}", customerId)
    .ToList();
```

#### AdÄ±m 4: Test Et

```bash
dotnet test --filter "GetOrders"
```

#### AdÄ±m 5: Commit & PR

```bash
git add .
git commit -m "fix: SQL injection vulnerability in OrderService"
git push origin fix/sql-injection
# Pull request aÃ§
```

**Checklist**:
- [ ] Vulnerability tespit edildi
- [ ] Test yazÄ±ldÄ±
- [ ] Kod dÃ¼zeltildi
- [ ] Testler geÃ§ti
- [ ] Code review yapÄ±ldÄ±
- [ ] Production'a deploy edildi

---

## 2. Exposed Secrets (Git'te Secret) DÃ¼zeltme

### âŒ Sorun

`.env` dosyasÄ± Git'e commit edilmiÅŸ, iÃ§inde secrets var.

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Git GeÃ§miÅŸinden Sil

```bash
# Git history'den tamamen sil
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (DÄ°KKAT: TakÄ±ma bildir!)
git push origin --force --all
```

#### AdÄ±m 2: Secrets'larÄ± Rotate Et

```bash
# Eski secrets artÄ±k public, hepsini deÄŸiÅŸtir:
# 1. Database password
# 2. API keys (OpenAI, Stripe, etc.)
# 3. JWT secret
# 4. OAuth client secrets
```

**Her Secret Ä°Ã§in**:
1. Yeni secret oluÅŸtur
2. Environment variable'a ekle
3. Eski secret'Ä± revoke et
4. Test et

#### AdÄ±m 3: .gitignore GÃ¼ncelle

```bash
# .gitignore dosyasÄ±na ekle
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
echo ".env.production" >> .gitignore
echo "*.pem" >> .gitignore
echo "*.key" >> .gitignore

git add .gitignore
git commit -m "chore: add secrets to .gitignore"
```

#### AdÄ±m 4: .env.example OluÅŸtur

```bash
# .env.example (template, secret'sÄ±z)
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
OPENAI_API_KEY=sk-...your-key-here
JWT_SECRET=your-secret-here
```

```bash
git add .env.example
git commit -m "docs: add .env.example template"
```

#### AdÄ±m 5: README GÃ¼ncelle

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
- [ ] TÃ¼m secrets rotate edildi
- [ ] .gitignore gÃ¼ncellendi
- [ ] .env.example oluÅŸturuldu
- [ ] README gÃ¼ncellendi
- [ ] TakÄ±ma bilgilendirme yapÄ±ldÄ±

---

## 3. Missing Authorization DÃ¼zeltme

### âŒ Sorun

Admin endpoint'lerde authorization check yok.

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Sorunlu Endpoint'leri Bul

```bash
# Authorization attribute olmayan controller'larÄ± bul
grep -r "public.*ActionResult" src/Controllers/ | grep -v "Authorize"
```

#### AdÄ±m 2: Authorization Ekle

```csharp
// âŒ Ã–ncesi: Authorization yok
[HttpDelete("/api/admin/users/{id}")]
public IActionResult DeleteUser(int id)
{
    _userService.DeleteUser(id);
    return Ok();
}

// âœ… SonrasÄ±: Admin role gerekli
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

#### AdÄ±m 3: Test Yaz

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

#### AdÄ±m 4: Test Et

```bash
dotnet test --filter "DeleteUser"
```

**Checklist**:
- [ ] TÃ¼m admin endpoint'ler belirlendi
- [ ] Authorization attribute eklendi
- [ ] Logging eklendi
- [ ] Test yazÄ±ldÄ±
- [ ] Testler geÃ§ti

---

## 4. Vulnerable Dependencies GÃ¼ncelleme

### âŒ Sorun

12 vulnerable npm package tespit edildi.

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Audit Ã‡alÄ±ÅŸtÄ±r

```bash
npm audit
# veya
npm audit --json > npm-audit.json
```

#### AdÄ±m 2: Otomatik Fix Dene

```bash
npm audit fix

# EÄŸer breaking change varsa:
npm audit fix --force
```

#### AdÄ±m 3: Manuel Fix (Otomatik Ã§Ã¶zemediÄŸini)

```bash
# Ã–rnek: axios 0.21.1 â†’ 1.6.2
npm install axios@1.6.2

# Test et
npm test
```

#### AdÄ±m 4: Alternatif Package AraÅŸtÄ±r

EÄŸer gÃ¼ncel version yok veya breaking change Ã§ok fazla:

```bash
# Alternatif ara
npm search [package-name] alternative

# Ã–rnek: moment.js â†’ date-fns
npm uninstall moment
npm install date-fns
```

#### AdÄ±m 5: CI/CD'ye Otomatik Scan Ekle

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
- [ ] npm audit Ã§alÄ±ÅŸtÄ±rÄ±ldÄ±
- [ ] Critical/High vulnerabilities fix edildi
- [ ] Testler geÃ§ti
- [ ] CI/CD'ye scan eklendi

---

## 5. CORS Misconfiguration DÃ¼zeltme

### âŒ Sorun

`AllowAnyOrigin()` kullanÄ±lÄ±yor - gÃ¼venlik riski.

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Mevcut KonfigÃ¼rasyonu Bul

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

#### AdÄ±m 2: DÃ¼zelt

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

#### AdÄ±m 3: Test Et

```bash
# Frontend'den API'ye istek at
curl -H "Origin: https://yourdomain.com" \
     -H "Access-Control-Request-Method: POST" \
     -X OPTIONS https://api.yourdomain.com/api/users

# Response'da Access-Control-Allow-Origin header'Ä± olmalÄ±
```

**Checklist**:
- [ ] Allowed origins belirlendi
- [ ] CORS policy gÃ¼ncellendi
- [ ] Test edildi (frontend + backend)
- [ ] Production'da deploy edildi

---

## 6. Weak Password Hashing DÃ¼zeltme

### âŒ Sorun

SHA256 kullanÄ±lÄ±yor (brute force riski).

### âœ… Ã‡Ã¶zÃ¼m: AdÄ±m AdÄ±m

#### AdÄ±m 1: Bcrypt Package Ekle

```bash
dotnet add package BCrypt.Net-Next
```

#### AdÄ±m 2: Yeni Hash Fonksiyonu

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

#### AdÄ±m 3: Migration Stratejisi

```csharp
// Users tablosuna yeni column ekle
public class User
{
    public string PasswordHash { get; set; }  // Eski (SHA256)
    public string PasswordHashV2 { get; set; }  // Yeni (Bcrypt)
    public int HashVersion { get; set; }  // 1: SHA256, 2: Bcrypt
}

// Login sÄ±rasÄ±nda lazy migration
public async Task<bool> LoginAsync(string email, string password)
{
    var user = await _context.Users.FirstOrDefaultAsync(u => u.Email == email);
    
    if (user.HashVersion == 1)  // Eski hash
    {
        // SHA256 ile verify
        if (VerifyOldHash(password, user.PasswordHash))
        {
            // DoÄŸru password, yeni hash'e upgrade et
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

#### AdÄ±m 4: Test Et

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
- [ ] Yeni hash fonksiyonu yazÄ±ldÄ±
- [ ] Migration stratejisi belirlendi
- [ ] Test yazÄ±ldÄ±
- [ ] KullanÄ±cÄ±lara bilgi verildi (deÄŸiÅŸiklik yok)

---

## ðŸ”’ Genel GÃ¼venlik Best Practices

### Her PR'de Kontrol Et

- [ ] Yeni secrets hardcoded deÄŸil mi?
- [ ] User input validate ediliyor mu?
- [ ] Authorization check var mÄ±?
- [ ] Error mesajlarÄ± hassas bilgi sÄ±zdÄ±rmÄ±yor mu?
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

## ðŸ“š Referanslar

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [Bcrypt Documentation](https://github.com/BcryptNet/bcrypt.net)
- [ASP.NET Core Security](https://docs.microsoft.com/en-us/aspnet/core/security/)

---

**Son GÃ¼ncelleme**: AralÄ±k 2024
