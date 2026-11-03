# Soal 2 - Pengembangan Soal 1: ditambah bilangan minimum dan maksimum
# Pencarian min/maks memakai iterasi (tanpa min() dan max())

# --- Input data ---
while True:
    try:
        n = int(input("Berapa banyak bilangan yang ingin dimasukkan? "))
        if n > 0:
            break
        print("Jumlah bilangan harus lebih dari 0.")
    except ValueError:
        print("Masukkan bilangan bulat.")

bilangan = []
for i in range(n):
    while True:
        try:
            x = float(input(f"Bilangan ke-{i + 1}: "))
            bilangan.append(x)
            break
        except ValueError:
            print("Input harus berupa angka, coba lagi.")

# --- Total & banyak data ---
total = 0
banyak = 0
for x in bilangan:
    total = total + x
    banyak = banyak + 1

# --- Rata-rata ---
rata_rata = total / banyak

# --- Standar deviasi ---
jumlah_kuadrat = 0
for x in bilangan:
    selisih = x - rata_rata
    jumlah_kuadrat = jumlah_kuadrat + selisih * selisih

std_populasi = (jumlah_kuadrat / banyak) ** 0.5
std_sampel = (jumlah_kuadrat / (banyak - 1)) ** 0.5 if banyak > 1 else 0.0

# --- Minimum dan maksimum (iterasi) ---
minimum = bilangan[0]   # anggap elemen pertama sebagai nilai awal
maksimum = bilangan[0]
for x in bilangan:
    if x < minimum:
        minimum = x
    if x > maksimum:
        maksimum = x

# --- Output ---
print("\n=== HASIL ===")
print("Data               :", bilangan)
print(f"Total              : {total:.2f}")
print(f"Rata-rata          : {rata_rata:.2f}")
print(f"Std. deviasi (pop) : {std_populasi:.4f}")
print(f"Std. deviasi (smp) : {std_sampel:.4f}")
print(f"Bilangan minimum   : {minimum:.2f}")
print(f"Bilangan maksimum  : {maksimum:.2f}")