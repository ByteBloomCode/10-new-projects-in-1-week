print("--- ORTALAMA HESAPLACIYA HOŞ GELDİNİZ ---")

birinci_not = float(input("Öğrencinin notunu giriniz:"))
ikinci_not = float(input("Öğrencinin notunu giriniz:"))
ucuncu_not = float(input("Öğrencinin notunu giriniz:"))

ortalama = (birinci_not + ikinci_not + ucuncu_not) / 3

istenilen_not_ortalamasi = round(ortalama,1)

print(istenilen_not_ortalamasi)