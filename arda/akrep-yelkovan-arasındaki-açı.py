

zaman=input("saati arasında tek bir nokta olucak şekilde giriniz.  mesela 4.5 , 8.32 gibi: ").strip()
zaman_liste=zaman.split(".")
i=0
j=0
while i<24:
    if int(zaman_liste[0])==i:
        while j<60:
            if  int(zaman_liste[1])==j:
                açı=(abs(j*6-30*i-(j/2)))
                if açı>=180:
                    print("saatin akrebi ve yelkovanı arasındaki açı ",abs(360-açı) ,"derece")
                else:
                    print("saatin akrebi ve yelkovanı arasındaki açı ", açı, "derece")
                break
            else:
                j+=1
        i+=1
    else:
        i+=1
if int(zaman_liste[0])>=24 or int(zaman_liste[1])>=60:
    print("yanlış sayıyı girdiniz öyle bir saat olamaz")



