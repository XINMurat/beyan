# Epic → Story → Task Breakdown

## Nasıl Kullanılır?

1. **Epic**: Büyük hedef (örn: "Güvenlik İyileştirmeleri")
2. **Story**: Kullanıcı hikayesi (örn: "Admin kullanıcı olarak, unauthorized erişimi engellemek istiyorum")
3. **Task**: Teknik görev (örn: "AdminController'a [Authorize] attribute ekle")

---

## Örnek: Güvenlik Epic

### Epic: Güvenlik Kritik Sorunları Çöz

**Hedef**: Zero critical security vulnerabilities  
**Süre**: 2 sprint (4 hafta)  
**Value**: Risk azaltma, compliance

#### Story 1: SQL Injection Koruması

**Kullanıcı Hikayesi**:
> Backend developer olarak, SQL injection saldırılarına karşı korumalı olmak istiyorum, böylece veritabanım güvende olur.

**Kabul Kriterleri**:
- [ ] Tüm SQL query'ler parameterized
- [ ] Security test geçiyor
- [ ] Code review tamamlandı

**Tasklar**:
- [ ] Task 1.1: SQL injection noktalarını tespit et (1h, Ali)
- [ ] Task 1.2: Test case'ler yaz (2h, Ayşe)
- [ ] Task 1.3: Parameterized query'lere geç (2h, Ali)
- [ ] Task 1.4: Test et (30m, Ayşe)
- [ ] Task 1.5: Code review (30m, Mehmet)
- [ ] Task 1.6: Deploy (30m, DevOps)

**Toplam Çaba**: 6.5 saat

---

#### Story 2: Exposed Secrets Temizliği

**Kullanıcı Hikayesi**:
> DevOps engineer olarak, secrets'ların Git'te expose olmamasını istiyorum, böylece güvenlik riski oluşmaz.

**Kabul Kriterleri**:
- [ ] .env Git'ten silindi
- [ ] Tüm secrets rotate edildi
- [ ] .gitignore güncellendi

**Tasklar**:
- [ ] Task 2.1: Git history'den sil (30m, DevOps)
- [ ] Task 2.2: Secrets rotate et (1h, Backend)
- [ ] Task 2.3: .gitignore ekle (15m, DevOps)
- [ ] Task 2.4: .env.example oluştur (15m, DevOps)
- [ ] Task 2.5: README güncelle (30m, DevOps)

**Toplam Çaba**: 2.5 saat

---

## Şablon: Yeni Epic Oluştur

### Epic: [EPİC ADI]

**Hedef**: [HEDEF AÇIKLAMA]  
**Süre**: [SPRINT SAYISI]  
**Value**: [İŞ DEĞERİ]

#### Story: [STORY ADI]

**Kullanıcı Hikayesi**:
> [ROL] olarak, [İHTİYAÇ] istiyorum, böylece [FAYDA] sağlanır.

**Kabul Kriterleri**:
- [ ] Kriter 1
- [ ] Kriter 2

**Tasklar**:
- [ ] Task: [AÇIKLAMA] (süre, sorumlu)

**Toplam Çaba**: [SAAT]

---

## Epic Estimation

| Epic | Story Sayısı | Toplam Story Point | Çaba (saat) |
|------|--------------|-------------------|-------------|
| Güvenlik | 3 | 13 SP | 32h |
| Performans | 5 | 21 SP | 52h |
| Erişilebilirlik | 4 | 13 SP | 32h |

**Toplam**: 12 story, 47 SP, 116 saat (~3 sprint)
