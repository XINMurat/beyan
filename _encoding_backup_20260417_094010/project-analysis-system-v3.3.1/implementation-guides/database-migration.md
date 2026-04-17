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
