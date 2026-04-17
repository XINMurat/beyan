# Module: State Management Analysis

**Priority**: P2
**Tokens**: ~1600
**Analysis Time**: Loaded for frontend projects

---

## Purpose
Evaluates the application's state management approach for correctness, scalability, and avoiding common pitfalls like prop drilling, unnecessary global state, and race conditions.

---

## State Classification

```yaml
state_types:
  local_ui_state: "Button hover, modal open/closed → useState, local component"
  server_state: "Data fetched from API → React Query, SWR, RTK Query"
  global_app_state: "Auth user, theme, cart → Context, Zustand, Redux"
  url_state: "Filters, pagination, tab → URL search params"
```

**Most Common Mistake:** Putting everything in global state when it should be local or URL state.

## Library Selection Guide

```yaml
library_guide:
  useState_useReducer:
    use_when: "Component-level state, simple forms"
  react_query_swr:
    use_when: "Server data fetching, caching, background sync — preferred for API data"
  zustand_jotai:
    use_when: "Lightweight global state without Redux boilerplate — ideal for medium apps"
  redux_toolkit:
    use_when: "Large enterprise apps with complex update logic, time-travel debugging needed"
  context_api:
    use_when: "Infrequently changing values (theme, locale) — NOT for frequently changing state"
    antipattern: "Using Context for server state causes full subtree re-renders on every update"
```

## Async State & Race Conditions

```typescript
// ❌ WRONG: Race condition — last request might not be the last response
useEffect(() => {
  fetch(`/api/users/${id}`).then(r => r.json()).then(setUser);
}, [id]);

// ✅ CORRECT: Cleanup with AbortController or use React Query
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/users/${id}`, { signal: controller.signal })
    .then(r => r.json()).then(setUser);
  return () => controller.abort();
}, [id]);
```

## Scoring

```yaml
scoring:
  excellent: "State appropriately classified, React Query for server state, minimal global state."
  good: "Reasonable approach but some unnecessary global state."
  attention: "Context used for frequently changing server data, prop drilling 5+ levels deep."
  critical: "Everything in Redux, race conditions in useEffect, stale closures everywhere."
```
