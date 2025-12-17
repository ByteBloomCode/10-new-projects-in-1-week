import time

def buyuk_bilgi_yarismasi():
    print("Çöz bakalım 10'da kaç yapacaksın?")
    
    puan = 0
    
    sorular = [
        {
            "soru": "1. Python dosyalarının uzantısı nedir?",
            "A": "A) .pyt", "B": "B) .py", "C": "C) .pt",
            "dogru": "B"
        },
        {
            "soru": "2. Fizikte 'Kuvvet'in birimi nedir?",
            "A": "A) Joule", "B": "B) Watt", "C": "C) Newton",
            "dogru": "C"
        },
        {
            "soru": "3. Türkiye'nin başkenti neresidir?",
            "A": "A) İstanbul", "B": "B) Ankara", "C": "C) İzmir",
            "dogru": "B"
        },
        {
            "soru": "4. Elon Musk'ın uzay taşımacılığı şirketinin adı nedir?",
            "A": "A) NASA", "B": "B) Blue Origin", "C": "C) SpaceX",
            "dogru": "C"
        },
        {
            "soru": "5. Hangisi bir programlama dili DEĞİLDİR?",
            "A": "A) HTML", "B": "B) Python", "C": "C) Java",
            "dogru": "A"
        },
        {
            "soru": "6. Güneş sistemindeki en büyük gezegen hangisidir?",
            "A": "A) Mars", "B": "B) Jüpiter", "C": "C) Satürn",
            "dogru": "B"
        },
        {
            "soru": "7. Suyun deniz seviyesindeki kaynama noktası kaç derecedir?",
            "A": "A) 90", "B": "B) 100", "C": "C) 120",
            "dogru": "B"
        },
        {
            "soru": "8. Demir Adam (Iron Man) karakterinin gerçek adı nedir?",
            "A": "A) Tony Stark", "B": "B) Steve Rogers", "C": "C) Bruce Banner",
            "dogru": "A"
        },
        {
            "soru": "9. Pi sayısının ilk 3 basamağı nedir?",
            "A": "A) 3.14", "B": "B) 3.41", "C": "C) 3.12",
            "dogru": "A"
        },
        {
            "soru": "10. Hangisi bilgisayarın beyni olarak kabul edilir?",
            "A": "A) RAM", "B": "B) Harddisk", "C": "C) CPU (İşlemci)",
            "dogru": "C"
        }
    ]

    for soru in sorular:
        print(soru["soru"])
        print(soru["A"])
        print(soru["B"])
        print(soru["C"])
        
        cevap = input("Cevabınız (A/B/C): ").upper()
        
        if cevap == soru["dogru"]:
            print("DOĞRU!")
            puan += 10
        else:
            print(f"YANLIŞ! Doğru cevap {soru['dogru']} olacaktı.")
        
        print("-" * 10)
        time.sleep(1)

    # SONUÇ EKRANI
    print(f"\n🏁 YARIŞMA BİTTİ! TOPLAM PUANIN: {puan} / 100")
    
    if puan == 100:
        print("HELAAAALLLL! Hepsini bildin.")
    elif puan >= 70:
        print("Gayet başarılı, tebrikler.")
    elif puan >= 50:
        print("Fena değil, geçtin işte boşver.")
    elif puan >= 20:
        print("Biraz daha çalışman lazım reis.")
    else:
        print("Çok çalışman lazım baba daha çookk...")

buyuk_bilgi_yarismasi()