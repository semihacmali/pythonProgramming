# class Ogrenci:
#     id = 0
#     ad = "Boş"
#
# o1 = Ogrenci()
# o2 = Ogrenci()
# print(type(o1)) # ogrenci class'i turundedir
# print(o1.id)
# print(o1.ad)
#
# #Referans ile atama islemi
# o1.id = 253
# o1.ad = "Metehan"
#
#
# o2.ad = "Batuhan"
# o2.id = 326
#
# print("O1 nesnesinin degerleri")
# print(o1.id)
# print(o1.ad)
# print("O2 nesnesinin degerleri")
# print(o2.ad)
# print(o2.id)

#
class Insan:
    ad = "Girilmedi"
    soyad = "Girilmedi"
    yas = 0
    def degerAtama(self, gelenAd, gelenSoyisim, gelenYas):
        self.ad = gelenAd
        self.soyad = gelenSoyisim
        self.yas = gelenYas

    def dogumYili(self):
        dogumyili = 2022 - self.yas
        return dogumyili
# i1 = Insan()
# print("{} \t {} \t {}".format(i1.ad, i1.soyad, i1.yas))
# i1.degerAtama("Mert","Yaşar", 21)
# print("{} \t {} \t {}".format(i1.ad, i1.soyad, i1.yas))
# print("{} \t {} \t {} \t {} ".format(i1.ad, i1.soyad, i1.yas, i1.dogumYili()))



##### butun get ve set lerini olusturun
class Motosiklet:
    marka = "Girilmedi"
    model = "Girilmedi"
    beygir = 0
    motorHacmi = 0.0

    def __init__(self, marka, model, beygir, motorHacmi):
        self.marka, self.model, self.beygir, self.motorHacmi = marka, model, beygir, motorHacmi

    def getMarka(self):  #### eger bir degiskenin degeri metod ile okunacaksa o metodun ismi getDegiskenAdi
        return self.marka

    def setModel(self, yeniModel): ##### eger bir degiskenin degeri metod ile guncellenecekse o metodun ismi setDegiskenAdi
        self.model = yeniModel

m1 = Motosiklet("Suzuki", "Hayabusa", 196, 1300)
print("{} \t {} \t {} \t {}".format(m1.marka, m1.model, m1.motorHacmi, m1.beygir))
m1.model = "Gsx-r"
print("{} \t {} \t {} \t {}".format(m1.marka, m1.model, m1.motorHacmi, m1.beygir))

print(m1.getMarka())

m1.setModel("GSR")
print("{} \t {} \t {} \t {}".format(m1.marka, m1.model, m1.motorHacmi, m1.beygir))