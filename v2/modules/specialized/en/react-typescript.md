# Module: React + TypeScript Best Practices

**Priority**: P1
**Tokens**: ~2000
**Analysis Time**: Loaded when react or *.tsx detected

---

## Purpose
Identifies TypeScript strict mode violations, React Hook rule breaches, unnecessary re-renders, state management antipatterns, and bundle size issues in React/TypeScript projects.

---

## TypeScript Strict Mode

```yaml
tsconfig_checks:
  must_enable: ["strict: true", "noImplicitAny: true", "strictNullChecks: true"]
  antipatterns:
    - "any usage — every 'any' is a type safety hole"
    - "Type assertions: 'obj as SomeType' bypasses type checking"
    - "@ts-ignore comments — suppress errors instead of fixing"
```

## React Hook Rules

```typescript
// ❌ WRONG: Hook inside condition
function Component({ isLoggedIn }) {
  if (isLoggedIn) {
    const [user, setUser] = useState(null); // Rules of Hooks violation!
  }
}

// ✅ CORRECT: Always at top level
function Component({ isLoggedIn }) {
  const [user, setUser] = useState(null);
}
```

## useEffect Dependency Array

```typescript
// ❌ WRONG: userId used but missing from deps — stale closure
useEffect(() => { fetchUser(userId); }, []);

// ✅ CORRECT
useEffect(() => { fetchUser(userId); }, [userId]);
```

## State Management

```yaml
antipatterns:
  context_overuse: "Context for frequently changing data — causes full subtree re-renders"
  prop_drilling: "Props passed 4+ levels deep — use Zustand or Context closer to usage"
  key_index: "key={index} in lists — breaks state on reorder, use unique IDs"
```

## Scoring

```yaml
scoring:
  excellent: "strict mode, no any, Hook rules followed, React Query for server state, lazy routes."
  good: "Mostly good, few any usages, some useEffect dep issues."
  attention: "Context overuse, God components >300 lines, key={index} everywhere."
  critical: "strict: false, Rules of Hooks violations causing render loops."
```
