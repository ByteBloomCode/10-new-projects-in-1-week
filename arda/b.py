import random
import string  #Harf karakter ve sayı setlerine hızlı erişim sağlamak için kullandık.

buyuk_harfler = string.ascii_uppercase
kucuk_harfler = string.ascii_lowercase
sayiler = string.digits
ozel_karakterler = string.punctuation

tum_karakterler = buyuk_harfler + kucuk_harfler + sayiler + ozel_karakterler

#Şifrenin güvenli olup olmadığını kontrol etmek için bir fonksiyon oluşturmamız gerekiyor.

def sifre_guvenli_mi (sifre):
    buyuk_harf_var_mi = any(char in string.ascii_uppercase for char in sifre)
    rakam_var_mi = any(char in string.digits for char in sifre)
    ozel_karakter_var_mı = any(cahr in string.punctuation for cahr in sifre)    #any fonksiyonu şifrenin içinde hiç var mı diye sorar.
                                                                         
    return buyuk_harf_var_mi and rakam_var_mi and ozel_karakter_var_mı          #üç değer de tru döndüğünde fonksiyonun değeride true dönecek.
    
print("------GÜVENLİ ŞİFRE ÜRETİCİYE HOŞ GELDİNİZ------")

while True:
    try:
        uzunluk = int(input("Şifreniz kaç karakterli olsun?(En az 8 karakterli olmalı!)"))

        if uzunluk >= 8:
            break                                                                #try-except: Python'da programda hata olursa programı kapatma uyarı mesajı göndermek için kullanılır.
        else:
            print("Güvenlik için en az 8 karakter girmelisiniz!!")
    except ValueError:
        print("Hata:Lütfen sadece rakam giriniz!!")

guvenli_sifre = ""  #Başlangıçta şifre boş

#--DIŞ DÖNGÜ(while)
#sifre_guvenli_mi fonksiyonu false döndüğü sürece döngü hep baştan başlar.

while not sifre_guvenli_mi(guvenli_sifre):

    deneme_sifresi = ""  #Her yeni denmede şifre sıfırdan başlar.

    #--İÇ DÖNGÜ--
    #Bu döngü kullanıcının girdiği uzunluk sayısı kadar döner.
    #Görevi karakter havuzundan rastgele karakterler seçip yan yana dizmek.

    for _ in range(uzunluk):
        rastgele_secilen = random.choice(tum_karakterler)
        deneme_sifresi+=rastgele_secilen
        guvenli_sifre = deneme_sifresi
    
print("\n" + "="*30)
print(f"GÜVENLİ ŞİFRE ÜRETİLDİ:{guvenli_sifre}")
print("="*30)




