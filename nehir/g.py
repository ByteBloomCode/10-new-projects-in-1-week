import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
gunluk_degisim = np.random.normal(loc=1.001 , scale=0.02 , size=30)
fiyatlar = 100 * np.cumprod(gunluk_degisim)

gunler = pd.date_range(start="2024-01-01" ,  periods=30)

df = pd.DataFrame({
    "Tarih": gunler,
    "Fiyat": fiyatlar
})

print(df.head())

en_yuksek = df["Fiyat"].max()
print(f"Zirve fiyatımız: {en_yuksek}")

yuksek_gunler = df[df["Fiyat"] > 105]
print("\nFiyatın 105 TL'yi geçtiği günler:")
print(yuksek_gunler)

print("\nTablomuzun genel özeti:")
print(df.describe())

plt.figure(figsize=(12, 5))
plt.plot(df["Tarih"], df["Fiyat"], color="blue", marker="o", linestyle="-", label="Günlük Fiyat")
plt.title("30 Günlük Hisse Senedi Takibi" , fontsize=14)
plt.xlabel("Tarih")
plt.ylabel("Tarih")
plt.grid(True)
plt.legend()
plt.show()