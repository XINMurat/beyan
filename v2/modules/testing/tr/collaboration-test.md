# Module: Collaboration & Real-Time Testing

**Priority**: P1 (Real-Time Systems & Concurrency)
**Tokens**: ~3500
**Analysis Time**: Gerçek zamanlı (Real-time) kodlar tespit edildiğinde otonom yüklenir

---

## Purpose
Bu modül, projede bulunan WebSockets, SignalR, gRPC-Stream veya CRDT (Conflict-free Replicated Data Type) kullanan gerçek zamanlı (real-time) işbirliği özelliklerinin güvenilirliğini, bağlantı kopmalarına karşı dayanıklılığını ve veri çakışmalarını (conflict) nasıl yönettiğini analiz eder.

---

## WebSocket / SignalR Test Stratejisi

Gerçek zamanlı bağlantılar asla kesintisiz (perfect) olarak varsayılamaz. Aşağıdaki test senaryolarının kodda varlığı kontrol edilmelidir:

1.  **Bağlantı Kurma ve Kopma (Connect/Disconnect):** İstemci interneti koptuğunda UI düzgün bir uyarı veriyor mu?
2.  **Yeniden Bağlanma (Reconnection):** Kopan bağlantı geri geldiğinde (Exponential Backoff ile) sistem eski durumu kurtarıyor mu?
3.  **Message Ordering (Sıralama):** 1 ve 2 numaralı mesajlar ağda yer değiştirip 2 ve 1 olarak geldiğinde sistem bunu algılayabiliyor mu?
4.  **Backpressure Handling:** Sunucu, istemciye saniyede 10.000 mesaj gönderirse istemci kilitleniyor mu (Out of Memory)?

---

## Çok Kullanıcılı Senaryo Testleri (Concurrency)

```yaml
test_scenarios:
  concurrent_edit:
    description: "2 kullanıcı aynı kaynağı aynı anda düzenliyor"
    expected: "Conflict resolution (örn: Last-Write-Wins veya CRDT) devreye girmeli, kullanıcılar senkronize olmalı."
  
  user_join_leave:
    description: "Bir dökümana/odaya yeni bir kullanıcı katıldığında veya ayrıldığında"
    expected: "Katılan kişiye mevcut State aktarılmalı, ayrılan kişinin cursor/presence verileri temizlenmeli (Zombie cursor engellenmeli)."
  
  network_partition:
    description: "Bağlantı 5 saniye kopsa, o arada işlem yapılsa"
    expected: "İşlemler Offline-Queue (kuyruk) içine alınmalı, bağlantı gelince sunucuya sırayla basılmalı."
```

---

## CRDT / OT (Operational Transformation) Uyumluluk Testleri

Eğer proje Google Docs benzeri çoklu yazım (Collaborative Editing) destekliyorsa:

*   **Convergence Testleri:** Ağ kopsa, iki kişi farklı şeyler yazsa ve ağ birleştiğinde (Merge) her iki ekran da aynı metni (Eventual Consistency) gösteriyor mu?
*   **Merge Conflict Simülasyonu:** Git mantığındaki gibi otomatik birleştirilemeyen satırlarda sistemin çöküp çökmediği kontrol edilmelidir.

---

## Performans ve Ölçek (Scale) Stratejisi

Real-time sistemlerin performans testleri standart HTTP testlerinden farklıdır. Şunlar aranmalıdır:

1.  **Eşzamanlı Kullanıcı Testi:** 100 kullanıcının aynı anda bağlandığı test senaryoları.
2.  **Message Latency Ölçümü:** Gönderilen bir sinyalin diğer kullanıcılara ne kadar sürede (ms) ulaştığı.
3.  **Memory Leak Tespiti:** Bağlantılar açılıp kapandıkça sunucuda kapanmayan soketlerin (Socket Leak) hafızayı doldurup doldurmadığı.

**Kullanılması Önerilen Araçlar:** `Socket.IO tester`, `Artillery`, `k6 websocket`

---

## Scoring

```yaml
scoring:
  excellent: "Yeniden bağlanma testleri var, concurrent_edit senaryoları kapsanmış, memory leak testleri mevcut."
  good: "Temel websocket bağlantı testleri var ancak backpressure ve order testleri eksik."
  attention: "Soketler sadece 'Happy Path' üzerinden test ediliyor, kopma senaryosu kodlanmamış."
  critical: "Real-time sistem tamamen manuel test ediliyor, herhangi bir otomasyon yok."
```

---

## Output Format

```markdown
## 🔌 Gerçek Zamanlı Sistem & İşbirliği Test Raporu

### 📡 Bağlantı ve Hata Yönetimi
- **Yeniden Bağlanma (Reconnect):** [Var / Yok - Açıklama]
- **Mesaj Sıralama Garantisi:** [Var / Yok - Açıklama]

### 👥 Eşzamanlı Kullanıcı Riskleri (Concurrency)
- **Çakışma Yönetimi (Conflict Resolution):** [Hangi yöntem kullanılıyor? CRDT, LWW vb.]
- **Bulunan Riskler:** [Örn: Kullanıcı çıkışında state temizlenmiyor]

### 🚀 Performans ve Ölçeklenebilirlik Önerileri
- [Artillery veya k6 kullanılarak yük testi yazılması tavsiyesi vb.]
```
