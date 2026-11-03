# import geometri as geo
from matematika.geometri import luasLingkaran, luasPersegi, volTabung

jari2 = float(input("masukkan jari-jari lingkaran: "))
tinggi = float(input("masukkan tinggi tabung: "))
#volTab = geo.volTabung(geo.luasLingkaran(jari2), tinggi)
volTab = volTabung(luasLingkaran(jari2), tinggi)

panjang = float(input("masukkan panjang persegi: "))
lebar = float(input("masukkan lebar persegi: "))
luasP = luasPersegi(panjang, lebar)

print("Volume Tabung:", volTab)
print("Luas Persegi:", luasP)
