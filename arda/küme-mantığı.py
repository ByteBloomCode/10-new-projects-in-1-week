#2 tane küme olucak ve her bir kümeye kullanıcının istediği adette değer girilicek sonrasında kümelerin birleşimi(union)
# ve kesişimi(intersection)alınıcak.
print("bu program sizden 2 farklı kümenin değerlerini alır;kümelerin birleşimlerini ve kesişimlerini hesaplar.")
sayıkume1=int(input("1. küme için kaç değer gireceksiniz: "))
sayıkume2=int(input("2. küme için kaç değer gireceksiniz: "))
degerkume1=[]
degerkume2=[]
i=0
for x in range(0,sayıkume1):
    i+=1
    kume1=input(f"1. küme için {i}.değeri giriniz: ")
    degerkume1.append(kume1)

i=0
for y in range(0,sayıkume2):
    i+=1
    kume2=input(f"2. küme için {i}.değeri giriniz: ")
    degerkume2.append(kume2)

kume1_set=set(degerkume1)
kume2_set=set(degerkume2)

print("kümelerin birleşimleri: ",kume1_set.union(kume2_set))
print("kümelerin kesişimleri: ",kume1_set.intersection(kume2_set))

