# Refactoring Rehberi

## God File Bölme

### Sorun
`utils/helpers.ts`: 2,847 satır

### Çözüm

#### Adım 1: Kategorilendir
```bash
# Fonksiyonları analiz et
grep "export function" utils/helpers.ts
```

Kategoriler:
- String helpers (23 fonksiyon)
- Date helpers (18 fonksiyon)
- Validation helpers (15 fonksiyon)
- Array helpers (17 fonksiyon)

#### Adım 2: Yeni Dosyalar Oluştur
```
utils/
├── string-helpers.ts
├── date-helpers.ts
├── validation-helpers.ts
└── array-helpers.ts
```

#### Adım 3: Fonksiyonları Taşı
```typescript
// string-helpers.ts
export function capitalize(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1);
}
```

#### Adım 4: Import'ları Güncelle
```bash
# Tüm dosyalarda eski import'ları bul
grep -r "from.*helpers" src/

# Yeni import'larla değiştir
# Öncesi: import { capitalize } from '@/utils/helpers';
# Sonrası: import { capitalize } from '@/utils/string-helpers';
```

#### Adım 5: Test Et
```bash
npm test
npm run build
```

**Checklist**:
- [ ] Fonksiyonlar kategorilendirildi
- [ ] Yeni dosyalar oluşturuldu
- [ ] Import'lar güncellendi
- [ ] Testler geçti
- [ ] Eski helpers.ts silindi
