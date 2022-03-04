import math

print("Yiu")

sayi1 = 8

#Kuvvet Alma
4 ** 2

pow(4, 2)


# Ekran ciktisi alma ornegi
print("* * * * *")
print(" * * * * *")
print("* * * * *")
print(" * * * * *")
print("* * * * *")


print("* " * 5)
print(" *" * 5)
print("* " * 5)
print(" *" * 5)
print("* " * 5)

print(("* " * 5 + "\n" + " *" * 5 + "\n") * 2 + "* " * 5)

# Degisken turlerinin onemi
sayi2 = "5"
type(sayi2)
sayi2 * 5
float(sayi2) * 5

sayi3 = "Bilgisayar Programciligi 2.Sınıf"
int(sayi3)

sayi4 = "52365"
print(int(sayi4))

#farkli islem ve ifadeleri farklı degiskenlere atama
sayi1, sayi2, sayi3 = 12, "Yiu", 58623.54
print(sayi1)
print(sayi2)
print(sayi3)

#ayni islem veya ifadeyi farklı degiskenlere atama
sayi4 = sayi5 = 6

sayi6 = 562.51
print(round(sayi6))
#dilin duyarliligini olcmek icin kullanilabilir
#bu dil icin 15 basamaktır
print(10/3)

#round(sayisal ifade, virgulden sonra kac basamak olacağı)
print(round((10/3), 10))

#degisken isimlendirme
Q430 = 56 #buyuk veya kucuk harfle baslayabilir.
q430 = 55
_asd = 65 # alt cizgi kullanilabilir
ar-at = 89 # orta cizgi kullanilamaz.
ar at = 89 # degisken isminde bosluk birakilamaz.
54s = 65 #sayi ile baslayamaz.

#for, if, elif, while gibi dile ait ifadeler degisken olarak kullanilamaz
fora = 98 #onerilmez

girilenDeger = input("Degeri Giriniz : ")
type(girilenDeger)

girilenSayi = input("Sayisal Degeri Giriniz : ")
type(girilenSayi)
#input olarak alinan tum degerler 'String' turundedir

girilenSayi = int(input("Sayisal Degeri Giriniz : "))
type(girilenSayi)

girilenSayi1 = float(str(int(float(input("Sayisal Degeri Giriniz : ")))))
#sadece degisken degistirme yapiliyorsa en distaki degisken sonuc olarak atanir.
type(girilenSayi1)

# girilen iki sayidan birinciyi taban ikinciyi üst olarak alan
# matematiksel islemi yapiniz
sayi1 = float(input("Birinci Sayiyi Giriniz : "))

sayi2 = float(input("Ikinci sayiyi Giriniz : "))

print(sayi1 ** sayi2)
print(pow(sayi1, sayi2))


#Girilen 3 sayinin aritmatik ortalamasini hesaplayiniz.
sayi1 = int(input('Birinci Sayıyı Giriniz : '))

sayi2 = int(input('İkinci Sayıyı Giriniz : '))

sayi3 = int(input('Üçüncü Sayıyı Giriniz : '))


ortalama = (sayi1 + sayi2 + sayi3) / 3

print("Sayıların Ortalaması: ", ortalama)


#girilen iki sayinin modu alan uygulamayi yaziniz

sayi1 = int(input("Birinci Sayiyi Giriniz : "))

sayi2 = int(input("Ikinci Sayiyi Giriniz : "))

modSonuc = sayi1 % sayi2
print(modSonuc)

18%6

18%1

18%3


#Klavyeden girilen 4 Basamakli Sayinin basamak degerlerinin
#toplamını bulan uygulamayi yaziniz.
# Ornek : 5623 girilmis olsun
# Sonuc : 5 + 6 + 2 + 3 = 16

math.pi
#Dikdortgen alani ve Silindirin alanini bulan uygulamayi yaziniz.
#Dikdörtgen icin 2 adet girdi lazim
#Silindir icin 2 adet girdi ve PI sayisi lazim


