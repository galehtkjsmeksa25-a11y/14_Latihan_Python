def hitung_kubus():
    print("===== HITUNG KUBUS =====")
    sisi = float(input("Masukkan panjang sisi kubus: "))

    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)

    print("Volume kubus:", volume)
    print("Luas permukaan kubus:", luas_permukaan)


def hitung_balok():
    print("===== HITUNG BALOK =====")
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))

    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

    print("Volume balok:", volume)
    print("Luas permukaan balok:", luas_permukaan)