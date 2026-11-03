# Soal 1 - Menghitung total, rata-rata, dan standar deviasi menggunakan List
# Semua perhitungan memakai perulangan (tanpa sum(), mean(), stdev(), dll.)

# --- Input data ---
while True:
    try:
        n = int(input("Berapa banyak bilangan yang ingin dimasukkan? "))
        if n > 0:
            break
        print("Jumlah bilangan harus lebih dari 0.")
    except ValueError:
        print("Masukkan bilangan bulat.")

bilangan = []  # list kosong untuk menampung input
for i in range(n):
    while True:
        try:
            x = float(input(f"Bilangan ke-{i + 1}: "))
            bilangan.append(x)
            break
        except ValueError:
            print("Input harus berupa angka, coba lagi.")

# --- Total ---
total = 0
for x in bilangan:
    total = total + x

# --- Rata-rata ---
banyak = 0
for x in bilangan:          # menghitung banyak data tanpa len()
    banyak = banyak + 1
rata_rata = total / banyak

# --- Standar deviasi ---
# Rumus populasi: sqrt( sum((x - rata)^2) / n )
jumlah_kuadrat = 0
for x in bilangan:
    selisih = x - rata_rata
    jumlah_kuadrat = jumlah_kuadrat + selisih * selisih

std_populasi = (jumlah_kuadrat / banyak) ** 0.5

# Rumus sampel: sqrt( sum((x - rata)^2) / (n - 1) )
if banyak > 1:
    std_sampel = (jumlah_kuadrat / (banyak - 1)) ** 0.5
else:
    std_sampel = 0.0

# --- Output ---
print("\n=== HASIL ===")
print("Data               :", bilangan)
print(f"Total              : {total:.2f}")
print(f"Rata-rata          : {rata_rata:.2f}")
print(f"Std. deviasi (pop) : {std_populasi:.4f}")
print(f"Std. deviasi (smp) : {std_sampel:.4f}")