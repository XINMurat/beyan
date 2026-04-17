# Module: Security Analysis

**Priority**: P1 (High - Critical for Production)  
**Tokens**: ~2800  
**Analysis Time**: 15-20 minutes  

---

## Purpose

Comprehensive security audit covering authentication, authorization, input validation, dependency vulnerabilities, secrets management, common attack vectors (OWASP Top 10), and security best practices.

---

## Security Dimensions

### 1. Authentication & Authorization

```yaml
authentication_checks:
  secure_storage:
    passwords: "Bcrypt, Argon2, PBKDF2 (NOT MD5, SHA1)"
    tokens: "JWT with proper expiration, signed"
    sessions: "HttpOnly, Secure, SameSite cookies"
    
  common_vulnerabilities:
    - Plain text passwords
    - Weak hashing (MD5, SHA1)
    - No rate limiting on login
    - Missing MFA support
    - Predictable session IDs

authorization:
  principle: "Least privilege - deny by default"
  checks:
    - Role-based access control (RBAC)
    - Attribute-based access control (ABAC)
    - JWT claims validation
    - API key security
    - Missing authorization checks
  
  anti_patterns:
    - "❌ Client-side only authorization checks"
    - "❌ Trusting user input for permissions"
    - "❌ No permission check on sensitive endpoints"

confidence: "high_92%"
```

**Detection Scripts**:
```bash
# Find password hashing
grep -r "MD5\|SHA1\|sha1" src/ --include="*.cs" --include="*.ts"

# Find JWT without expiration
grep -r "GenerateToken\|jwt.sign" src/ | grep -v "expiresIn"

# Find authorization decorators
grep -r "@Authorize\|[Authorize]" src/ controllers/
```

### 2. Input Validation & Injection Prevention

```yaml
sql_injection:
  vulnerable: "String concatenation in queries"
  safe: "Parameterized queries, ORM"
  
  detection:
    csharp: |
      // ❌ Vulnerable
      var sql = $"SELECT * FROM Users WHERE Username = '{username}'";
      
      // ✅ Safe
      var user = _context.Users.FirstOrDefault(u => u.Username == username);
  
  confidence: "high_95%"

xss_prevention:
  output_encoding: "Always encode user input in HTML"
  csp: "Content-Security-Policy headers"
  
  detection:
    react: |
      // ❌ Vulnerable
      <div dangerouslySetInnerHTML={{__html: userInput}} />
      
      // ✅ Safe
      <div>{userInput}</div>  // React auto-escapes
  
  confidence: "high_90%"

command_injection:
  vulnerable: "Unvalidated input in shell commands"
  detection:
    nodejs: |
      // ❌ Vulnerable
      exec(`ping ${userInput}`)
      
      // ✅ Safe
      execFile('ping', [userInput])
  
  confidence: "high_92%"

path_traversal:
  vulnerable: "User input in file paths"
  detection:
    csharp: |
      // ❌ Vulnerable
      File.ReadAllText($"uploads/{filename}")
      
      // ✅ Safe
      var safePath = Path.GetFileName(filename);
      File.ReadAllText(Path.Combine("uploads", safePath))
  
  confidence: "high_95%"
```

### 3. Dependency Vulnerabilities

```yaml
scanning_tools:
  npm: "npm audit"
  dotnet: "dotnet list package --vulnerable"
  python: "pip-audit or safety"
  
severity_levels:
  critical: "Immediate patch required"
  high: "Patch within 1 week"
  moderate: "Patch within 1 month"
  low: "Patch when convenient"

automated_checks:
  command: |
    # NPM
    npm audit --json > npm-audit.json
    
    # .NET
    dotnet list package --vulnerable --include-transitive
    
    # Python
    pip-audit --format json > pip-audit.json
  
  confidence: "high_98%"  # Tool-based, highly reliable
```

### 4. Secrets Management

