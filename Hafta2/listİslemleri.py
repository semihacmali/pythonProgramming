sayi_listesi = list(range(0,100))
#ciftsayilari yazdirmak istersek
sayi_listesi[0::2]
#tek sayilari yazdirmak istersek
sayi_listesi[1::2]


ilkArray = [56, 41.6, True, 5, 'yiu']

#varolan bir diziye eleman ekleme
ilkArray.append("Python") #listenin sonuna ekleme yapar

ilkArray.insert(1, "Java") # verilen index e degeri ekler

#varolan bir diziden eleman silme
ilkArray.remove(5)
ilkArray.remove(52) #listenin icerisinde bulunan bir degeri silebiliriz


ilkArray.pop() #dizinin son elemanini siler


#Python for dongusu tanimlama
#diger dillerdeki genel tanimlama
for(int i = 0; i < 50; i++){
    print(i)
}
#pythondaki tanimlama
for i in range(0,50):
    print(i)


ikinciArray = [98, 45, 12, 65, 1, 23, 41]

toplam = 0
for eleman in ikinciArray:
    toplam = toplam + eleman
#len(degiskenAdi) dizinin eleman uzunlugunu verir
aritmatikOrt = toplam / len(ikinciArray)

