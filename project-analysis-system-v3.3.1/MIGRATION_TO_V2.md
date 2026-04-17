# Beyan v2.0 Agentic Framework - Göç (Migration) ve Karşılıklar Rehberi

Bu doküman, eski **Beyan v1.0.0** (Statik Prompt Kütüphanesi) ve **Project Analysis System v3.3.1** (Agentic Altyapı) sistemlerindeki eski alışkanlıklarınızı, yeni **Beyan v2.0 Agentic Framework** (`beyan-v2.0-agentic`) klasöründe nasıl devam ettireceğinizi anlatan bir haritadır.

---

## 🔍 1. Beyan v1.0.0 Kullanıcıları İçin Karşılıklar

Eski sistemdeki "Kopyala-Yapıştır" dönemi tamamen otomatize edildi.

| Eski Beyan v1.0.0'daki İşlem | Yeni Beyan v2.0'daki Karşılığı | Nasıl Yapılır? |
| :--- | :--- | :--- |
| **Triyaj Yapmak:** <br>`triyaj_yonlendirme_promptu_v1.0.md` dosyasını kopyalayıp klasör ağacını AI'a vererek hangi promptları kullanacağını sormak. | **Otomatik Keşif (Auto-Discovery):** <br>Yazdığımız CLI aracı klasörlerinizi milisaniyeler içinde tarar ve triyajı kendi kendine yapar. | Terminale şunu yazın:<br>`python cli/analyzer.py --target .` <br>Sistem dosyalarınızı tarar ve gereken modülleri (Örn: *Bu bir Blockchain projesi*) kendi anlar. |
| **Proje Türü Seçmek:** <br>`proje-turu/os_analiz_promptu_generic_v1.0.md` dosyasını bulup tüm içeriği AI'a vermek. | **Domain Modülleri:** <br>Eski devasa promptlar artık `modules/domains/tr/` altında ufak "Bilgi Modüllerine" dönüştü. | Hiçbir şey yapmanıza gerek yok. Sistem `CMakeLists.txt` veya `.c` gördüğü an o modülü koda otomatik dahil eder. |
| **Odak (Focus) Denetimi:** <br>`odak/guvenlik_denetim_promptu_v1.0.md` dosyasını arayıp bulmak. | **Focus Modülleri:** <br>Güvenlik, API ve KVKK uyumluluk bilgileri `modules/focus/tr/` altına taşındı. | Otomatik çekilir veya CLI aracını manuel modifiye ederek zorla ekletebilirsiniz. |
| **Meta Denetim (Sağlık Skoru):** <br>Dosyaları AI'a verip 1-5 arası puan istemek. | **Scoring Criteria Modülü:** <br>Eski Sağlık Skoru mekanizması artık sistemin kalbine gömüldü. | Analiz sonunda yapay zeka her zaman P0, P1, P2 formatında ve 10 üzerinden standart bir metrikle rapor üretir. |

---

## ⚙️ 2. Project Analysis System v3.3.1 Kullanıcıları İçin Karşılıklar

M3 ve M4 fazlarında yarattığımız otonom yetenekler, Beyan'ın domain bilgisiyle harmanlandı.

| v3.3.1'deki Yapı | Yeni Beyan v2.0'daki Karşılığı | Ne Değişti? |
| :--- | :--- | :--- |
| **Modül Eksikliği:** <br>Sistem sadece yazılım mimarisi, maliyet, UI/UX biliyordu; ancak "Blockchain" veya "DevOps" gibi spesifik domainlerde zayıftı. | **Devasa MANIFEST (50 Modül):** <br>Eski sistemdeki 35 modüle, Beyan'ın 11 eşsiz domain modülü eklendi. | Artık sistem sadece "Kodu düzelt" demiyor, "Kodu düzeltirken şu KVKK (Türkiye Pazarı) kurallarına uy" diyebilecek zekaya (Domain Knowledge) ulaştı. |
| **Dil Sorunu:** <br>Her şey tek dilde (Türkçe) çalışmaya programlıydı. | **Çift Dil Desteği (`{lang}`):** <br>Sistemin altyapısı `--lang en` veya `--lang tr` parametreleriyle çalışacak şekilde baştan aşağı yenilendi. | Hem Türkçe (tr) hem de İngilizce (en) projelerde kusursuz analizler. |
| **Bütünlük Testi:** <br>Sadece `.md` dosyalarının UTF-8 kontrolü yapılıyordu. | **CI/CD Pipeline (GitHub Actions):** <br>Kodunuz GitHub'a gittiğinde `verify_integrity.ps1` otomatik çalışıp repoyu test eder. | Proje her zaman "Production-Ready" kalır. |

---

## 🚀 Yeni Sistemde Nasıl Çalışılır? (Kısa Özet)

Eskiden onlarca dosya arasında kaybolurdunuz, yeni sistemde sadece **tek bir komut** yeterlidir.

1. Terminalinizi açın ve hedef projenizin bulunduğu klasöre gidin.
2. Aşağıdaki komutu çalıştırın:
```bash
python /path/to/beyan-v2.0-agentic/cli/analyzer.py --target . --mode 1 --lang tr
```
3. Aracın ürettiği `beyan_compiled_prompt.md` dosyasını yapay zekaya (ChatGPT/Claude/Gemini) yapıştırın.
4. **(Opsiyonel)** Eğer arkaplanda her şeyin tam otomatik yapılmasını istiyorsanız `.env` dosyanıza OpenAI anahtarınızı ekleyip sonuna `--api openai` parametresini ekleyin. Sonuç saniyeler içinde `.md` dosyası olarak bilgisayarınıza inecektir!
