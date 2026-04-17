# Guide: Fixing OWASP Top 10 Security Findings

**Module Type**: Implementation Guide
**Priority**: P3

---

## Purpose
Provides patch code for the most critical security findings identified by the security analysis module.

---

## 1. SQL Injection Fix

```python
# ❌ WRONG: User input concatenated into SQL
query = f"SELECT * FROM users WHERE username = '{username}'"

# ✅ CORRECT: Parameterized query
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

---

## 2. XSS Fix

```javascript
// ❌ WRONG: innerHTML with user data
document.getElementById('msg').innerHTML = userInput;

// ✅ CORRECT: textContent escapes HTML automatically
document.getElementById('msg').textContent = userInput;

// ✅ CORRECT in React: JSX auto-escapes
<div>{userInput}</div>
```

---

## 3. CSRF Protection

```html
<form action="/transfer" method="POST">
  <input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
  <button type="submit">Send</button>
</form>
```

---

## 4. Secret Management

```python
# ❌ WRONG: Hardcoded secret in source code
api_key = "sk-abc123..."

# ✅ CORRECT: Load from environment variable
import os
api_key = os.environ.get("API_KEY")
if not api_key:
    raise EnvironmentError("API_KEY not set")
```

**.gitignore must include:**
```
.env
*.env.local
config/secrets.yml
```

## Quick Checklist

- [ ] All DB queries using parameterized queries?
- [ ] User input escaped before rendering in HTML?
- [ ] CSRF tokens on all POST forms?
- [ ] API keys/passwords in environment variables?
- [ ] `.env` files in `.gitignore`?