```yaml
secrets_detection:
  patterns:
    - API keys (AWS, OpenAI, Stripe)
    - Database connection strings
    - Private keys, certificates
    - JWT secrets
    - OAuth tokens
  
  tools:
    - git-secrets
    - truffleHog
    - gitleaks
  
  common_mistakes:
    - "❌ Secrets in .env committed to Git"
    - "❌ API keys hardcoded in source"
    - "❌ Passwords in config files"
    - "❌ Secrets in client-side code"
  
  best_practices:
    - "✅ Azure Key Vault, AWS Secrets Manager"
    - "✅ Environment variables (not committed)"
    - "✅ .env.example (template without secrets)"
    - "✅ Secrets rotation policy"

confidence: "high_93%"
```

**Detection Script**:
```bash
# Find potential secrets
git grep -E "api[_-]?key|secret|password|token" -- '*.cs' '*.ts' '*.js' '*.py' | \
  grep -v "// Safe comment" | \
  grep -v "password:" | \
  head -20

# Check for committed .env
git log --all --full-history -- ".env"

# Scan with truffleHog
truffleHog git file://. --json --regex --entropy=False
```

### 5. CORS & CSRF Protection

```yaml
cors:
  dangerous: "Access-Control-Allow-Origin: *"
  safe: "Specific origins, credentials handling"
  
  detection:
    csharp: |
      // ❌ Dangerous
      builder.Services.AddCors(options => {
        options.AddPolicy("AllowAll", builder => {
          builder.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader();
        });
      });
      
      // ✅ Safe
      builder.Services.AddCors(options => {
        options.AddPolicy("Production", builder => {
          builder.WithOrigins("https://yourdomain.com")
                 .AllowCredentials()
                 .AllowMethods("GET", "POST");
        });
      });

csrf:
  protection: "Anti-CSRF tokens for state-changing operations"
  requirement: "All POST, PUT, DELETE, PATCH"
  
  frameworks:
    aspnet: "[ValidateAntiForgeryToken] attribute"
    react: "Include CSRF token in headers"

confidence: "high_88%"
```

### 6. Logging & Monitoring

```yaml
security_logging:
  must_log:
    - Authentication attempts (success/failure)
    - Authorization failures
    - Input validation errors
    - Security exceptions
  
  must_not_log:
    - Passwords (plain or hashed)
    - Credit card numbers
    - Personal identification numbers
    - Session tokens
  
  pii_detection:
    patterns: "Email, SSN, credit cards in logs"
    tools: "Log analysis, regex patterns"

confidence: "high_90%"
```

### 7. HTTPS & TLS

```yaml
checks:
  https_enforcement:
    redirect: "HTTP → HTTPS automatic"
    hsts: "Strict-Transport-Security header"
    
  tls_version:
    minimum: "TLS 1.2"
    recommended: "TLS 1.3"
    avoid: "TLS 1.0, TLS 1.1, SSL"
  
  certificate:
    validation: "Valid, not expired, proper CN"
    best_practice: "Let's Encrypt (free, auto-renew)"

detection:
  csharp: |
    // Check for HTTPS redirect
    app.UseHttpsRedirection();
    
    // Check for HSTS
    app.UseHsts();

confidence: "high_95%"
```

### 8. File Upload Security

```yaml
vulnerabilities:
  unrestricted_upload:
    risk: "Upload executable files (.exe, .dll, .php)"
    fix: "Whitelist allowed extensions"
  
  no_size_limit:
    risk: "DoS via large files"
    fix: "Max 10 MB for images, adjust per need"
  
  stored_in_webroot:
    risk: "Direct execution of uploaded scripts"
    fix: "Store outside webroot, serve via controller"
  
  no_virus_scan:
    risk: "Malware distribution"
    fix: "ClamAV or cloud scanning service"

best_practices: |
  1. Whitelist file types (not blacklist)
  2. Rename files (don't trust user filename)
  3. Validate file content (not just extension)
  4. Store outside webroot
  5. Scan with antivirus
  6. Set size limits
  7. Generate unique filenames (GUID)

confidence: "high_92%"
```

### 9. API Security

```yaml
rate_limiting:
  requirement: "Prevent brute force, DoS"
  implementation: "AspNetCoreRateLimit, express-rate-limit"
  
  typical_limits:
    public_endpoint: "100 req/min per IP"
    authenticated: "1000 req/min per user"
    login: "5 attempts per 15 min"

api_keys:
  storage: "Hashed in database (like passwords)"
  transmission: "HTTPS only, in headers"
  rotation: "Support key rotation"

confidence: "high_88%"
```

