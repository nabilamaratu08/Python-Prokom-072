def luassegitiga(alas: float, tinggi: float)->float:
    luas = 0.5*alas*tinggi
    return luas

def luaskotak(panjang: float, lebar: float)->float:
    luas = panjang*lebar
    return luas


ls_segitiga= luassegitiga(20,100)
ls_kotak= luaskotak("wk ",100)
print(ls_segitiga)
print(ls_kotak)
