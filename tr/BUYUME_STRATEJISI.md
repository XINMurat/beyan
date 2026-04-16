# PROMPT AİLESİ — BÜYÜME STRATEJİSİ VE KATKI REHBERİ

> **Son Güncelleme:** 2026-04-16
> **Kapsam:** Yeni prompt ekleme, mevcut promptu güncelleme ve aileyi yönetme kuralları

---

## Ailenin Mevcut Yapısı

```
PROJE TÜRÜ BAZLI (7 prompt)         ODAK BAZLI (4 prompt)
├── master_v2.3     Uygulama         ├── guvenlik_denetim
├── os_generic      Sistem/OS        ├── api_tasarim_denetim
├── research_ai     Araştırma/AI     ├── performans_denetim
├── veri_analitik   Veri/ETL         └── uyumluluk_denetim
├── altyapi_devops  IaC/DevOps
├── legacy_goc      Göç/Legacy       ÖZEL (1 prompt)
└── blockchain      Blockchain       └── ai_analiz_denetim (meta)

YATAY ARAÇLAR (3 prompt)            GİRİŞ NOKTASI (1 prompt)
├── duzeltme_plani                  └── triyaj_yonlendirme
├── proje_saglik_skoru
└── triyaj_yonlendirme
```

**Toplam: 15 aktif prompt + 3 deprecated**

---

## Yeni Prompt Ne Zaman Eklenir?

Yeni bir prompt eklemeden önce şu üç soruyu cevapla:

**1. Bu gerçekten yeni bir tür mü?**
Mevcut bir prompt kapsamına girmiyorsa yeni prompt gerekir. Örnek: "Oyun motoru analizi" → `master_v2.3` kullanılamaz → yeni prompt.

**2. Yoksa odak bazlı bir ek mi?**
Proje türünden bağımsız ama belirli bir lens gerektiriyorsa odak bazlı prompt. Örnek: "Erişilebilirlik denetimi" → tüm proje türlerine uygulanabilir → odak bazlı.

**3. Yoksa mevcut bir prompta bölüm eklemek yeterli mi?**
Kapsam küçükse yeni dosya yerine mevcut prompta alt bölüm ekle. Örnek: "CLI aracı desteği" → `master_v2.3`'e not eklemek yeterli.

---

## Yeni Prompt Yazma Standardı

Her yeni prompt şu yapıyı zorunlu olarak içermelidir:

### Zorunlu Başlık Bloğu
```markdown
# [BAŞLIK] — Generic Edition v1.0

> **Son Güncelleme:** [Tarih]
> **Güncelleme Tetikleyicisi:** [Neden eklendi/güncellendi]
> **Sonraki Gözden Geçirme:** [Koşul veya tarih]
```

### Zorunlu Bölümler (Sırayla)
1. Rol Tanımı (kim olduğu, neyin nasıl analiz edileceği)
2. Tanımlayıcı/Değerlendirici katman tablosu *(yatay araçlar için opsiyonel)*
3. Temel Kurallar (placeholder yasağı, dil standardı, analiz sırası)
4. Aşama 0: Ön Keşif (`preflight_summary.md`)
5. Tanımlayıcı aşamalar (sisteme özgü)
6. `— DEĞERLENDİRİCİ KATMAN —` bölümü
7. Değerlendirici aşamalar (tamamlanmamışlık haritası **zorunlu**)
8. Çıktı Dosya Sistemi (`docs/[dizin-adi]/` ile)
9. Kalite Kontrol Listesi (minimum 6 madde)

### Zorunlu Çıktı Dosyaları
Her proje türü bazlı prompt şunları içermelidir:
- `completeness_report.md` — tamamlanmamış bileşenler
- `system_taxonomy.md` — alan terimleri sözlüğü
- `index.md` — her zaman en son yazılır

### Yasak Örüntüler
- ❌ Proje adı, kişi adı veya spesifik teknoloji adı başlıkta geçemez
- ❌ Placeholder içerik bırakılamaz — her tablo ve örnek doldurulmalı ya da `[sisteme özgü doldur]` notu konulmalı
- ❌ "Opsiyonel" etiketi son aşama dışında kullanılamaz

---

## Mevcut Prompt Güncelleme Kuralları

### Ne Zaman Güncellenir?
- Mevzuat değişikliği (uyumluluk promptu)
- Ekosistem değişikliği (blockchain promptu — yeni EVM standartları vb.)
- Kullanımda tespit edilen boşluk veya hata
- Meta-denetim döngüsü bulgusu

### Güncelleme Prosedürü
1. Dosyanın başlık bloğundaki `Son Güncelleme` ve `Güncelleme Tetikleyicisi` alanlarını güncelle
2. Değişikliği ilgili bölümde yap
3. Eğer yapısal değişiklikse (yeni aşama, yeni çıktı dosyası): versiyon numarasını artır (`v1.0` → `v1.1`)
4. Eğer içerik güncellemesiyse: versiyon numarası değişmez, sadece tarih güncellenir

### Büyük Versiyon (Major) Eşiği
`v1.x` → `v2.0` geçişi için:
- Aşama yapısı değişmişse
- Çıktı dizin yapısı değişmişse
- Temel kurallar değişmişse

Büyük versiyon geçişinde eski dosya `DEPRECATED` uyarısıyla saklanır, silinmez.

---

## Aile Gözden Geçirme Döngüsü

### Tetikleyiciler (herhangi biri olduğunda)
- Yeni proje türü ihtiyacı ortaya çıktığında
- Mevzuat veya ekosistem büyük değişim geçirdiğinde
- 5+ yeni prompt eklendikten sonra
- Gerçek projede uygulamada yapısal sorun tespit edildiğinde

### Gözden Geçirme Adımları
1. `triyaj_yonlendirme_promptu`'nun referans tablosunu güncelle
2. `NAVIGASYON_STANDARDI.md` dizin kartını güncelle
3. Meta-denetim promptunu (`ai_analiz_sistemi_denetim`) çalıştır
4. Sağlık Skoru karşılaştırmalı değerlendirmesi üret
5. Bu dosyadaki "Ailenin Mevcut Yapısı" bölümünü güncelle

---

## Uzun Vadeli Kapsam Hedefleri

Aşağıdaki boşluklar bilinçli olarak ertelenmiştir — öncelik kazandığında eklenecek:

| Eksik Alan | Öncelik | Tetikleyici Koşul |
|---|---|---|
| Oyun / Game Engine Analiz Promptu | Düşük | Oyun projesi analiz talebi |
| Hardware / FPGA Analiz Promptu | Düşük | Donanım projesi analiz talebi |
| Mikroservis Özgün Sorular (`master_v2.3` eki) | Orta | Mikroservis projesinde v2.3 yetersizliği tespit edilirse |
| Mobil Platform Özgün Sorular (`master_v2.3` eki) | Orta | Mobil projede v2.3 yetersizliği tespit edilirse |
| Erişilebilirlik Odak Promptu | Düşük | Kamu veya sağlık projesi analiz talebi |
