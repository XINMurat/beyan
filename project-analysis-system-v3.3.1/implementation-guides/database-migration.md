# Database Migration Rehberi

## Güvenli Migration Stratejisi

### Adım 1: Backup Al
```bash
# PostgreSQL
pg_dump production_db > backup_$(date +%Y%m%d).sql

# SQL Server
sqlcmd -S server -d database -Q "BACKUP DATABASE [db] TO DISK='backup.bak'"
```

### Adım 2: Test Migration (Staging)
```bash
# Migration oluştur
dotnet ef migrations add AddIndexCustomerId

# Staging'de test et
dotnet ef database update --connection "[STAGING]"
```

### Adım 3: Rollback Planı Hazırla
```csharp
protected override void Down(MigrationBuilder migrationBuilder)
{
    migrationBuilder.DropIndex(
        name: "IX_Orders_CustomerId",
        table: "Orders");
}
```

### Adım 4: Production'da Uygula
```bash
# Maintenance window
# Low traffic saatlerde (gece 2-4)
dotnet ef database update --connection "[PROD]"
```

**Checklist**:
- [ ] Backup alındı
- [ ] Staging'de test edildi
- [ ] Rollback planı hazır
- [ ] Maintenance window planlandı
- [ ] Production'da uygulandı
- [ ] Smoke test geçti


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