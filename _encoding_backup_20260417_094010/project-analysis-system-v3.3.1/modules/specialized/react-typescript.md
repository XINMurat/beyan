# Module: React + TypeScript Analysis

**Priority**: P1  
**Tokens**: ~2000  

## Turkish Output

```markdown
# React + TypeScript Analizi

## TypeScript Strict: ✅ Aktif
## React Best Practices: 7/10 🟡

### Bulgular

#### 1. 🟡 useEffect Bağımlılıkları Eksik (12 yer)

```typescript
// ❌ Eksik dependency
useEffect(() => {
  fetchUser(userId);
}, []);  // userId dependency eksik!

// ✅ Tam
useEffect(() => {
  fetchUser(userId);
}, [userId]);
```

**Çaba**: 1 saat
**Güven**: Yüksek (%95)

---

#### 2. 🔴 Gereksiz Re-render'lar (5 component)

```typescript
// ❌ Her render'da yeni object
function UserList({ users }) {
  const filteredUsers = users.filter(u => u.active);
  // Her seferinde yeni array!
}

// ✅ useMemo ile cache
function UserList({ users }) {
  const filteredUsers = useMemo(
    () => users.filter(u => u.active),
    [users]
  );
}
```

**Çaba**: 2 saat
**Güven**: Yüksek (%90)

---

## Öneriler

### 🔴 P0
1. useEffect dependencies düzelt (1 saat)
2. Re-render'ları optimize et (2 saat)

**Hedef**: Performant React app

---

**Analiz Tamamlandı** | React/TS Skoru: 7/10
```
