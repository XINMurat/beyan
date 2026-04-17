# Beyan v2.0 — Sıkça Sorulan Sorular (FAQ)

---

## Genel Sorular

**S: Beyan v2.0 ile v1.0 arasındaki temel fark nedir?**
C: v1.0 statik bir prompt kütüphanesiydi — siz elle prompt seçer ve yapıştırırdınız. v2.0 otonom bir analiz motorudur: projenizi tarar, hangi modüllerin gerektiğine kendi karar verir ve devasa bir analiz promptu derleyerek yapay zekaya gönderir. İnsan müdahalesi yalnızca onay aşamalarında gerekir.

**S: Sistemi çalıştırmak için internet bağlantısı gerekiyor mu?**
C: CLI aracı (`analyzer.py`) ile prompt derleme tamamen offline çalışır. Sadece `--api openai` veya `--api anthropic` seçerseniz internet bağlantısı ve API anahtarı gerekir.

**S: Hangi programlama dilleri destekleniyor?**
C: Modüller dil agnostiktir (dil bağımsız). Python, JavaScript/TypeScript, C#/.NET, Go, Java, Rust projelerini analiz edebilir. Modüller proje dosyalarına bakarak hangi teknolojinin kullanıldığını tespit eder.

---

## Teknik Sorular

**S: Token limiti nedir ve aşarsam ne olur?**
C: Sistem varsayılan olarak **48.000** token limitiyle çalışır. `tiktoken` kütüphanesi sayesinde bu hesaplama artık %100 hassastır. Sınırı aşarsanız:
1. `--mode 1` ile sadece en kritik modülleri yükleyin.
2. `MANIFEST.yaml` içindeki `max_total_tokens` değerini artırın (LLM limitine dikkat ederek).

**S: Kendi modülümü nasıl eklerim?**
C: `USAGE_GUIDE.md` Bölüm 4'e bakın. Özetle: yeni bir `.md` dosyası oluşturun ve `MANIFEST.yaml`'a ekleyin. Sistem bir sonraki çalıştırmasında otomatik olarak yeni modülü tanır.

**S: `--api none` seçeneği ne işe yarar?**
C: Promptu derler ve `beyan_compiled_prompt.md` dosyasına kaydeder ama hiçbir API'ye göndermez. Bu dosyayı Cursor, ChatGPT veya Claude arayüzünde manuel olarak kullanabilirsiniz — en esnek seçenek budur.

**S: verify_integrity.ps1 ne kontrol eder?**
C: 3 şeyi kontrol eder: (1) `.md` dosyalarında mojibake (encoding bozukluğu) var mı? (2) Modüllerde kırık iç bağlantı var mı? (3) `MANIFEST.yaml`'daki modül tanımları fiziksel dosyalarla senkronize mi?

---

## Kullanım Sorular

**S: Hangi mode'u kullanmalıyım?**
C: `MODE_TRANSITIONS.md` dosyasına bakın. Kısa cevap: keşif ve değerlendirme için Mode 1, planlama için Mode 2, aktif geliştirme döngüsü için Mode 3.

**S: Rapor Türkçe çıkmıyor, ne yapmalıyım?**
C: `--lang tr` parametresini eklediğinizden emin olun. Eğer yine de İngilizce geliyorsa kullandığınız LLM'in sistem prompt'unu (BASE_PROMPT.md) güçlendirin — `"Tüm yanıtlar yalnızca Türkçe olacak"` direktifini daha üst satıra ekleyin.

**S: Sistem kendi kendine kod değiştirebilir mi?**
C: Evet, **Mode 3 (Semi-Autonomous Fix)** ile bu özellik pilot aşamasındadır. Ancak sistem asla onayınız olmadan kod yazmaz. Mode 3, her değişiklikten önce size "Mevcut vs Önerilen" farkını (diff) gösterir ve onayınızı bekler.

---

## Sorun Giderme

**S: "Modül bulunamadı" hatası alıyorum.**
C: `MANIFEST.yaml`'daki modül `path` değeri ile fiziksel dosya konumunu karşılaştırın. `{lang}` placeholder'ının doğru dile (tr/en) çözümlenip çözümlenmediğini kontrol edin.

**S: Python `yaml` import hatası veriyor.**
C: `pip install pyyaml` komutuyla bağımlılığı yükleyin.
