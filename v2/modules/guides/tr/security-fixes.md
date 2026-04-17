# Guide: OWASP Top 10 Güvenlik Bulgularını Düzeltme

**Modül Türü**: Uygulama Rehberi (How-to Guide)
**Priority**: P3
**Hedef Kitle**: Tüm Geliştiriciler

---

## Purpose
Güvenlik analizi modülünün tespit ettiği OWASP Top 10 açıklarını nasıl gidereceğinizi somut before/after kod örnekleriyle gösterir.

---

## 1. SQL Injection Düzeltmesi

```python
# ❌ YANLIŞ: Kullanıcı girdisi direkt SQL'e ekleniyor
username = request.form['username']
query = f"SELECT * FROM users WHERE username = '{username}'"  # Tehlike!

# ✅ DOĞRU: Parameterized Query — Girdi asla SQL olarak yorumlanamaz
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

---

## 2. XSS (Cross-Site Scripting) Düzeltmesi

```javascript
// ❌ YANLIŞ: Kullanıcı girdisi direkt HTML'e yazılıyor
document.getElementById('greeting').innerHTML = `Merhaba, ${userName}!`;
// userName = "<script>document.cookie</script>" olabilir!

// ✅ DOĞRU: textContent kullan — HTML olarak yorumlanmaz
document.getElementById('greeting').textContent = `Merhaba, ${userName}!`;

// ✅ DOĞRU: React kullanıyorsanız, dangerouslySetInnerHTML'den kaçının
// JSX içinde {userName} otomatik olarak escape edilir
<div>Merhaba, {userName}!</div>
```

---

## 3. CSRF (Cross-Site Request Forgery) Koruması

```html
<!-- ✅ DOĞRU: Her form'a CSRF token ekle -->
<form action="/transfer" method="POST">
  <input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
  <input type="number" name="amount" />
  <button type="submit">Gönder</button>
</form>
```

```python
# Backend: Token doğrulama
@app.route('/transfer', methods=['POST'])
def transfer():
    token = request.form.get('csrf_token')
    if token != session.get('csrf_token'):
        abort(403)  # Reddedildi
```

---

## 4. Secret Management (API Key / Şifre Güvenliği)

```python
# ❌ YANLIŞ: API anahtarı direkt kodda — Git'te görünür!
openai_key = "sk-abc123..."

# ✅ DOĞRU: Ortam değişkeninden oku
import os
openai_key = os.environ.get("OPENAI_API_KEY")
if not openai_key:
    raise EnvironmentError("OPENAI_API_KEY ortam değişkeni tanımlanmamış!")
```

**.gitignore'a eklenmesi zorunlu dosyalar:**
```
.env
*.env.local
config/secrets.yml
appsettings.Development.json
```

---

## Hızlı Kontrol Listesi

- [ ] Tüm DB sorguları parameterized query kullanıyor mu?
- [ ] Kullanıcı girdisi HTML'e yazılırken escape ediliyor mu?
- [ ] POST formlarında CSRF token var mı?
- [ ] API anahtarları, şifreler ortam değişkenlerinde mi?
- [ ] `.env` dosyaları `.gitignore`'a eklenmiş mi?
