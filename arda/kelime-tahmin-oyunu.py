"""öncelikle kendin 10 tane kelime belirle ve program o kelimelerden 1 tanesini seçsin kullanıcıda  harf girerek o kelimeyi 
tahmin etmeye çalışıcak kelime adana olsun kullanıcı a girerse a_a_a olarak kullanıcıya gösterilicek kullanıcının kelimeyi 
bilmek için belli bi hakkı olucak """

kelimeler=["müzakere","ihtiras","resital","assolist","teftiş","prosedür","mecal","küstah","ukala","aheste","sükunet","mazlum",
           "hakkaniyet","mapus","izdivaç","valide","inkılap","haset","avutmak","paravan","izah","züppe","içerlemek","sersefil"
           ,"işkillenmek","moloz","namert","usanmak","mütemadiyen","ihtisas","mukayese","münhasır"]

import random
harfListe=[]
kelimem=random.choice(kelimeler)
kelimeminUzunluğu=len(kelimem)
print(f"tahmin etmeniz istenen kelimenin uzunluğu: {kelimeminUzunluğu} ")
print("_ "*kelimeminUzunluğu)
liste_kelimem=list(kelimem)
hak=8
tahminListesi=[]
print("kelimeyi doğru tahmin etmek için 8 hakkınız var")
harf=input("kelimeyi tahmin etmek için tek bir harf girin: ").lower()
harfListe.append(harf)
if harf not in liste_kelimem:
    hak -= 1
    print(f"yanlış oldu {hak} hakkınız kaldı")
for x in liste_kelimem:
        if x!=harf:
            tahminListesi.append("_ ")
        else:
            tahminListesi.append(harf)
print(tahminListesi)
j=0
while 0<hak:
    harf=input("kelimeyi tahmin etmek için tek bir harf girin: ").lower()
    if harf in harfListe:
        print("girdiğiniz harfi zaten daha önce girdiniz.")
        continue
    harfListe.append(harf)
    for x in liste_kelimem:

        if harf not in liste_kelimem:
            hak-=1
            print(f"yanlış oldu {hak} hakkınız kaldı")
            break
        else:
            for j in range(kelimeminUzunluğu):
                if  tahminListesi[j] == "_ " and liste_kelimem[j] == harf:
                    tahminListesi[j] = harf
    if tahminListesi==liste_kelimem:
        print("tebrikler kelimeyi bildiniz. ")





    print(tahminListesi)
    
    