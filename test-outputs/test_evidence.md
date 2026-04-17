# Test Dosyaları ve Kanıtlar

İçinizin tamamen rahat etmesi için az önce çalıştırdığım komutların kodlarını, birleştirme scriptlerini ve **yapay zekanın kendi kendine ürettiği 34 bin tokenlik o devasa promptu** inceleyebilmeniz için aşağıya ekliyorum. 

> [!NOTE]
> Aşağıdaki bağlantılara tıklayarak üretilen dosyaların içlerini klasörünüz içerisinde bizzat okuyabilirsiniz.

### 1. Üretilen Nihai Prompt (Otonom Çıktı)
Sistemin hiçbir klasöre/koda dokunmadan sadece "kendini tarayarak" ürettiği, içinde Meta Analiz (AI Denetimi) dahil tam 7 modül barındıran nihai derlenmiş prompt dosyası:
👉 [beyan_compiled_prompt.md](file:///C:/TRAE/beyan-v1.0.0/test-outputs/beyan_compiled_prompt.md)

### 2. Akıllı CLI Aracı (Motor)
Sistemin beyni olan, klasörleri tarayıp `MANIFEST.yaml` üzerinden hangi modüllerin yükleneceğine karar veren ve token maliyetini hesaplayan Python betiği:
👉 [analyzer.py](file:///C:/TRAE/beyan-v1.0.0/test-outputs/analyzer_script.py)

### 3. Yapılandırma Dosyası (MANIFEST)
İçerisinde sizinle beraber kurtardığımız v3.3.1 modülleri ve Beyan'ın eski bilgilerinin birleştiği, toplam 51 modül kapasiteli o devasa yapılandırma dosyası:
👉 [MANIFEST.yaml](file:///C:/TRAE/beyan-v1.0.0/test-outputs/MANIFEST.yaml)

### 4. Taşıma İşlemi İçin Yazdığım Betik
Eski v3.3.1 modüllerini çoklu-dil (tr/en) klasörlerine parçalayarak taşırken yazdığım geçici Python operasyon betiği:
👉 [merge_modules.py](file:///C:/TRAE/beyan-v1.0.0/test-outputs/merge_modules.py)

---

### Terminalde Çalıştırdığım Test Komutu ve Çıktısı

Eğer sistemi denemek isterseniz terminale tam olarak şunu yazmanız yeterli:
```powershell
# beyan-v2.0-agentic klasörü içerisinde:
python cli/analyzer.py --target . --mode 1 --lang tr
```

**Aldığım Çıktı (Terminal):**
```text
[*] Hedef dizin taranıyor: C:\TRAE\beyan-v1.0.0\beyan-v2.0-agentic
[*] Algılanan teknolojiler: yaml, python, cli, manifest.yaml
[*] Secilen Modüller (7 adet): project_intelligence, file_structure_analysis, performance_analysis, ui_ux_analysis, security_analysis, scoring_criteria, meta_analysis
[*] Tahmini Token Maliyeti: 34185 (Limit: 35000)
[BASARILI] Prompt derlendi ve kaydedildi: C:\TRAE\beyan-v1.0.0\beyan-v2.0-agentic\beyan_compiled_prompt.md
```
