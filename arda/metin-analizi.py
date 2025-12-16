"""girdiğiniz medinde hangi harften kaç tane olduğunuz gösteren program"""

metin=input("girdiğiniz metinde hangi harften ve rakamdan kaç tane olduğunuz bulmak için metni giriniz: ").lower()

for harf in set(metin):
    if harf.isalpha():
        print(harf,metin.count(harf))

for rakam in set(metin):
    if rakam.isdigit():
        print(rakam,metin.count(rakam))

for boşluk in set(metin):
    if boşluk.isspace():
        print("boşluk",metin.count(boşluk))
uzunluk=len(metin)


ortalanmış_metin=metin.center(10+uzunluk,"-")
print(ortalanmış_metin)
print(set(metin))
