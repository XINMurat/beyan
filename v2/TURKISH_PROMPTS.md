# Beyan v2.0 — Türkçe Prompt Örnekleri (TURKISH_PROMPTS)

Bu doküman, Beyan v2.0 sistemini farklı analiz senaryolarında kullanmak için hazır Türkçe prompt şablonları içerir. Promptları doğrudan bir LLM'e (ChatGPT, Claude vb.) yapıştırabilir veya `analyzer.py` ile derlenen promptla birleştirebilirsiniz.

---

## Kategori 1: Proje Genel Sağlık Analizi

```
Sana bir yazılım projesi sunuyorum. Beyan v2.0 analiz metodolojisini kullanarak:
1. Proje tipini ve teknoloji yığınını tespit et.
2. Projenin genel sağlık skorunu (0–10) ağırlıklı ortalama formülüyle hesapla.
3. Tespit ettiğin sorunları P0, P1, P2, P3 olarak önceliklendir.
4. Her bulgu için güven seviyeni (High/Medium/Low) belirt.
5. Epistemic Humility prensibine uy — belirsizsen açıkça belirt.

Projenin dosya yapısı ve önemli dosya içerikleri aşağıdadır:
[BURAYA PROJE İÇERİĞİNİ YAPIŞTIRIN]
```

---

## Kategori 2: Güvenlik Odaklı Analiz

```
Aşağıdaki kod tabanını OWASP Top 10 perspektifinden incele:
- SQL Injection, XSS, CSRF ve güvensiz doğrudan nesne referansı (IDOR) açıklarına bak.
- Ortam değişkeni yerine hard-coded secret kullanımı var mı tespit et.
- Her bulgu için: Hangi dosya, hangi satır, nasıl düzeltilir.
- Confidence level ekle: Spekülatif bulgular için "%30 ihtimalle, doğrulama gerekiyor" de.

[BURAYA KOD İÇERİĞİNİ YAPIŞTIRIN]
```

---

## Kategori 3: Performans Analizi

```
Bu projenin performans darboğazlarını tespit et:
- Frontend: Bundle büyüklüğü, lazy loading eksikliği, gereksiz re-render.
- Backend: N+1 sorgu, index eksikliği, cache fırsatları.
- Her öneri için: Tahmini performans kazanımı ve uygulama eforunu belirt.
- Spekülatif tahminlerde güven aralığı ver (örn: "Tahminen %20-40 hız artışı sağlar").

[BURAYA PROJE DOSYALARINI YAPIŞTIRIN]
```

---

## Kategori 4: Teknik Borç Değerlendirmesi

```
Bu projedeki teknik borcu ölç ve önceliklendir:
- Zombie kod (hiç çağrılmayan fonksiyonlar, ölü importlar) tespit et.
- Bus Factor riskini analiz et: Hangi kritik modülü kaç kişi biliyor?
- TODO/FIXME yorum sayısı ve dağılımına bak.
- Teknik borç "faizi": Şimdi düzeltilmezse ileride ne kadar maliyetli olur?
Sonunda: Teknik Borç Skoru ve 3 aylık tasfiye planı sun.

[BURAYA KOD İÇERİĞİNİ YAPIŞTIRIN]
```

---

## Kategori 5: KVKK ve Türkiye Uyumluluk Denetimi

```
Bu uygulamayı Türkiye mevzuatı açısından değerlendir:
- KVKK uyumu: Açık rıza mekanizması, veri silme hakkı, yurt dışı transfer var mı?
- Ödeme sistemi entegrasyonu: 3D Secure zorunlu mu? Merchant secret güvenli mi?
- E-fatura/GİB entegrasyonu gerekiyor mu?
- Her uyumsuzluk için öncelik (P0–P3) ve düzeltme yolunu belirt.

[BURAYA PROJE AÇIKLAMASI VE İLGİLİ KOD PARÇALARINI YAPIŞTIRIN]
```

---

## Kategori 6: Code Review Yardımcısı

```
Aşağıdaki Pull Request'i incele ve code review yap:
- Bug riski taşıyan satırları P0/P1 olarak işaretle.
- İyi yazılmış kısımları da takdir et (positive feedback).
- Her yorum için: Neden sorun? Nasıl düzeltilir? — somut kod örneği ver.
- Subjektif stil tercihlerini "Öneri" olarak işaretle, blocker olarak değil.

[BURAYA DIFF VEYA KOD PARÇASINI YAPIŞTIRIN]
```

---

## Kategori 7: Sprint Retrospektifi Yardımcısı

```
Geçen sprint'in teknik kararlarını değerlendir:
- Hangi teknik borç bilerek alındı (ve neden)?
- Hangi hızlı çözüm (quick fix) şimdi uzun vadeli sorun haline geldi?
- Bir sonraki sprint için: 1 adet P0 borç ve 2 adet P1 iyileştirme öner.

Sprint özeti: [SPRINT ÖZETINI BURAYA YAZIN]
Oluşturulan veya değiştirilen kritik dosyalar: [DOSYA LİSTESİ]
```

---

## Kategori 8: Mimari Karar Değerlendirmesi (ADR)

```
Önümüzde bir mimari karar var. Şu seçenekleri değerlendir:

Seçenek A: [Açıklama]
Seçenek B: [Açıklama]

Lütfen şu kriterlere göre karşılaştır:
- Ölçeklenebilirlik (Scalability)
- Maliyet
- Geliştirici deneyimi (DX)
- Uzun vadeli sürdürülebilirlik

Her seçenek için güçlü ve zayıf yönleri listele. Belirsizlik varsa açıkça belirt.
Sonunda önerini ve gerekçeni yaz.
```
