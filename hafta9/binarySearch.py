# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import time
dizi1 = [5,8,7,1,35,42,32,12,56,45,21,326,20,28,54]

arananEleman = 1
######## Linear Arama #############
for diziDeger in dizi1:
    if arananEleman == diziDeger:
        print("Aranan Eleman Dizinin İcerisinde Vardir")
        break
    print("{} icin for calisti".format(diziDeger))

arananDegerIndex = ""
bulunmaDurumu = False
for index in range(0,len(dizi1)):
    if arananEleman == dizi1[index]:
        bulunmaDurumu = True
        print("Aranan Deger Bulundu")
        arananDegerIndex = index
        break
if not bulunmaDurumu:
    print("Aranan Deger Dizinin İcerisinde Bulunmamaktadir.")


dizi1.sort()


def recursiveBinarySearch(arr, arananDeger):
    index = (int)(len(arr)/2) #ortadaki index i bul
    baslangic = 0
    bitis = len(arr)
    #ortanca = arr[index]
    if len(arr) < 1:
        return "Aranan Deger Dizinin İcerisinde Yoktur"
    if arr[index] == arananDeger:
        return "Aranan Deger Bulundu"
    elif arr[index] > arananDeger:
        return recursiveBinarySearch(arr[baslangic:index - 1], arananDeger)
    elif arr[index] < arananDeger:
        return recursiveBinarySearch(arr[index + 1:bitis], arananDeger)

        
dizi1 = random.sample(range(0,10000000), 1000000)
dizi1.sort()
arananEleman = dizi1[len(dizi1)-1]

basla = time.time()
arananDegerIndex = ""
bulunmaDurumu = False
for index in range(0,len(dizi1)):
    if arananEleman == dizi1[index]:
        bulunmaDurumu = True
        print("Aranan Deger Bulundu")
        arananDegerIndex = index
        break
if not bulunmaDurumu:
    print("Aranan Deger Dizinin İcerisinde Bulunmamaktadir.")
bitis = time.time()
print("Linear Search Süresi {}".format(bitis-basla))

basla = time.time()
recursiveBinarySearch(dizi1, arananEleman)
bitis = time.time()
print("Binary Search Süresi {}".format(bitis-basla))
0.15623998641967773/0.04684305191040039
