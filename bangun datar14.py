def hitung_persegi():
    print("===== HITUNG PERSEGI =====")
    sisi = float(input("Masukkan panjang sisi persegi: "))

    luas = sisi ** 2
    keliling = 4 * sisi

    print("Luas persegi:", luas)
    print("Keliling persegi:", keliling)


def hitung_persegi_panjang():
    print("===== HITUNG PERSEGI PANJANG =====")
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    print("Luas persegi panjang:", luas)
    print("Keliling persegi panjang:", keliling)