# Module: Database Analysis

**Priority**: P1 (High for Backend/Data-Intensive Apps)  
**Tokens**: ~2500  
**Analysis Time**: 10-15 minutes  

---

## Purpose

Evaluate database schema design, query performance, indexing strategy, migration safety, and data integrity. Identifies N+1 queries, missing indexes, and optimization opportunities.

---

## Analysis Dimensions

### 1. Schema Design & Normalization

```yaml
normalization_levels:
  1NF: "No repeating groups (atomic values)"
  2NF: "No partial dependencies on composite keys"
  3NF: "No transitive dependencies"
  denormalization: "Acceptable for read-heavy queries"

checks:
  proper_keys:
    - Primary keys on all tables
    - Foreign keys with proper constraints
    - Unique constraints where needed
  
  data_types:
    - Appropriate types (INT vs BIGINT, VARCHAR length)
    - No VARCHAR(MAX) or TEXT unless necessary
    - DATETIME vs DATE precision
  
  naming_conventions:
    - Consistent (snake_case or PascalCase)
    - Plural vs singular table names
    - Clear relationship naming

confidence: "high_88%"
```

### 2. Index Strategy

```yaml
missing_indexes:
  detection: "EXPLAIN query shows table/index scans"
  candidates:
    - Foreign key columns
    - WHERE clause columns
    - ORDER BY columns
    - JOIN columns
  
  commands:
    sqlserver: "SELECT * FROM sys.dm_db_missing_index_details"
    postgresql: "EXPLAIN ANALYZE <query>"
    mysql: "EXPLAIN <query>"

over_indexing:
  problem: "Too many indexes slow INSERT/UPDATE"
  detection: "Unused indexes (never in query plans)"
  
  sqlserver: |
    SELECT 
      OBJECT_NAME(s.object_id) AS TableName,
      i.name AS IndexName,
      s.user_seeks, s.user_scans, s.user_updates
    FROM sys.dm_db_index_usage_stats s
    JOIN sys.indexes i ON s.object_id = i.object_id
    WHERE s.user_seeks = 0 AND s.user_scans = 0

confidence: "high_92%"
```

### 3. N+1 Query Detection

```yaml
pattern:
  problem: "1 query + N queries in loop = N+1"
  symptom: "Slow page load despite small dataset"
  detection: "ORM logs show repeated similar queries"

entity_framework:
  bad: |
    var users = context.Users.ToList();
    foreach (var user in users) {
        var orders = context.Orders.Where(o => o.UserId == user.Id).ToList();
        // 1 + N queries
    }
  
  good: |
    var users = context.Users
        .Include(u => u.Orders)  // Eager loading
        .ToList();
    // 1 query with JOIN

sequelize:
  bad: |
    const users = await User.findAll();
    for (const user of users) {
        const orders = await Order.findAll({ where: { userId: user.id } });
    }
  
  good: |
    const users = await User.findAll({
        include: [{ model: Order }]  // Eager loading
    });

confidence: "high_95%"  # ORM logs are definitive
```

### 4. Query Performance

```yaml
slow_query_thresholds:
  excellent: "< 50ms"
  good: "50-100ms"
  attention: "100-500ms"
  critical: "> 500ms"

optimization_tactics:
  add_indexes: "Most common fix"
  rewrite_query: "Avoid subqueries, use JOINs"
  limit_columns: "SELECT specific columns, not *"
  pagination: "LIMIT/OFFSET for large result sets"
  caching: "Redis for read-heavy queries"
  
  confidence: "high_90%"
```

### 5. Migration Safety

```yaml
dangerous_migrations:
  - "DROP TABLE without backup"
  - "ALTER TABLE on large table (locks)"
  - "NOT NULL constraint without default"
  - "UNIQUE constraint on existing duplicates"

best_practices:
  - Reversible (add Down() method)
  - Test on copy of production data
  - Run during low-traffic window
  - Monitor lock duration
  - Use online schema change tools (gh-ost, pt-online-schema-change)

confidence: "medium_75%"
```

---

## Quick Analysis

```sql
-- SQL Server: Find slow queries
SELECT TOP 20
    total_elapsed_time / execution_count AS avg_time_ms,
    execution_count,
    SUBSTRING(text, statement_start_offset/2, 
        (CASE WHEN statement_end_offset = -1 
         THEN LEN(CONVERT(nvarchar(max), text)) * 2 
         ELSE statement_end_offset END - statement_start_offset)/2) AS query_text
FROM sys.dm_exec_query_stats
CROSS APPLY sys.dm_exec_sql_text(sql_handle)
ORDER BY avg_time_ms DESC;

-- PostgreSQL: Find missing indexes
SELECT 
  schemaname, tablename, 
  idx_scan AS index_scans,
  seq_scan AS sequential_scans,
  CASE 
    WHEN seq_scan > 0 THEN seq_scan::float / idx_scan::float 
    ELSE 0 
  END AS ratio
FROM pg_stat_user_tables
WHERE idx_scan > 0
ORDER BY ratio DESC
LIMIT 20;

-- Find N+1 pattern in logs
-- Count similar queries
grep "SELECT.*FROM Orders WHERE UserId" app.log | wc -l
```

---

**Example Report**:

```markdown
# Database Analysis

## Overall Score: 7/10 ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¡

### Critical Issues

#### 1. N+1 Query in Orders Endpoint ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´
**Query**: `SELECT * FROM Orders WHERE UserId = ?`
**Executed**: 347 times in single request
**Impact**: 2.4s page load

**Fix** (Entity Framework):
```csharp
// Before: N+1
var users = _context.Users.ToList();  // 1 query
foreach (var user in users) {
    user.Orders = _context.Orders
        .Where(o => o.UserId == user.Id)
        .ToList();  // N queries
}

// After: 1 query
var users = _context.Users
    .Include(u => u.Orders)  // JOIN
    .ToList();
```

**Effort**: 1 hour  
**Impact**: 2.4s ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ 0.15s (94% faster)  
**Confidence**: High (95%)

---

#### 2. Missing Index on Foreign Key ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´
**Table**: `Orders.CustomerId`
**Query**: `SELECT * FROM Orders WHERE CustomerId = 123`
**Current**: Full table scan (10M rows)
**Impact**: 850ms query time

**Fix**:
```sql
CREATE INDEX IX_Orders_CustomerId ON Orders (CustomerId);
```

**Effort**: 5 minutes (15 min on large table)  
**Impact**: 850ms ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ 8ms (99% faster)  
**Confidence**: High (98%)

---

### Schema Issues

#### 3. VARCHAR(MAX) Overuse ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¡
**Tables**: Users.Bio, Products.Description
**Problem**: Excessive memory allocation

```sql
-- Current
CREATE TABLE Users (
    Bio VARCHAR(MAX)  -- ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Overkill
)

-- Better
CREATE TABLE Users (
    Bio VARCHAR(500)  -- ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Realistic limit
)
```

**Effort**: 2 hours (data migration)  
**Impact**: 15% memory reduction  
**Confidence**: High (90%)
```

---

**Analysis Complete** | Database Health: 7/10 | Confidence: High (88%)