### 10. Known Attack Patterns

```yaml
owasp_top_10_2021:
  A01_broken_access: "Authorization bypass"
  A02_crypto_failures: "Weak encryption, exposed data"
  A03_injection: "SQL, NoSQL, OS command injection"
  A04_insecure_design: "Missing security requirements"
  A05_security_misconfiguration: "Default configs, verbose errors"
  A06_vulnerable_components: "Outdated dependencies"
  A07_identification_auth: "Weak auth, session management"
  A08_integrity_failures: "Unsigned code, CI/CD issues"
  A09_security_logging: "Missing logs, monitoring"
  A10_ssrf: "Server-Side Request Forgery"
```

---

## Analysis Protocol

### Step 1: Automated Scans (5 min)

```bash
#!/bin/bash
# Comprehensive security scan

echo "=== Dependency Vulnerabilities ==="
npm audit --json > npm-audit.json
dotnet list package --vulnerable

echo "=== Secrets Detection ==="
truffleHog git file://. --json --regex > secrets.json

echo "=== Static Analysis ==="
# Find SQL injection patterns
grep -rn "ExecuteRaw\|FromSql.*+\|QueryAsync.*+" src/

# Find XSS vectors
grep -rn "dangerouslySetInnerHTML\|innerHTML\|document.write" src/

# Find hardcoded secrets
git grep -E "password\s*=\s*['\"][^'\"]{5,}" -- '*.cs' '*.ts'

echo "=== CORS Configuration ==="
grep -rn "AllowAnyOrigin\|AllowAnyHeader" src/
```

### Step 2: Manual Review (10 min)

```yaml
authentication:
  - [ ] Password hashing (Bcrypt/Argon2)
  - [ ] JWT expiration set
  - [ ] Session security (HttpOnly, Secure, SameSite)
  - [ ] Rate limiting on login

authorization:
  - [ ] All endpoints have authorization checks
  - [ ] Role checks server-side (not client-only)
  - [ ] Principle of least privilege

input_validation:
  - [ ] All user input validated
  - [ ] Parameterized queries (no string concat)
  - [ ] File upload restrictions

secrets:
  - [ ] No secrets in code
  - [ ] .env not in Git
  - [ ] Environment-based config

security_headers:
  - [ ] HTTPS enforced
  - [ ] HSTS header
  - [ ] CSP header
  - [ ] X-Frame-Options
```

### Step 3: Generate Report

```markdown
# Security Analysis Report

## Risk Level: 🟡 Medium (3 Critical, 5 High)

### Executive Summary
- 🔴 Critical: 3 issues requiring immediate fix
- 🟡 High: 5 issues to address this sprint
- 🟢 Medium: 8 improvements recommended
- ✅ Good: Authentication, HTTPS enforced

**Overall Security Posture**: 6.5/10 (Needs Improvement)

---

## Critical Findings (P0)

### 1. 🔴 SQL Injection Vulnerability

**Location**: `OrderService.cs:45`

```csharp
// CRITICAL VULNERABILITY
var sql = $"SELECT * FROM Orders WHERE CustomerId = {customerId}";
var orders = _context.Orders.FromSqlRaw(sql).ToList();
```

**Risk**: 
- Severity: **CRITICAL**
- Exploitability: **Easy** (single HTTP request)
- Impact: **Complete database compromise**
- CVSS Score: **9.8/10**

**Exploit Example**:
```http
GET /api/orders?customerId=1 OR 1=1; DROP TABLE Orders--
```

**Fix** (15 minutes):
```csharp
// ✅ Safe: Parameterized query
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();

// OR with FromSqlRaw (if raw SQL needed)
var orders = _context.Orders
    .FromSqlRaw("SELECT * FROM Orders WHERE CustomerId = {0}", customerId)
    .ToList();
