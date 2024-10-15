#alistirma 1
#Verilen string ifadenintümharflerinibüyükharfeçeviriniz.
#Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız
text = "The goal is to turn data into information, and information into insight."
new_string = ""
for i in text:
    if i == "," or i == ".":
        new_string += " "
    else:
        new_string += i

word_list = new_string.upper().split()
print(word_list)

#alistirma 2
#
lst = ["D","A","T","A","S","C","I","E","N","C","E"]
new_lst = []
print(len(lst))

print(lst[0])
print(lst[10])
new_lst = lst[:4]
print(new_lst)
lst.remove(lst[8])
print(lst)
lst.append("2")
print(lst)
lst.insert(8, "N")
print(lst)

#alistirma 3

dict = {'Christian' : ["America" , 18],
        'Daisy' : ["England" , 12],
        'Antonio' : ["Spain", 22],
        'Dante': ["Italy" , 25]}
print(dict.keys())
print(dict.values())
dict['Daisy'][1] = 13
print(dict)
dict.update({"Ahmed" : ["Turkey",24]})
print(dict)
dict.pop('Antonio')
print(dict)

#alistirma 4
#Argüman olarak bir liste alan,
# listenin içerisindeki tek ve çift sayıları ayrı listelere atayan
# ve bu listeleri return eden fonksiyon yazınız.

l = [2,13,18,24,25]
tek = []
cift = []
def func(l):
    for i in l:
        if i % 2 == 0:
            cift.append(i)
        if i % 2 == 1:
            tek.append(i)
    return cift, tek

print(func(l))

#alistirma 5

ogrenciler = ["Ali" ,"Veli" ,"Ayşe" , "Talat" , "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler,1):
    if index < 4:
        print(f"Mühendislik Fakültesi {index}. öğrenci: {ogrenci}" )
        continue
for index, ogrenci in enumerate(ogrenciler, -2):
    if index > 0:
        print(f"Tıp Fakültesi {index}. öğrenci: {ogrenci}")
        continue

#alistirma 6
#Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız

ders_kodu = ["CMP1005" , "PSY1001" , "HUK1005" , "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

zipped_list = list(zip(ders_kodu, kredi, kontenjan))
print(zipped_list)
for index, (kod, kredi, kontenjan) in enumerate(zipped_list):
    print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjanı {kontenjan} dir.")

#alistirma 7

kume1 = set(["data", "python"])
kume2 = set(["data", "function" ,"qcut","lambda", "python","miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume1))
else:
    print(kume2.difference(kume1))

#alistirma 8
#List Comprehension yapısı kullanarak car_crashes verisindeki
#numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz

import seaborn as sns
df = sns.load_dataset("car_crashes")
upper_car_columns = [f"NUM_{i.upper()}" for i in df.columns]
print(upper_car_columns)

#alistirma 9
#  List Comprehension yapısı kullanarak car_crashes verisinde isminde
#  "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız

modified_columns = [i.upper()+ "_FLAG" if "NO" not in i.upper() else i.upper() for i in df.columns]
print(modified_columns)

#alistirma 10
#List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden
# FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir data frame oluşturunuz

og_list = ["abbrev" , "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df)