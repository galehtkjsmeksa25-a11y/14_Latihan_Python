import importlib.util
import os

def muat_modul(nama_file, nama_modul):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), nama_file)
    spec = importlib.util.spec_from_file_location(nama_modul, path)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


ganjil_genap = muat_modul("Ganjil genap v2.py", "ganjil_genap")
bangun_datar = muat_modul("bangun datar14.py", "bangun_datar")
bangun_ruang = muat_modul("bangun ruang14.py", "bangun_ruang")

cek_bilangan = ganjil_genap.cek_bilangan
cek_prima = ganjil_genap.cek_prima
hitung_persegi = bangun_datar.hitung_persegi
hitung_persegi_panjang = bangun_datar.hitung_persegi_panjang
hitung_kubus = bangun_ruang.hitung_kubus
hitung_balok = bangun_ruang.hitung_balok


def menu():
    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Cek Bilangan Ganjil/Genap")
        print("2. Cek Bilangan Prima")
        print("3. Hitung Persegi")
        print("4. Hitung Persegi Panjang")
        print("5. Hitung Kubus")
        print("6. Hitung Balok")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            cek_bilangan()
        elif pilihan == "2":
            cek_prima()
        elif pilihan == "3":
            hitung_persegi()
        elif pilihan == "4":
            hitung_persegi_panjang()
        elif pilihan == "5":
            hitung_kubus()
        elif pilihan == "6":
            hitung_balok()
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    menu()