```

**Testing**:
```csharp
[Test]
public void Should_Reject_SQL_Injection() {
    var maliciousInput = "1 OR 1=1; DROP TABLE Orders--";
    
    // Should throw or return empty, not execute DROP
    Assert.Throws<FormatException>(() => 
        orderService.GetOrders(maliciousInput)
    );
}
```

**Confidence**: High (98%)

---

### 2. 🔴 Secrets Committed to Git

**Location**: `.env` file in commit history

```bash
# Found in commit: abc123 (2024-11-15)
DB_PASSWORD=SuperSecret123!
OPENAI_API_KEY=sk-proj-...
JWT_SECRET=my-secret-key
```

**Risk**:
- Public exposure if repo leaked
- API key abuse ($$$)
- Database compromise

**Remediation** (30 minutes):

1. **Rotate ALL secrets immediately**:
   ```bash
   # Database password
   # OpenAI API key
   # JWT secret
   ```

2. **Remove from Git history**:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   
   git push origin --force --all
   ```

3. **Add to .gitignore**:
   ```gitignore
   .env
   .env.local
   .env.production
   *.pem
   *.key
   ```

4. **Use secure storage**:
   ```csharp
   // Azure Key Vault
   var client = new SecretClient(new Uri(keyVaultUrl), new DefaultAzureCredential());
   var dbPassword = await client.GetSecretAsync("DbPassword");
   ```

**Confidence**: High (100%) - Verified in Git history

---

### 3. 🔴 Missing Authorization on Admin Endpoints

**Location**: `AdminController.cs`

```csharp
// ❌ NO AUTHORIZATION CHECK
[HttpDelete("/api/admin/users/{id}")]
public IActionResult DeleteUser(int id) {
    _userService.DeleteUser(id);
    return Ok();
}
```

**Risk**:
- Anyone can delete users
- No audit trail
- Severity: **CRITICAL**

**Fix** (5 minutes):
```csharp
// ✅ Require Admin role
[Authorize(Roles = "Admin")]
[HttpDelete("/api/admin/users/{id}")]
public IActionResult DeleteUser(int id) {
    _logger.LogWarning("Admin {Admin} deleting user {UserId}", 
        User.Identity.Name, id);
    _userService.DeleteUser(id);
    return Ok();
}
```

**Test**:
```csharp
[Test]
public async Task DeleteUser_WithoutAdminRole_Returns403() {
    // Setup non-admin user
    var response = await client.DeleteAsync("/api/admin/users/123");
    
    Assert.Equal(HttpStatusCode.Forbidden, response.StatusCode);
}
```

**Confidence**: High (95%)

---

## High Priority (P1)

### 4. 🟡 Vulnerable Dependencies (12 packages)

**NPM Audit Results**:
```json
{
  "critical": 2,
  "high": 4,
  "moderate": 6,
  "total": 12
}
```

**Critical Vulnerabilities**:

1. **axios@0.21.1** → Upgrade to **1.6.2**
   - CVE-2023-45857: SSRF vulnerability
   - Severity: Critical (9.1 CVSS)
   - Effort: 5 minutes
   ```bash
   npm update axios
   ```

2. **express@4.17.1** → Upgrade to **4.18.2**
   - CVE-2022-24999: Open redirect
   - Severity: High (7.5 CVSS)
   - Effort: 10 minutes (test routes)

**Fix All**:
```bash
npm audit fix --force
# Test thoroughly after upgrade
```

**Confidence**: High (98%) - Tool-detected

---

### 5. 🟡 CORS Allows All Origins

**Location**: `Program.cs:23`

```csharp
// ❌ DANGEROUS
builder.Services.AddCors(options => {
    options.AddPolicy("AllowAll", builder => {
        builder.AllowAnyOrigin()
               .AllowAnyMethod()
               .AllowAnyHeader();
    });
});
```

**Risk**:
- Any website can call your API
- Credential theft possible
- CSRF attacks

**Fix** (10 minutes):
```csharp
// ✅ Specific origins only
builder.Services.AddCors(options => {
    options.AddPolicy("Production", builder => {
        builder.WithOrigins(
                   "https://yourdomain.com",
                   "https://app.yourdomain.com"
               )
               .AllowCredentials()
               .AllowMethods("GET", "POST", "PUT", "DELETE")
               .AllowHeaders("Authorization", "Content-Type");
    });
});

app.UseCors("Production");
```

