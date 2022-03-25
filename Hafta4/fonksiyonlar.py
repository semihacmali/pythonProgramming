# Python dilinde fonksiyon tanimlamak icin defination(def)(tanimlama) ifadesini kullaniyoruz
# def fonksiyon-adi():
# fonksiyon-adi : degisken tanimlama icin gecerli olan tum kurallar gecerlidir
# () icerisine ise disardan alacagi degisken var ise onu yaziyoruz.
# disardan alinan degiskenler icin degisken turu tanimlamak zorunda degiliz
# : sonra alt satira gecerek bir tab boslugu birakilir ve fonksiyon icersindeki islemler yazilir

def ilkFunc():
    print("Disardan deger almayan ve geri deger dondurmeyen bir fonksiyon!")
    print("İkinci Cikti!")

ilkFunc()

#disardan bir tane String deger alsin ve bu degerin uzunlugunu ekrani yazdirsin

def secondFunc(metin): # metinin String bir ifade olmasini bekliyoruz
    uzunluk = str(len(metin))
    print("Girilen metnin Uzunlugu : " + uzunluk)

metin = "Alper Tunga"
secondFunc(metin)

dizi = [8, "asd", 9, "şlkasd", True, False, 's']
secondFunc(dizi)

sayi = 2
secondFunc(sayi)

karakter = 'x'
secondFunc(karakter)

# aritmetik ortalama; disaridan alinan bir dizinin icerisindeki sayilarin
# aritmetik ortalamasini alan fonksiyonu yaziniz.

def artOrt(dizi): # float ve int olanlari bulmam lazim
    for eleman in dizi:
        if not isinstance(eleman, bool) and (isinstance(eleman, int) or isinstance(eleman, float)):
            print(str(eleman) + " degeri  boolean degildir ve integerdir.")

dizi1 = [0, 1, 5, 5.7, 9.5,'a', "semih", True, "mert", 1.8, 8]

artOrt(dizi1)

def artOrt(dizi): # float ve int olanlari bulmam lazim
    toplam = 0
    sayac = 0
    for eleman in dizi:
        if not isinstance(eleman, bool) and (isinstance(eleman, int) or isinstance(eleman, float)):
            toplam = toplam + eleman
            sayac = sayac + 1
    if sayac > 0:
        sonuc = toplam / sayac # degerler toplaminin eleman sayisina orani
    else:
        print("Dizide hic sayisal bir ifade yoktur!")
        sonuc = "Tanimsiz"
    return sonuc

dizi2 = ["s","e", "y", "w", "m"]
artOrt(dizi2)

# girdi olarak verilen iki farkli degiskenlere gore kuvvet alan fonksiyonu yaziniz.

def kuvvet(taban,ust):
    return taban ** ust

sayi1 = 5
sayi2 = 3

sonuc = kuvvet(sayi2, sayi1) # 3 ** 5
print(sonuc)

sonuc2 = kuvvet(ust = sayi2, taban = sayi1) # 5 ** 3
print(sonuc2)

#fonksiyonlardaki girdi degiskenlerine default(varsayılan) olarak bir deger verilebilir.
#eger fonksiyon cagirilirken bu degiskene deger girilmezse burada tanimlanan ifade gecerli olur
def thirdFunc(metin = "Girilmedi"):
    print("Fonksiyon Ciktisi : " + str(metin))

thirdFunc()
thirdFunc(8)
thirdFunc("Metin Girildi")