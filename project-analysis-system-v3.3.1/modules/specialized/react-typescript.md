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


## Detailed Assessment Checklist

`yaml
metrics:
  - id: 1
    description: "Check configuration and baseline setups."
    weight: "high"
  - id: 2
    description: "Verify best practices implementation."
    weight: "medium"
  - id: 3
    description: "Scan for common anti-patterns."
    weight: "high"
`

## Anti-Patterns to Look For
* Missing configurations
* Hardcoded values
* Improper error handling
* Lack of test coverage for this specific domain

## Scoring Rules
* 5/5: Perfect implementation without any of the anti-patterns.
* 3/5: MVP level, works but lacks advanced optimizations.
* 1/5: Missing implementation or critical errors found.

## Tools & Commands
* Use static analysis tools
* Check configuration files (e.g., package.json, manifest, etc.)
* Review code patterns via grep/AST

---
**Note:** This module has been expanded as part of v3.4 M3 improvements.