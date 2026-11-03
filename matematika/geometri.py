def luasPersegi(panjang, lebar):
    luas = panjang * lebar
    return luas

def luasLingkaran(jari_jari):
    pi = 3.14
    luas = pi * (jari_jari ** 2)
    return luas

def volTabung(luas, tinggi):
    volume = luas * tinggi
    return volume

def main():
    jari2 = float(input("masukkan jari-jari lingkaran: "))
    tinggi = float(input("masukkan tinggi tabung: "))
    volTab = volTabung(luasLingkaran(jari2), tinggi)
    print(volTab)

#print(__name__)

if __name__ == "__main__":
    main()

volTab = volTabung(luasLingkaran (7), 14)
print(volTab)

luasP = luasPersegi(14, 7)
print(luasP)

luasL = luasLingkaran(7)
print(luasL)
