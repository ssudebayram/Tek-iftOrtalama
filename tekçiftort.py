tekAdet = 0
ciftAdet = 0
tekToplam = 0
ciftToplam = 0

n = int(input("Kaç Adet Sayı Girilecek : "))
for i in range(n):
    sayi = int(input("Sayı : "))
    if (sayi % 2 == 0):
        tekAdet += 1
        tekToplam += sayi
    else:
        ciftAdet += 1
        ciftToplam += sayi
if (tekAdet != 0):
    print("Tek Sayıların Ortalaması : ", tekToplam / tekAdet)
if (ciftAdet != 0): 
    print("Çift Sayıların Ortalaması : ", ciftToplam / ciftAdet)