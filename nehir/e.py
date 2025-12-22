import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Liste oluşturalım

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

#Ratgele 1000 ile 5000 arasında satış verileri oluşturalım.

satislar = np.random.randint(1000,5000,size=12)

performans = []

for satis in satislar:
    if satis>=3000:
        performans.append("Yüksek")
    else:
        performans.append("Düşük")

#Sonuçları görelim

print("="*20)
print(f"Satışlar: {satislar}")
print(f"Performans Notları: {performans}")

#Sözlük yapısını DataFrame'e dönüştürme

veri_sozlugu = {
    "ay": aylar,
    "satis_miktarı" : satislar,
    "durum" : performans
}

df = pd.DataFrame(veri_sozlugu)

#pandas fonksiyonlarıyla hızlı analiz

print(df.head())   #İlk 5 satırı yazdırır.
print(f"Toplam Satış: {df["satis_miktarı"].sum()}")
print(f"Ortalama Satış: {df["satis_miktarı"].mean()}")

plt.figure(figsize=(10,5))
plt.plot(df["ay"], df["satis_miktarı"], marker="o", color="b", linestyle="--")

#Grafik süsleme
plt.title("12 Aylık Satış Performansı")
plt.xlabel("Aylar")
plt.ylabel("Satış tutarı (TL)")
plt.grid(True)
plt.show()