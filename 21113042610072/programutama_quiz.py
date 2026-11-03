def tampilkan_menu():
    print("\n=== PROGRAM TARIF PARKIR ===")
    print("1. Becak")
    print("2. Motor")
    print("3. Mobil")


def hitung_tarif(jenis, jam):
    if jenis == "1":
        return 1000

    elif jenis == "2":
        if jam <= 2:
            return 2000
        elif jam < 24:
            return 3000
        else:
            return 15000

    elif jenis == "3":
        if jam <= 2:
            return 4000
        elif jam < 24:
            return 6000
        else:
            return 20000

    return None


def tampilkan_hasil(jenis, jam, tarif):
    nama = {
        "1": "Becak",
        "2": "Motor",
        "3": "Mobil"
    }

    print("\n=== HASIL PARKIR ===")
    print("Jenis kendaraan :", nama[jenis])
    print("Lama parkir     :", jam, "jam")
    print(f"Total bayar     : Rp {tarif:,}".replace(",", "."))