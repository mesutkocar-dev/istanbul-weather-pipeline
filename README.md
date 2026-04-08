#  İstanbul Weather Simulator & Data Pipeline

[English]
This project is an **in-memory data pipeline** that simulates real-time weather conditions for Istanbul. Instead of fetching data from an external API, it uses **mathematical modeling** (sine waves & normal distribution) to generate realistic temperature and humidity patterns, then visualizes them using **Pandas** and **Matplotlib**.

[Türkçe]
Bu proje, İstanbul için anlık hava durumu koşullarını simüle eden bir **bellek içi veri hattıdır**. Verileri dış bir API'den çekmek yerine, gerçekçi sıcaklık ve nem desenleri üretmek için **matematiksel modelleme** (sinüs dalgaları ve normal dağılım) kullanır; ardından bu verileri **Pandas** ve **Matplotlib** ile görselleştirir.

---

# Visual Analysis | Görsel Analiz

![Weather Simulation Report](weather_report.png)

> **Note:** If the image doesn't appear, please run `weather_simulator.py` first to generate the file.
> **Not:** Eğer görsel görünmüyorsa, dosyayı oluşturmak için lütfen önce `weather_simulator.py` kodunu çalıştırın.

---

# Key Features | Öne Çıkan Özellikler

* **In-Memory Processing:** No physical database or CSV files are required. All data is processed directly in RAM for maximum performance.
* **Realistic Simulation:** Implements a sine-wave based model to mimic the natural day/night temperature cycle of Istanbul.
* **Dual-Axis Visualization:** Displays temperature (Celsius) and humidity (Percentage) on a single cohesive chart.
* **Zero-Footprint:** Designed to run without leaving temporary files behind.

* **Bellek İçi İşleme:** Fiziksel veritabanı veya CSV dosyası gerektirmez. Maksimum performans için tüm veriler doğrudan RAM üzerinde işlenir.
* **Gerçekçi Simülasyon:** İstanbul'un doğal gece/gündüz sıcaklık döngüsünü taklit etmek için sinüs dalgası tabanlı bir model kullanır.
* **Çift Eksenli Görselleştirme:** Sıcaklık (Derece) ve nemi (Yüzde) tek bir uyumlu grafik üzerinde gösterir.
* **Sıfır Ayak İzi:** Çalışma sonrası gereksiz dosya bırakmaz.

---

#  Tech Stack | Teknolojiler

* **Language:** Python
* **Data Science:** Pandas, NumPy
* **Visualization:** Matplotlib

---

#  How to Run | Nasıl Çalıştırılır

1. **Clone the repository | Depoyu indirin:**
   ```bash
   # Replace YOUR_USERNAME with your actual GitHub username
   git clone [https://github.com/YOUR_USERNAME/istanbul-weather-pipeline.git](https://github.com/YOUR_USERNAME/istanbul-weather-pipeline.git)
