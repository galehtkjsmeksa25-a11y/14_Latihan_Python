def cek_bilangan():
    while True:
        print("===== PROGRAM CEK BILANGAN =====")

        angka = int(input("Masukkan sebuah bilangan: "))

        if angka % 2 == 0:
            print("Bilangan", angka, "adalah GENAP")
        else:
            print("Bilangan", angka, "adalah GANJIL")

        pilihan = input("Apakah ingin mengulang? (y/n): ")

        if pilihan.lower() == "n":
            print("Program selesai.")
            break


cek_bilangan()