**Confidence**: High (95%)

---

### 6. 🟡 Missing Rate Limiting

**Location**: Login endpoint, public APIs

**Risk**:
- Brute force attacks on login
- API abuse / DoS
- Resource exhaustion

**Implementation** (30 minutes):

1. **Install package**:
   ```bash
   dotnet add package AspNetCoreRateLimit
   ```

2. **Configure**:
   ```csharp
   // appsettings.json
   {
     "IpRateLimiting": {
       "EnableEndpointRateLimiting": true,
       "GeneralRules": [
         {
           "Endpoint": "*",
           "Period": "1m",
           "Limit": 100
         },
         {
           "Endpoint": "*:/api/auth/login",
           "Period": "15m",
           "Limit": 5
         }
       ]
     }
   }
   
   // Program.cs
   builder.Services.AddMemoryCache();
   builder.Services.Configure<IpRateLimitOptions>(
       builder.Configuration.GetSection("IpRateLimiting"));
   builder.Services.AddInMemoryRateLimiting();
   builder.Services.AddSingleton<IRateLimitConfiguration, RateLimitConfiguration>();
   
   app.UseIpRateLimiting();
   ```

**Confidence**: High (90%)

---

### 7. 🟡 Passwords Not Properly Hashed

**Location**: `AuthService.cs:67`

```csharp
// ❌ Weak: SHA256 is fast (brute-forceable)
using var sha256 = SHA256.Create();
var hashBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
var hash = Convert.ToBase64String(hashBytes);
```

**Risk**:
- Rainbow table attacks
- Fast brute forcing (billions of hashes/sec)

**Fix** (20 minutes):
```csharp
// ✅ Strong: Bcrypt (slow by design)
using BCrypt.Net;

// Hash password
var hash = BCrypt.HashPassword(password, workFactor: 12);

// Verify password
bool isValid = BCrypt.Verify(password, hash);
```

**Migration Plan**:
1. Add `PasswordHashVersion` column to Users table
2. On next login, rehash with Bcrypt
3. Support both temporarily (6 months)
4. Force password reset for inactive users

**Confidence**: High (95%)

---

### 8. 🟡 Sensitive Data in Logs

**Location**: Multiple files

```csharp
// ❌ Logging password!
_logger.LogInformation("User login attempt: {Email}, {Password}", email, password);

// ❌ Logging credit card
_logger.LogError("Payment failed for card: {CardNumber}", cardNumber);
```

**Risk**:
- PII exposure
- GDPR/CCPA violations
- Log aggregation services see secrets

**Fix** (1 hour):
```csharp
// ✅ Safe logging
_logger.LogInformation("User login attempt: {Email}", email);
// Password NEVER logged

_logger.LogError("Payment failed for card: ****{Last4}", 
    cardNumber.Substring(cardNumber.Length - 4));

// Or use structured logging with PII redaction
public class SensitiveData {
    public string Email { get; set; }
    [NotLogged]
    public string Password { get; set; }
}
```

**Audit**:
```bash
# Find password logging
grep -rn "LogInformation.*[Pp]assword" src/
grep -rn "LogError.*token\|secret" src/
```

**Confidence**: High (92%)

---

## Medium Priority (P2)

### 9. 🟢 Missing Security Headers

**Current Response Headers**:
```http
HTTP/1.1 200 OK
Content-Type: application/json
```

**Missing**:
- `Strict-Transport-Security` (HSTS)
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Content-Security-Policy`
- `Referrer-Policy`

**Fix** (15 minutes):
```csharp
// Program.cs
app.Use(async (context, next) => {
    context.Response.Headers.Add("X-Content-Type-Options", "nosniff");
    context.Response.Headers.Add("X-Frame-Options", "DENY");
    context.Response.Headers.Add("X-XSS-Protection", "1; mode=block");
    context.Response.Headers.Add("Referrer-Policy", "strict-origin-when-cross-origin");
    context.Response.Headers.Add("Content-Security-Policy", 
        "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'");
    
    await next();
});

