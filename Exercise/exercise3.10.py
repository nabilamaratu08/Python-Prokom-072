mountains = ['Everest', 'Bromo', 'Fuji']
print(mountains)
 
mountains.append('Rinjani')           # tambah di akhir
mountains.insert(1, 'Semeru')         # sisip di posisi 1
print(mountains)
 
mountains.remove('Fuji')              # hapus berdasarkan nilai
print(mountains)
 
last = mountains.pop()                # hapus & ambil elemen terakhir
print(f"Popped: {last}")
 
del mountains[0]                      # hapus berdasarkan indeks
print(mountains)
 
mountains.extend(['Merapi', 'Rinjani', 'Fuji'])
print(mountains)
 
print(f"Sorted (temporary): {sorted(mountains)}")
mountains.sort()                      # urut permanen
print(f"After sort(): {mountains}")
mountains.reverse()                   # balik urutan
print(f"After reverse(): {mountains}")
 
print(f"Length: {len(mountains)}")
print(f"Last item via [-1]: {mountains[-1]}")