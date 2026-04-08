# istanbul-weather-pipeline
Istanbul weather simulation and data visualization pipeline built with Python.  
(Python ile oluşturulmuş İstanbul hava durumu simülasyonu ve veri görselleştirme hattı.)
#  İstanbul Weather Simulator & Data Pipeline

[English]
This project is an **in-memory data pipeline** that simulates real-time weather conditions for Istanbul. Instead of fetching data from an external API, it uses **mathematical modeling** (sine waves & normal distribution) to generate realistic temperature and humidity patterns, then visualizes them using **Pandas** and **Matplotlib**.

[Türkçe]
Bu proje, İstanbul için anlık hava durumu koşullarını simüle eden bir **bellek içi veri hattıdır**. Verileri dış bir API'den çekmek yerine, gerçekçi sıcaklık ve nem desenleri üretmek için **matematiksel modelleme** (sinüs dalgaları ve normal dağılım) kullanır; ardından bu verileri **Pandas** ve **Matplotlib** ile görselleştirir.

---

##  Visual Analysis | Görsel Analiz
![Weather Simulation Report](weather_report.png)
*Note: The chart above is generated in real-time by the simulator.*

---

##  Key Features | Öne Çıkan Özellikler

* **In-Memory Processing:** No physical database or CSV files are required. All data is generated, processed, and visualized directly in RAM for maximum performance.
* **Realistic Simulation:** Implements a sine-wave based model to mimic the natural day/night temperature cycle of Istanbul.
* **Dual-Axis Visualization:** Displays two different data scales (Celsius and Percentage) on a single cohesive chart.
* **Zero-Footprint:** Designed to run without leaving temporary files behind, keeping your workspace clean.

* **Bellek İçi İşleme:** Fiziksel veritabanı veya CSV dosyası gerektirmez. Maksimum performans için tüm veriler doğrudan RAM üzerinde üretilir ve işlenir.
* **Gerçekçi Simülasyon:** İstanbul'un doğal gece/gündüz sıcaklık döngüsünü taklit etmek için sinüs dalgası tabanlı bir model uygular.
* **Çift Eksenli Görselleştirme:** İki farklı veri ölçeğini (Derece ve Yüzde) tek bir uyumlu grafik üzerinde gösterir.
* **Sıfır Ayak İzi:** Geçici dosyalar bırakmadan çalışacak şekilde tasarlanmıştır.

---

## 🛠️ Tech Stack | Teknolojiler

* **Language:** Python 3.14
* **Data Science:** Pandas, NumPy
* **Visualization:** Matplotlib (Seaborn-style)
* **Modeling:** Stochastic Processes & Sine-Wave Modeling

---

##   How to Run | Nasıl Çalıştırılır

1. **Clone the repository | Depoyu indirin:**
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/REPO_ADIN.git](https://github.com/KULLANICI_ADIN/REPO_ADIN.git)
