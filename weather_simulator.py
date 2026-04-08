import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 1. VERİ ÜRETİMİ (BELLEK ÜZERİNDE / IN-MEMORY)
def generate_weather_data(points=100):
    start_time = datetime.now()
    data = []
    
    print(f"Sistem: {points} veri noktası bellek üzerinde simüle ediliyor...")
    
    for i in range(points):
        # Her 30 dakikada bir veri kaydı simülasyonu
        timestamp = start_time + timedelta(minutes=i*30)
        
        # Matematiksel Modelleme: İstanbul sıcaklık dalgalanması (Sinüs Dalgası)
        # 18°C merkezli, +/- 5 derece sapmalı gerçekçi bir model
        temp = round(18 + 5 * np.sin(i * 0.2) + np.random.normal(0, 0.5), 1)
        
        # Nem modellemesi (Sıcaklıkla ters orantılı)
        humidity = int(50 + 15 * np.cos(i * 0.2) + np.random.randint(-5, 5))
        
        data.append({"Zaman": timestamp, "Sicaklik": temp, "Nem": humidity})
    
    return pd.DataFrame(data)

# 2. ANALİZ VE GÖRSELLEŞTİRME
def visualize_data(df):
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Sıcaklık Ekseni
    ax1.set_xlabel('Zaman Akışı (Simülasyon)')
    ax1.set_ylabel('Sıcaklık (°C)', color='red', fontweight='bold')
    ax1.plot(df['Zaman'], df['Sicaklik'], color='red', linewidth=2, label='Sıcaklık')
    ax1.fill_between(df['Zaman'], df['Sicaklik'], color='red', alpha=0.1)

    # Nem Ekseni
    ax2 = ax1.twinx()
    ax2.set_ylabel('Nem (%)', color='blue', fontweight='bold')
    ax2.plot(df['Zaman'], df['Nem'], color='blue', linestyle='--', alpha=0.6, label='Nem')

    plt.title("İstanbul Hava Durumu Simülasyonu (In-Memory Data Pipeline)", fontsize=14)
    
    # Grafiği GitHub için kaydet
    plt.savefig("weather_report.png", dpi=300)
    print("Sistem: 'weather_report.png' grafiği başarıyla oluşturuldu.")
    plt.show()

if __name__ == "__main__":
    weather_df = generate_weather_data(120) # 60 saatlik simülasyon
    visualize_data(weather_df)