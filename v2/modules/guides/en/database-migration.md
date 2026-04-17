# Guide: Safe Database Migration

**Module Type**: Implementation Guide
**Priority**: P3

---

## Purpose
Step-by-step guide for applying database schema changes in production with zero downtime.

---

## Zero-Downtime Column Addition

Never ALTER a large table in a single transaction — it locks the table:

```sql
-- STEP 1: Add nullable column (no table lock)
ALTER TABLE orders ADD COLUMN discount_amount DECIMAL(10,2) NULL;

-- STEP 2: Backfill existing rows in batches
UPDATE orders SET discount_amount = 0 WHERE discount_amount IS NULL LIMIT 5000;
-- Repeat until all rows filled

-- STEP 3: After code supports both columns, add NOT NULL constraint
ALTER TABLE orders MODIFY COLUMN discount_amount DECIMAL(10,2) NOT NULL DEFAULT 0;
```

## Migration Tool Selection

```yaml
tools:
  flyway: "SQL-first, Java/.NET projects, simple and battle-tested"
  liquibase: "XML/YAML/JSON changesets, automatic rollback support"
  ef_core: "Code-first .NET, ORM-integrated"
  alembic: "Python/SQLAlchemy projects"
```

## Rollback Strategy

```sql
-- For every migration (V2__add_discount.sql) write a matching undo:
-- U2__add_discount.sql
ALTER TABLE orders DROP COLUMN discount_amount;
```

**Golden Rule:** Adding columns/tables = reversible. Dropping data = irreversible. Always backup before destructive changes.

## Quick Checklist

- [ ] Database backup taken before migration?
- [ ] Migration tested on staging first?
- [ ] Rollback script written and tested?
- [ ] Large table changes done in batches?
- [ ] Migration automated in CI/CD pipeline?