// HSTS (only in production)
if (app.Environment.IsProduction()) {
    app.UseHsts();
}
```

**Test**:
```bash
curl -I https://yourapi.com/api/users
# Verify headers present
```

**Confidence**: High (95%)

---

## Recommendations Summary

### 🔴 P0 - Fix Immediately (Before Next Deployment)

| Issue | Effort | Impact | Confidence |
|-------|--------|--------|------------|
| SQL Injection | 15 min | Critical | 98% |
| Rotate exposed secrets | 30 min | Critical | 100% |
| Add authorization checks | 5 min | Critical | 95% |

**Total P0 Effort**: 50 minutes  
**Must complete before production deployment**

### 🟡 P1 - Fix This Sprint

| Issue | Effort | Impact | Confidence |
|-------|--------|--------|------------|
| Update vulnerable deps | 15 min | High | 98% |
| Fix CORS policy | 10 min | High | 95% |
| Add rate limiting | 30 min | High | 90% |
| Fix password hashing | 20 min | High | 95% |
| Remove PII from logs | 60 min | High | 92% |

**Total P1 Effort**: 2 hours 15 minutes

### 🟢 P2 - Next Month

| Issue | Effort | Impact | Confidence |
|-------|--------|--------|------------|
| Add security headers | 15 min | Medium | 95% |
| Implement file upload limits | 30 min | Medium | 90% |
| Add CSRF protection | 45 min | Medium | 88% |

---

## Testing Checklist

```yaml
before_fix:
  - [ ] Document current vulnerabilities
  - [ ] Create exploit POCs (for testing)
  - [ ] Backup database

after_fix:
  - [ ] Run automated security tests
  - [ ] Verify exploits no longer work
  - [ ] Penetration testing (if available)
  - [ ] Update threat model
  
continuous:
  - [ ] Enable Dependabot / Renovate
  - [ ] Add security tests to CI/CD
  - [ ] Schedule quarterly security reviews
```

---

## Tools & Resources

```yaml
vulnerability_scanning:
  - npm audit / dotnet list package --vulnerable
  - Snyk (free tier)
  - GitHub Dependabot

secrets_detection:
  - truffleHog
  - git-secrets
  - gitleaks

static_analysis:
  - Semgrep
  - SonarQube
  - Checkmarx (enterprise)

penetration_testing:
  - OWASP ZAP
  - Burp Suite
  - Metasploit

learning:
  - OWASP Top 10: https://owasp.org/www-project-top-ten/
  - CWE Top 25: https://cwe.mitre.org/top25/
  - NIST Cybersecurity Framework
```

---

## Compliance Considerations

```yaml
gdpr_kvkk:
  - [ ] Encrypt PII at rest and in transit
  - [ ] Implement right to erasure (delete user data)
  - [ ] Data breach notification process
  - [ ] Privacy policy and consent

pci_dss: # If handling credit cards
  - [ ] Never store CVV
  - [ ] Encrypt cardholder data
  - [ ] Use tokenization service (Stripe, Square)
  - [ ] Maintain access logs

hipaa: # If handling health data
  - [ ] Encrypt all PHI
  - [ ] Implement audit logging
  - [ ] Access controls
  - [ ] Business Associate Agreements
```

---

## Incident Response Plan

```yaml
if_breach_detected:
  immediate (0-1 hour):
    - Isolate affected systems
    - Disable compromised accounts
    - Notify security team
    
  short_term (1-24 hours):
    - Assess scope of breach
    - Preserve evidence
    - Implement temporary fixes
    - Notify affected users (if required)
    
  long_term (1-7 days):
    - Root cause analysis
    - Permanent fixes
    - Update security policies
    - Post-mortem review
```

---

## Success Metrics

```yaml
immediate (1 week):
  - P0 vulnerabilities: 3 → 0
  - Secrets in Git: Rotated
  - SQL injection: Fixed

short_term (1 month):
  - P1 vulnerabilities: 5 → 0
  - Automated security tests: Added
  - Security headers: Implemented

long_term (3 months):
  - Security score: 6.5 → 9.0
  - Zero critical vulnerabilities
  - Automated dependency updates
  - Quarterly penetration tests scheduled
```

---

**Analysis Complete** | Security Risk: 🟡 Medium | Next Review: After P0 fixes
