# Module: React + TypeScript Best Practices

**Priority**: P1 (Teknoloji Stack — Frontend Ekosistemi)
**Tokens**: ~2000
**Analysis Time**: `react`, `*.tsx` veya `typescript` tespit edildiğinde otonom yüklenir

---

## Purpose
React ve TypeScript kullanan projelerde Type Safety, Hook kuralları, gereksiz re-render döngüleri, State Management antipatternleri ve Bundle büyüklüğü gibi kritik kalite ve performans sorunlarını tespit eder.

---

## TypeScript Strict Mode Analizi

`tsconfig.json` dosyasının `strict` modda olup olmadığı kontrol edilmelidir. Strict mod kapalıysa, projenin gerçek tip güvenliği (Type Safety) yoktur demektir.

```yaml
tsconfig_checks:
  must_be_enabled:
    - "strict: true"
    - "noImplicitAny: true"
    - "strictNullChecks: true"
  antipatterns:
    - "any kullanımı: Her 'any' bir güvenlik ve kalite deliğidir"
    - "'as' ile zorla tip dönüştürme (Type Assertion): 'obj as SomeType'"
    - "'@ts-ignore' yorum satırları: Hata bastırmak yerine düzeltmek gerekir"
```

---

## React Best Practices ve Hook Kuralları

### Rules of Hooks İhlalleri (Kritik)
Hook'ların sadece 2 temel kuralı vardır ve her ikisinin de ihlali component'in silah gibi davranmasına neden olur:

```typescript
// ❌ YANLIŞ: Koşul içinde Hook
function Component({ isLoggedIn }) {
  if (isLoggedIn) {
    const [user, setUser] = useState(null); // HATA: Koşul içinde hook
  }
}

// ✅ DOĞRU: Her zaman component'in en üstünde
function Component({ isLoggedIn }) {
  const [user, setUser] = useState(null); // Doğru: Koşuldan bağımsız
}
```

### useEffect Dependency Array Hataları
```typescript
// ❌ YANLIŞ: userId her değiştiğinde effect çalışmalı ama eksik bağımlılık
useEffect(() => {
  fetchUser(userId); // userId bağımlılık dizisinde yok!
}, []); // Sonsuz döngü veya stale closure riski

// ✅ DOĞRU
useEffect(() => {
  fetchUser(userId);
}, [userId]); // userId takip ediliyor
```

### Gereksiz Re-render (Performance)
*   **`useMemo`:** Pahalı hesaplamaların gereksiz yere her render'da tekrar yapılmasını önler.
*   **`useCallback`:** Child component'lere geçirilen fonksiyonların referans eşitliğini korur.
*   **Antipattern:** `useMemo` veya `useCallback`'i her yere savurganlıkla koymak da performansı düşürür.

---

## State Management Değerlendirmesi

```yaml
state_management:
  context_api_overuse:
    description: "Context API tüm global state için kullanılıyor ve her tüketici (consumer) her değişimde re-render alıyor."
    check: "Çok fazla sayıda Context provider var mı?"
  prop_drilling:
    description: "Bir veriyi 4-5 component'ten geçirmek zorunda kalmak."
    check: "Props'ların kaç seviye derinliğe kadar aşağı indiğini say."
  library_eval:
    description: "Zustand/Jotai küçük projeler için; Redux büyük enterprise projeler için uygundur."
    check: "Proje büyüklüğüyle orantılı bir state kütüphanesi seçilmiş mi?"
```

---

## Bileşen (Component) Kalitesi

*   **God Component:** 300+ satır ve onlarca props alan component'ler bölünmelidir.
*   **Separation of Concerns:** UI kodu (JSX) ile iş mantığı kod aynı dosyada olmamalıdır. Custom Hook'lar ve servisler kullanılmalıdır.
*   **Key Prop Antipatternleri:** Listeler render edilirken `key={index}` kullanımı, sıra değişince state karışmasına neden olur. `key` için benzersiz ID kullanılmalıdır.

---

## Bundle Analizi

*   **Tree-shaking:** Kütüphanelerin tamamı mı import ediliyor? `import _ from 'lodash'` yerine `import debounce from 'lodash/debounce'` kullanılmalı.
*   **Lazy Loading:** Route bazlı `React.lazy()` ile büyük component'ler gerektiğinde yüklenmelidir.

---

## Scoring

```yaml
scoring:
  excellent: "strict mode açık, any yok, hook kuralları tam, state management ölçülü, lazy loading var."
  good: "Çoğunlukla iyi ama birkaç any veya useEffect dependency hatası var."
  attention: "Context overuse, God component'ler, useMemo eksikliğinden kaynaklı performans sorunları."
  critical: "strict: false, 'as any' her yerde, Rules of Hooks ihlalleri ciddi re-render döngüleri yaratıyor."
```

---

## Output Format

```markdown
## ⚛️ React + TypeScript Analiz Raporu

### TypeScript Sağlığı
- **Strict Mode:** [Açık / Kapalı]
- **'any' Kullanım Sayısı:** [Tahmini]

### Hook ve Bileşen Kalitesi
- **Rules of Hooks İhlalleri:** [Var / Yok, Açıklama]
- **God Component Sayısı:** [Kaç tane >300 satır component var?]

### State Management
- **Mevcut Yaklaşım:** [Context / Zustand / Redux / vb.]
- **Önerilen Değişiklik:** [Varsa]
```