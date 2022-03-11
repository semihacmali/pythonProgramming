ilkString = "Bilgisayar Programciligi Programi"

type(ilkString)

ilkString[8] # köseli parantezin icerisine index yazilir
             # python indexlemeye 0(sifir) dan baslar
ilkString[0]

ilkString[5:10] #substring baslangic index : bitis index + 1

ilkString = "Bilgisayar Programciligi Programi"

bosluklar = []
for index in range(0,len(ilkString)):
    if(ilkString[index] == " "):
        bosluklar.append(index) #diziye eleman ekler

bolunmusIfade = []
baslangicIndex = 0
for bosluk in bosluklar:
    bolunmusIfade.append(ilkString[baslangicIndex:bosluk])
    baslangicIndex = bosluk + 1
bolunmusIfade.append(ilkString[baslangicIndex:]) #[baslangic index : ] verilen indexten son karaktere kadar yazar

print(ilkString[:10]) # [ : bitis index] baslangictan verilen bitis indexine kadar yazar

bolunmusMetin = ilkString.split() #default olarak(bir ifade girilmediginde) " "(bosluk)'a gore metni ayirir

print(bolunmusMetin)

ikinciMetin = "Batuhan, Burak, Emir, Emir K, Engincan, Mustafa"

bolunmusIsimler = ikinciMetin.split(",") # Eger bir ifade verilirse ona göre ayirma islemi yapar
bolunmusIsimler

ilkString
ilkbosluk = ilkString.find(" ") # ....find(aranan ifade, (optional)baslangic index, (optional)bitis index)
ikinciBosluk = ilkString.find(" ", ilkbosluk + 1)

ilkString.find("say")

#Bir metin icerisinde bir ifade ariyoruz ancak metinin ve aranacak ifadenin büyük veya küçük harfle yazildigini
#bilmiyoruz ama buna ragmen eslesen ifadeyi bulmamiz lazim

metin = input("Metni Giriniz : ")

aranacakIfade = input("Aranacak Ifadeyi Giriniz : ")

metin.lower() # metni kucuk harfe cevirir
aranacakIfade.lower()

metin.find(aranacakIfade) # eger -1 donuyorsa metinin icinde o ifade yoktur

metin.lower().find(aranacakIfade.lower()) #metin ile aranacak ifade aynı metin duzlemine cekilir

metin.upper().find(aranacakIfade.upper()) #metin ile aranacak ifade aynı metin duzlemine cekilir

metin.isnumeric() #metnin sayi icerip icermedigini bulur

metin2 = input("Sayi Giriniz : ")

metin2.isnumeric()
int(metin2)

bolunmusIsimler

birlesikIsimler = ",".join(bolunmusIsimler) # ayrac ifadesi.join(birlestirilecek liste)
birlesikIsimler

birlesik2 = ",".join(bolunmusIsimler[:3])
birlesik2

#pythonda listelerde [baslangicindex:bitisindex:atlamaMiktari]
birlesik3 = ",".join(bolunmusIsimler[::2])
birlesik3