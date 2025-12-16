"""iki boyutlu bir yapı olucak satır ve sütun şeklinde kullanıcı satırın ve sütunun uzunluğunu giricek programda ona göre 
bir düzlem oluşturucak"""


satır = int(input("satırın uzunluğunu giriniz: "))
sütun = int(input("sütunun uzunluğunu giriniz: "))

satıryazısı = ""
i = 0

while i < satır:
    if i % 2 == 0:
        satıryazısı += "w "
    else:
        satıryazısı += "b "
    i += 1

j=0
while j<sütun:
    j+=1
    print(satıryazısı)
























