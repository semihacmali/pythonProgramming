vize = float(input("Vize Notunu Giriniz : ")) # inputlarin hepsi stringdir bunlar uygun veri turunedegistirilmelidir

final = float(input("Final Notunu Giriniz : "))

dersNotu = vize * 0.4 + final * 0.6

dersNotu = 85

if dersNotu < 50.0:
    print("Kaldi(DD)")
elif dersNotu < 60.0: #birinci durumu kontrol et eger birinci durum yanlis ise bu durumu kontrol et; birinci durum dogruysa bunu kontrol etme
    print("Sartli Gecti(DC)")
elif dersNotu < 70.0: # ustteki durumlar kontrol edilir eger ustteki durumlar yanlis ise bu kontrol edilir.
    print("Gecti(CC)")
elif dersNotu < 80.0:
    print("Basarili Gecti(BB)")
else: # ustteki durumlardan hicbiri dogru degilse bunu calistir
    print("Ustun Basari(AA)")

#devamsizliga gore ders durumu ciktisi
devamsizlik = float(input("Devamsizlik Giriniz : "))

if dersNotu < 50.0 or devamsizlik > 5: # or ('|') operatoru birden fazla durumu 'yada(veya)' mantiksal operatorune gore birlestirir ve ikisinden biri dogruysa dogru sonucunu uretir.
    print("Kaldi...")

print(dersNotu < 50.0 or devamsizlik > 5)

dersNotu = 72
if (dersNotu > 70.0 and dersNotu < 80.0): # and('&') operatoru birden fazla durumu 've' mantiksal operatorune gore birlestirir ve ikisi de dogru ise dogru sonucunu uretir.
    print("Basarili Gecti(BB)")


if not dersNotu < 50.0: # not('!') operatoru durumun tersini almak icin kullanilir
    print("Geçti...")


print("semih" == 'semih') # tek esittir sagdaki ifadeyi soldaki ifadeye atar
                          # iki esittir sagdaki ifadeyle soldaki ifadeyi karsilastirir ve true(dogru)/false(yanlis) sonuc uretir
print(50 != 50.0)  # != (esit degil) verilen ifadeler birbirine esit degilse true cevirir

girisParolasi = "batuhanBurak"

parola = input("Parolanizi Giriniz : ")

if girisParolasi != parola:
    print("Parolaniz Yanlis")
else:
    print("Giris İslemi Basarili")

kullaniciAdi = "YiuBilPro"

girilenKullanici = input("Kullanici Adinizi Giriniz : ")

if kullaniciAdi == girilenKullanici and parola == girisParolasi:
    print("Giris İslemi Basarili")
else:
    print("Kullanici Adiniz veya Sifreniz Yanlis")
