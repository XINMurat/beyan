# Module: .NET Core Analysis

**Priority**: P1  
**Tokens**: ~1800  

## Turkish Output

```markdown
# .NET Core Analizi

## Genel Skor: 7.5/10 ✅

### Bulgular

#### 1. 🟡 Entity Framework N+1 Query (3 yer)

```csharp
// ❌ N+1
var users = _context.Users.ToList();
foreach (var user in users) {
    user.Orders = _context.Orders
        .Where(o => o.UserId == user.Id).ToList();
}

// ✅ Eager loading
var users = _context.Users
    .Include(u => u.Orders)
    .ToList();
```

**Çaba**: 1 saat
**Güven**: Yüksek (%95)

---

#### 2. ✅ Async/Await Doğru Kullanılmış

```csharp
// ✅ İyi: Async all the way
public async Task<User> GetUserAsync(int id) {
    return await _context.Users
        .FirstOrDefaultAsync(u => u.Id == id);
}
```

---

## Öneriler

### 🔴 P0
1. N+1 query'leri düzelt (1 saat)

**Hedef**: Optimize edilmiş EF queries

---

**Analiz Tamamlandı** | .NET Skoru: 7.5/10
```
