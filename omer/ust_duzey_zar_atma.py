import numpy as np


zar = np.array([]) 
adet = int(input("Kaç defa zar atılsın? \n Cevap: "))
for i in range(1,adet+1):
    zar = np.append(zar, np.random.randint(1,7,1)).astype(int)
toplam = zar.sum()
ortalama = zar.sum() / adet
print(f"Atılan Zarlar: {zar}")
print(f"Atılan Zarların Toplamı: {toplam}")
print(f"Atılan Zarların Ortalaması: {ortalama}")