# Module: State Management Analysis

**Priority**: P2  
**Tokens**: ~1800  

## State Management Patterns

```yaml
solutions:
  react_context: "Simple, built-in"
  redux: "Complex apps, time-travel debugging"
  zustand: "Lightweight alternative"
  recoil: "Facebook's solution"
  mobx: "Observable-based"
```

## Turkish Output

```markdown
# State Yönetimi Analizi

## Genel Skor: 6/10 🟡

### Bulgular

#### 1. 🔴 Karışık State Çözümleri

**Sorun**: Redux + Context + Local state (3 farklı yöntem)

```typescript
// File A: Redux
const user = useSelector(state => state.user);

// File B: Context (aynı user için!)
const user = useContext(UserContext);

// File C: Local state
const [user, setUser] = useState(null);
```

**Problem**: Hangi user doğru? Senkronizasyon hatası riski

**Çözüm**: Tek kaynak seç (Zustand öneriyoruz)
```typescript
// Zustand (basit, hızlı)
const useUserStore = create((set) => ({
  user: null,
  setUser: (user) => set({ user }),
}));

// Kullanım
const user = useUserStore(state => state.user);
```

**Çaba**: 1 hafta (migration)
**Güven**: Yüksek (%85)

---

#### 2. 🟡 Prop Drilling (7 seviye derin)

```tsx
// ❌ Prop drilling: 7 component zinciri
<App user={user}>
  <Layout user={user}>
    <Sidebar user={user}>
      <Menu user={user}>
        <MenuItem user={user}>
          ...
```

**Çözüm**: Context veya state management library
```tsx
// ✅ Context ile
const user = useUser();  // Her component'te
```

**Çaba**: 2 gün
**Güven**: Yüksek (%90)

---

## Öneriler

### 🔴 P0
1. Tek state solution seç (1 hafta)
2. Prop drilling'i düzelt (2 gün)

**Hedef**: Tutarlı, maintainable state

---

**Analiz Tamamlandı** | State Yönetimi: 6/10
```
