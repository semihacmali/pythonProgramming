# for( int i = 0; i < 10; i++)

ad = "Semih"

for harf in ad:  # ad ifadesinin icerisindeki herbir elemani teker teker harf ifadesine ata ve islme yap
    print(harf)

print(list(range(0, 10)))
# for( int i = 0; i < 10; i++)

for i in range(0, 10):
    print(i)

# for( int i = 0; i < 20; i=i+2)
for j in range(0, 20, 2):  # range(baslangicDegeri, BitisDegeri, AtlamaMiktari)
    print(j)

meyveler = ["Kayisi", "Nektar", "Armut", "Domates"]

for k in meyveler:
    print(k)

for meyve in meyveler:
    for meyveharf in meyve:
        print(meyveharf)
    print("\n")

# 0 ile 128 arasindaki 5 e bölünebilen sayilari ekrana  yazdirin
for sayi in range(5,128,5):
    print(sayi)

#kullanicidan girilen degerler arasindaki 5 e bolunebilne sayilari bulunuz.
sayi1 = float(input("Birinci Sayiyi Giriniz : "))
sayi2 = float(input("İkinci Sayiyi Giriniz : "))

for sayi in range(int(sayi1), int(sayi2)):
    if sayi % 5 == 0:
        print(sayi)

modSonuc = sayi1 % 5

sayi1 = sayi1 + ( 5 - modSonuc)

for sayi in range(int(sayi1),int(sayi2),5):
    print(sayi)

# 1 ile 100 arasindaki sayilarin karelerini alan uygulamayi yaziniz.

kareler = [i**2 for i in range(0,101)]
print(kareler)

ikiKat5Fazla = [(i*2 + 5)/(i+2)  for i in range(0,101)]
print(ikiKat5Fazla)


############# WHILE ##############
m = 1
while m < 20:
    print(m**2 + 2*m + 5)
    m = m + 1


sayilar = [5,6,1,8,9,8,2,6,1,-1]

n = 0
while n < len(sayilar):
    print(sayilar[n])  # dizinin icerisindeki elemanlari index ile gezmek icin [](koseli parantez) kullanilir
    n = n + 1

#verilen dizinin en kucuk ve en buyuk elemanlarini bulan kodu yaziniz.
sayilar = [5,6,1,8,9,8,2,6,1,-1]

enkucuk = sayilar[0]
enbuyuk = sayilar[0]

i = 1
while i < len(sayilar):
    if enkucuk > sayilar[i]:
        enkucuk = sayilar[i]
    i = i + 1
enkucuk

j = 1
while j < len(sayilar):
    if enbuyuk < sayilar[j]:
        enbuyuk = sayilar[j]
    j = j + 1
enbuyuk