data = input("Palindromluğunu kontrol etmek istediğiniz bir kelime veya cümle giriniz: ")

data_2 = data.lower()
if " " in data:
    data_2 = data_2.replace(" ", "")
data_3= data_2[::-1]
if data_2 == data_3:
    if data_2 == data_3 and data_2.find(" "):
        print(f"'{data_2}' cümlesi bir PALİNDROMDUR ve tersi '{data_3}' olur.")
    else:
        print(f"'{data_2}' kelimesi bir PALİNDROMDUR ve tersi '{data_3}' olur.")
elif " " in data:
    print(f"'{data_2}' cümlesinin tersi '{data_3}' olduğu için bir palindrom DEĞİLDİR.")
else:
    print(f"'{data_2}' kelimesinin tersi '{data_3}' olduğu için bir palindrom DEĞİLDİR.")