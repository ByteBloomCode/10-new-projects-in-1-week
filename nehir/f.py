import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gunler = ["Pazartesi", "Salı", "Çarşamba" , "Perşembe" , "Cuma"]
sicakliklar = []

print("--- 5 Günlük Hava Durumu Giriş Paneli ---")

for gun in gunler:
    while True: #Geçerli bir sayı girine kadar sormaya devam et
        try:
            veri = input(f"{gun} günü için beklenen sıcaklığı girin (°C)")
            derece = float(veri) #input tan gelen stringi sayıya çeviriyoruz

            #Karar Yapısı : Mantıksız bir değer girilirse uyar
            if -60 < derece < 60:
                sicakliklar.append(derece)
                break
            else:
                print("Lütfen -60 ile +60 arasında mantıklı bir değer girin.")
        except ValueError:
            print("Hata! Lütfen harf değil, bir sayı giriniz.")

    
sicaklik_np = np.array(sicakliklar)

enerji_tuketimi = np.where(sicaklik_np > 25, (sicaklik_np*2), (sicaklik_np * 1.2 + 10))
df = pd.DataFrame({
        "Gün": gunler,
        "Sıcaklık": sicakliklar,
        "Tahmini_Enerji_kWh" : enerji_tuketimi
    })

print("\n--- Haftalık Analiz Özeti ---")
print(f"En Yüksek Sıcaklık: {df["Sıcaklık"].max()} °C")
print(f"Ortalama Enerji Tüketimi: {df["Tahmini_Enerji_kWh"].mean():.2f} kWh")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,8))

ax1.plot(df["Gün"], df["Sıcaklık"], marker="o" , linestyle="-" , color="orange" , label= "Sıcaklık")
ax1.set_title ("5 Günlük Sıcaklık Tahmini")
ax1.set_ylabel("Derece (°C)")
ax1.grid(True, alpha=0.3)

ax2.bar(df["Gün"], df["Tahmini_Enerji_kWh"] , color="royalblue" , label= "Enerji Tüketimi")
ax2.set_title("SIcaklığa Bağlı Tahmini Enerji Tüketimi")
ax2.set_ylabel("Tüketim (kWh)")

plt.tight_layout() #Grafik başlıkları birbirine girmesin
plt.show()
