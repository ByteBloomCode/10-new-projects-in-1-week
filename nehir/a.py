"""
--SAYI TAHMİN OYUNU---ALGORİTMAM ---
1- START
2- TANIMLA gizli_sayi,tahmin,tahmin_hakkim=5,bilgisayarin_skoru=0,benim_skorum=0,devam,deneme_sayim
3- deneme_sayim = 5-tahmin_hakkim
4- devam = true
5- while(devam)
{

    while(tahmin_hakkim!=0)
     {
         YAZ("Lütfen tahmin ettiğiniz sayıyı giriniz:")
         if(tahmin>gizli_sayi)
        {
            tahmin_hakkim-=1
            YAZ("Daha küçük bir sayı deneyiniz.")
        }                                                              #Algoritmamda hatalar vardı değiştirmek zorunda kaldım sonradan kodu yazarken ama buraya yazdığım algoritmayı değiştirmedim o yüzden kod ve algoritma
                                                                        arasında bazı farklılıklar var.
        else if(tahmin<gizli_sayi)
        {
             tahmin_hakkim-=1                                                  
             YAZ("Daha büyük bir sayı deneyiniz.")
        }
        else
        {
            tahmin_hakkim-=1
            break
            YAZ("Tebrikler. {0} denemede doğru bildiniz." , deneme_sayim)
        }
     }
     
    if(tahmin_hakkim!=0)
         bemim_skorum+=1
    else
        bilgisayarın_skoru+=1
    
    devam = YAZ("Devam etmek istiyor musunuz?(true/false)")

    if(devam=false)
        break
}

6- YAZ("Oyun bitmiştir. Sizin skorunuz{0}\nbilgisiyarın skoru{1}\nOynadığınız için teşekkürler.")
7- STOP
"""

#KAYNAK KODUM

import random

print("SAYI TAHMİN OYUNUNA HOŞGELDİNİZ...")

devam = True
benim_skorum = 0
bilgisayarın_skoru = 0

while devam:
   
    gizli_sayi = random.randint(1,100)
    tahmin_hakkim = 5
    deneme_sayim = 0
    
    while tahmin_hakkim != 0:
        tahmin = int(input("Tahmin ettiğiniz sayıyı giriniz:"))
        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı giriniz!")
            tahmin_hakkim-=1
            deneme_sayim+=1
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı giriniz!")
            tahmin_hakkim-=1
            deneme_sayim+=1
        else:
            deneme_sayim+=1
            print(f"Tebrikler.{deneme_sayim} denemede sayıyı doğru bildiniz.")
            break
    
    if tahmin_hakkim != 0:
        benim_skorum+=1
    else:
        bilgisayarın_skoru+=1

    print(f"Skor durumu\nSizin skorunuz : {benim_skorum}\nBilgisayarın skoru : {bilgisayarın_skoru}")
    
    cevap = (input("Oyuna devam etmek istiyor musunuz?(E/H)"))

    if cevap == "H":
        devam = False




