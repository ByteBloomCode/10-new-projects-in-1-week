import random

#1- Tahtanın sınırlarını belirleyelim:

genislik = 20
yukseklik = 10

#2- Yılanın konumu: oyun başladığında yılan tahtanın rastgele bir yerinde olsun.

yilan_x = random.randint(0,genislik-1)          #-1 dememizin nedeni bilgisayarın saymaya 0 dan başlaması.
yilan_y = random.randint(0,yukseklik-1)

#3- Yemin konumu: oyun başladığında yem de rastgele bir yerde belirsin.

yem_x = random.randint(0,genislik-1)          
yem_y = random.randint(0,yukseklik-1)

def tahtayi_çiz():
    print("#"*(genislik+2))        #Daha estetik gözükmesi için

    #--DIŞ DÖNGÜ: SATIRLAR (y kordinatı)--
    
    for y in range(yukseklik):
        print("#" , end="")       #Her satırın en başındaki sol duvar

        #--İÇ DÖNGÜ: SÜTUNLAR (x kordinatı)--
        
        for x in range(genislik):
            #Bilgisayara şuan ki hücrede yılan ya da yem var mı diye soruyoruz:
            if x == yilan_x and y == yilan_y:
                print("S" , end="")
            elif x == yem_x and y == yem_y:
                print("*" , end="")
            else:
                print("." , end="")
        print("#")

    print("#"*(genislik+2))


while True:
    
    tahtayi_çiz()

    komut = input("HAREKET: A: Sola , S: Aşağıya , W: Yukarı , D: Sağa , Q: Çıkış").upper()

    if komut == "W":
        yilan_y-=1
    elif komut == "S":
        yilan_y+=1
    elif komut == "A":
        yilan_x-=1
    elif komut == "D":
        yilan_x+=1
    elif komut == "Q":
        print("Oyundan çıkılıyor...")
        break
    

if yilan_x == yem_x and yem_x and yilan_y == yem_y:
    print("Harika yemi yedin.")
    yem_x = random.randint(0,genislik-1)          
    yem_y = random.randint(0,yukseklik-1)


