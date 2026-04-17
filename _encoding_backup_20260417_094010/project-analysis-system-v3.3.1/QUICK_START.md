# Quick Start - 5 Dakikada Başla

**Hedef Süre**: 5 dakika  
**Zorluk**: Kolay  
**Gereklilik**: Hiçbir teknik bilgi gerekmez

---

## 🚀 3 Basit Adım

### ADIM 1: Dosyaları Hazırla (1 dakika)

**Seçenek A - Minimum Setup** ✅ **(Önerilen)**
```
Sadece bu 2 dosyayı yükle:
1. ORCHESTRATOR_PROMPT.md
2. BASE_PROMPT.md
```

**Seçenek B - Tam Kurulum** 🔧
```
İndirdiğin tüm klasörü yükle (tüm modüller dahil)
```

**Hangi seçeneği seçmeliyim?**
- İlk defa kullanıyorum → **Seçenek A**
- Her şeyi denemek istiyorum → **Seçenek B**

---

### ADIM 2: Proje Dosyalarını Ekle (2 dakika)

Claude'a (bu AI) **proje dosyalarını** yükle:

**Web Projesi için**:
```
✅ package.json
✅ src/ klasörü
✅ tsconfig.json veya .eslintrc (varsa)
```

**Backend Projesi için**:
```
✅ *.csproj veya *.sln
✅ Controllers/, Services/ klasörleri
✅ appsettings.json
```

**Kaç dosya yüklemeliyim?**
- Minimum: 5-10 önemli dosya
- Maksimum: 50-100 dosya (Claude 200MB'a kadar destekler)
- **İpucu**: Tüm klasörü zip yapıp yükleyebilirsin

---

### ADIM 3: Analiz İste (2 dakika)

**İşte bu kadar basit! Şimdi şunu yaz:**

```markdown
"Projeyi analiz et"
```

**Ya da Türkçe örneklerden birini seç:**

| Ne İstiyorsun? | Yaz |
|----------------|-----|
| Genel analiz | "Projeyi analiz et" |
| Sadece güvenlik | "Security audit yap" |
| Performans sorunları | "Performans analizi çalıştır" |
| Plan istiyorum | "Aksiyon planı oluştur" |
| Otomatik düzelt | "P0 sorunları düzelt" |

---

## ✅ Başarılı Setup Kontrolü

**Analiz başarıyla çalıştı mı?** Şunları gördüysen EVET:

```markdown
# Proje Sağlık Raporu
**Genel Skor**: X.X/10

## P0 - Kritik Sorunlar
...

## P1 - Yüksek Öncelikli
...
```

**Sorun mu var?** → [Troubleshooting](#-sorun-giderme) bölümüne bak

---

## 🎯 İlk Sonuçları Anlama

### Skor Ne Anlama Geliyor?

```
9-10:  Mükemmel! 🟢 Çok iyi durumdasın
7-8.9: İyi 🟡 Birkaç iyileştirme yapılabilir
5-6.9: Orta 🟠 Dikkat gerektiren sorunlar var
0-4.9: Kritik 🔴 Acil iyileştirme gerekli
```

### Öncelik Seviyeleri

```
P0 🔴: HEMEN düzelt (güvenlik, data loss riski)
P1 🟡: Bu sprint içinde düzelt
P2 🟢: Yakında düzelt
P3 ⚪: Nice-to-have (opsiyonel)
```

---

## 🔄 Sonraki Adımlar

### Sadece Raporla Yetindiysen (Mode 1)
```markdown
✅ Raporu oku
✅ P0 sorunları not et
✅ Ekibinle paylaş
```

### Aksiyon Planı İstiyorsan (Mode 2)
```markdown
"Bu analiz için aksiyon planı oluştur"
```
→ Sprint planı + task breakdown alırsın

### Otomatik Düzeltme İstiyorsan (Mode 3)
```markdown
"P0 sorunlarını düzelt"
```
→ Sistem güvenli değişiklikler yapar (senin onayınla)

---

## 💡 İpuçları

### 🎯 Daha İyi Sonuçlar İçin

1. **Spesifik ol**
   ```
   ❌ "Analiz yap"
   ✅ "Security ve performans analizi yap"
   ```

2. **Öncelikli alanı belirt**
   ```
   ✅ "Sadece P0 sorunları göster"
   ✅ "Backend kod kalitesini değerlendir"
   ```

3. **Context ver**
   ```
   ✅ "Bu bir e-ticaret projesi, ödeme güvenliği kritik"
   ✅ "Production'da 10K kullanıcı var, performans önemli"
   ```

### 📚 Daha Fazla Öğren

- **Detaylı kullanım**: `USAGE_GUIDE.md`
- **100+ Türkçe örnek**: `TURKISH_PROMPTS.md`
- **Mode nasıl seçilir**: `MODE_TRANSITIONS.md`

---

## ❓ Sorun Giderme

### Hata: "Context window full"
**Sebep**: Çok fazla dosya yükledin  
**Çözüm**: Daha az dosya yükle (önce önemli olanlar)

### Hata: "Cannot analyze project"
**Sebep**: Proje dosyaları eksik  
**Çözüm**: En az package.json veya .csproj gibi ana dosyayı yükle

### Sonuç çok genel/yüzeysel
**Sebep**: Sistem minimum moddaysa  
**Çözüm**: Daha fazla modül yükle veya spesifik alan iste

### Türkçe yerine İngilizce rapor geldi
**Sebep**: Sistem dili algılayamamış  
**Çözüm**: Türkçe prompt kullan: "Projeyi analiz et"

---

## 🎓 Video Rehber (Yakında)

```
[📹 Video] 5 Dakikada İlk Analiz
[📹 Video] Aksiyon Planı Oluşturma
[📹 Video] Mode 3 ile Otomatik Düzeltme
```

---

## 🎉 Başarıyla Başladın!

**Bir sonraki adımlar**:

```markdown
1. ✅ İlk analizi oku
2. 📋 P0 sorunları not et
3. 🎯 Aksiyon planı iste
4. 🚀 Düzeltmelere başla
```

**Sorular?**
- `USAGE_GUIDE.md` - Kapsamlı rehber
- `FAQ.md` - Sık sorulan sorular (yakında)
- Community: (Discord/Slack link yakında)

---

**Hoş geldin! Analiz sistemine başarıyla başladın.** 🎊

*Oluşturulma: Aralık 2024*  
*Güncelleme: Her major release*
