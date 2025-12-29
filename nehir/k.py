print("--- AKILLI DEPOYA HOŞ GELDİNİZ --")

envanter = {
    "İphone 15" : {"stok": 10, "fiyat": 55000},
    "MacBook Air" : {"stok": 5, "fiyat": 42500},
    "AirPords Pro" : {"stok": 25, "fiyat": 7500},
    "Samsung Monitör" : {"stok": 8, "fiyat": 12000},
    "Logitech Mouse" : {"stok": 50, "fiyat": 1200}
    }

def stok_listele():
    print("\n--- TEKNOLOJİ MAĞZASI STOK DURUMU ---")
    for urun, bilgiler in envanter.items():
        stok_miktari = bilgiler["stok"]
        fiyat = bilgiler["fiyat"]

        cikti = f"Ürün: {urun} | Stok: {stok_miktari} | Fiyat: {fiyat} TL"

        if stok_miktari < 10:
            cikti += "--> [STOK AZALDI!]"
        
        print(cikti)

    print("-" * 40)

stok_listele()

def stok_ekle(urun_adi, adet):
    
    if urun_adi in envanter:
        
        envanter[urun_adi]["stok"] += adet
        print(f"\nBAŞARILI: {urun_adi} stoğu {adet} adet artırıldı.")
        print(f"Yeni Stok: {envanter[urun_adi]['stok']}")
    else:
        
        print(f"\nHATA: '{urun_adi}' envanterde bulunamadı!")
        print("Lütfen önce yeni_urun_tanimla fonksiyonunu kullanın.")


stok_ekle("MacBook Air", 10)


stok_ekle("iPad Pro", 5)


stok_listele()

# Kasa (Toplam Ciro) için bir değişken tanımlayalım
toplam_ciro = 0

def satis_yap(urun_adi, adet):
    global toplam_ciro # Fonksiyon dışındaki toplam_ciro'yu güncelleyebilmek için
    
    
    if urun_adi not in envanter:
        print(f"\nHATA: '{urun_adi}' dükkanda satılmamaktadır.")
        return

    
    mevcut_stok = envanter[urun_adi]["stok"]
    if adet > mevcut_stok:
        print(f"\nHATA: Yetersiz stok! {urun_adi} için sadece {mevcut_stok} adet var.")
        return

    
    
    birim_fiyat = envanter[urun_adi]["fiyat"]
    satis_tutari = adet * birim_fiyat
    
    # Stoktan düşelim
    envanter[urun_adi]["stok"] -= adet
    
    
    toplam_ciro += satis_tutari
    
    print(f"\n✅ SATIŞ BAŞARILI!")
    print(f"Satılan: {adet} adet {urun_adi}")
    print(f"Toplam Tutar: {satis_tutari} TL")
    print(f"Kalan Stok: {envanter[urun_adi]['stok']}")


satis_yap("iPhone 15", 2)  
satis_yap("AirPods Pro", 30) 
satis_yap("Ekmek", 1)        

print(f"\n💰 GÜNCEL KASA TOPLAMI: {toplam_ciro} TL")