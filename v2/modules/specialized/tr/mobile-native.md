# Module: Mobile Native Analysis

**Priority**: P2 (Mobil Platform Ekosistemi)
**Tokens**: ~2000
**Analysis Time**: `pubspec.yaml`, `Podfile`, `android/`, `*.xcodeproj` tespit edildiğinde yüklenir

---

## Purpose
React Native, Flutter veya native iOS/Android projelerindeki platform spesifik sorunları, performans darboğazlarını ve mağaza (App Store / Google Play) yayın gerekliliklerini analiz eder.

---

## Flutter Analizi

```yaml
flutter_checks:
  widget_rebuild:
    description: "const constructor kullanılmayan widget'lar her build'de yeniden oluşturulur."
    check: "const Text('...'), const Icon(...) kullanımı yaygın mı?"
  state_management:
    description: "setState() tüm widget ağacını rebuild eder — büyük projelerde Riverpod/Bloc tercih edilmeli."
  platform_channel:
    description: "Native API'ye köprü (MethodChannel) gerekliyse doğru hata yönetimi var mı?"
```

---

## React Native Analizi

```yaml
react_native_checks:
  bridge_usage:
    description: "Yeni Mimari (JSI) yerine eski Bridge mi kullanılıyor? Bridge her JS/Native çağrısında overhead ekler."
  flatlist_optimization:
    description: "FlatList'te getItemLayout, keyExtractor ve initialNumToRender optimize edilmiş mi?"
  hermes_engine:
    description: "Hermes JS motoru aktif mi? Başlangıç süresini önemli ölçüde kısaltır."
```

---

## Uygulama Mağazası Gereklilikleri

```yaml
store_requirements:
  ios_app_store:
    - "Privacy Manifest (PrivacyInfo.xcprivacy) iOS 17+ için zorunlu"
    - "App Transport Security (ATS) HTTP bağlantı istisnası gerekçelendirilmeli"
  google_play:
    - "targetSdkVersion en güncel Android API seviyesinde mi?"
    - "64-bit kütüphane desteği zorunlu"
    - "Veri güvenliği bölümü doldurulmuş mu?"
```

---

## Output Format

```markdown
## 📱 Mobil Uygulama Analiz Raporu

### Platform ve Framework
- **Framework:** [Flutter / React Native / Native iOS / Native Android]
- **Min SDK Hedefi:** [iOS X / Android API Y]

### Performans Bulguları
- [Widget rebuild optimizasyonu eksik, P1]
- [FlatList optimizasyonu yok, yavaş scroll]

### Mağaza Uyum Durumu
- **iOS Privacy Manifest:** [Var / Eksik - KRİTİK]
- **Google Play Data Safety:** [Dolu / Eksik]
```