"""marketin  bir envanter yapısı olucak mesela 
-ülker çikolatalı göfretten 10 tane 
-nutelladan 15 tane 
-lays fırından 18 tane 
-doritos baharatlı 22 tane 
-doritos peynirli 9 tane 
-eti janga dan 14 tane 
-sarelle fındık ezmesi 23 tane 
-eti popkek 28 tane var 
sonrasında ürünlerin her biri kullanıcıya teker teker 
sorulucak kullanıcı almak istiyorsa kaç tane almak iste
diğini almak istemiyosa almicam yazıcak
"""

market_envanteri={
    "ülker çikolatalı gofret: ": 10,
    "nutella: ": 15   ,
    "lays fırından":18,
    "doritos baharatlı: ":22,
    "doritos peynirli: ":9,
    "eti janga: ":14,
    "sarelle fındız ezmesi: ":23,
    "eti popkek: ": 28,
  }
i=-1
while i<7:
    i+=1
    y=list(market_envanteri.keys())
    x=list(market_envanteri.values())
    print(y[i],x[i])
    istiyormusun=input("üründen almak istiyormusunuz: (cevabınız evet/hayır olmalı)")
    if istiyormusun != "hayır" and istiyormusun!= "evet":
        print("evet veya hayır girin")
        i-=1
        continue
    elif istiyormusun==("hayır"):
        continue
    elif istiyormusun==("evet"):
        kaç_tane=int(input("kaç tane almak istiyorsun? "))
        azalan=int(x[i]) - int(kaç_tane)
        if azalan <0:
            print(f"markette o kadar {y[i]} yok")
            i-=1
            continue
        else:
            print(f"{y[i]} den {azalan} tane kaldı")

    










































