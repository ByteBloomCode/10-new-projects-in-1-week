import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Verilerimizzz

harcamalar = {
    "Kategori" : ["Gıda", "Kira", "Ulaşım", "Eğlence", "Fatura", "Giyim", "Diğer"],
    "Miktar" : [2500, 12000, 1500, 3000, 2200, 1800, 900]
}

def butce_analiz(veriler, limit):
    print(f"---{limit} TL Üzerinden Harcamalar İnceleniyor---")

    #List Comprehension (Kısa döngü) ile yüksek harcamaları seçelim

    yuksek_harcamalar = [m for m in veriler["Miktar"] if m > limit]

    for miktar in veriler["Miktar"]:
        if miktar > limit:
            print(f"UYARI: {miktar} TL tutarındaki harcama limitini aşıyor!")
        else:
            print(f"Normal: {miktar} TL harcama makul")
    
    return sum(yuksek_harcamalar)

#Fonksiyonu çalıştıralım (Limitimiz 2500 TL olsun)

toplam_riskli = butce_analiz(harcamalar, 2500)

df = pd.DataFrame(harcamalar)

#Numpy ile her harcamanın toplam içindeki % oranını hesaplayalım

toplam_harcama = df["Miktar"].sum()
df["Yuzde_Pay"] = np.round((df["Miktar"] / toplam_harcama) * 100, 2)

print("\n--- Harcama Tablosu ---")
print(df)

plt.figure(figsize=(8, 8))
#autopct = "½1.1f%%" -> Dilimlerin üzerine yüzde yazar
plt.pie(df["Miktar"], labels=df["Kategori"], autopct="%1.1f%%", startangle=140, colors=plt.cm.Paired.colors)
plt.title("Aylık Harcama Dağılımı")
plt.show()