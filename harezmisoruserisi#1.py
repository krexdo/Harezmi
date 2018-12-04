print("""****************
Mustafa Öksüz 4.12.2018 03.04
Harezmi Soru Serisi #1
****************
""")
def asal_mi(sayi):
    for i in range(2,sayi):
        if (sayi % i == 0 ):
            return False
    return True
def rakamlar_toplami(sayi):
    toplam = 0
    sayi = str(sayi)
    i = list(sayi)
    for x in sayi:
        toplam+= int(x)
    return toplam

i = 2
doğruluk = 0
çifte_asallar = []
while i<=10000:
    if asal_mi(i)==True:
        doğruluk+=1
    if asal_mi(rakamlar_toplami(i))==True:
        doğruluk+=1
    if doğruluk ==2:   
        çifte_asallar.append(i)

    doğruluk = 0
    i+=1
print("CEVAP: ",sum(çifte_asallar))
