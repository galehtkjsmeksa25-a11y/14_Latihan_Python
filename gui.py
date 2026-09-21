import tkinter as tk
from tkinter import messagebox

from ganjilgenap30 import cek_bilangan, cek_prima
from bangundatar30 import hitung_persegi, hitung_persegi_panjang
from bangunruang30 import hitung_kubus, hitung_balok
import database


# ---------- Helper umum ----------

def buka_window(judul, lebar=350, tinggi=300):
    """Membuat window baru (Toplevel) dengan judul & ukuran tertentu."""
    win = tk.Toplevel(root)
    win.title(judul)
    win.geometry(f"{lebar}x{tinggi}")
    win.resizable(False, False)
    return win


def ambil_float(entry, nama_field):
    try:
        return float(entry.get())
    except ValueError:
        messagebox.showerror("Input tidak valid", f"{nama_field} harus berupa angka.")
        return None


def ambil_int(entry, nama_field):
    try:
        return int(entry.get())
    except ValueError:
        messagebox.showerror("Input tidak valid", f"{nama_field} harus berupa bilangan bulat.")
        return None


def bersihkan_root():
    """Menghapus semua widget yang ada di root, dipakai saat pindah 'halaman'."""
    for widget in root.winfo_children():
        widget.destroy()


# ---------- Fitur 1-6: sama seperti sebelumnya ----------

def window_ganjil_genap():
    win = buka_window("Cek Ganjil / Genap", 300, 180)
    tk.Label(win, text="Masukkan bilangan:").pack(pady=(15, 5))
    entry_angka = tk.Entry(win)
    entry_angka.pack()
    label_hasil = tk.Label(win, text="", font=("Arial", 10, "bold"))
    label_hasil.pack(pady=15)

    def proses():
        angka = ambil_int(entry_angka, "Bilangan")
        if angka is None:
            return
        label_hasil.config(text=cek_bilangan(angka))

    tk.Button(win, text="Cek", command=proses).pack()


def window_prima():
    win = buka_window("Cek Bilangan Prima", 300, 180)
    tk.Label(win, text="Masukkan bilangan:").pack(pady=(15, 5))
    entry_angka = tk.Entry(win)
    entry_angka.pack()
    label_hasil = tk.Label(win, text="", font=("Arial", 10, "bold"))
    label_hasil.pack(pady=15)

    def proses():
        angka = ambil_int(entry_angka, "Bilangan")
        if angka is None:
            return
        label_hasil.config(text=cek_prima(angka))

    tk.Button(win, text="Cek", command=proses).pack()


def window_persegi():
    win = buka_window("Hitung Persegi", 300, 220)
    tk.Label(win, text="Panjang sisi:").pack(pady=(15, 5))
    entry_sisi = tk.Entry(win)
    entry_sisi.pack()
    label_hasil = tk.Label(win, text="", font=("Arial", 10, "bold"), justify="left")
    label_hasil.pack(pady=15)

    def proses():
        sisi = ambil_float(entry_sisi, "Panjang sisi")
        if sisi is None:
            return
        luas, keliling = hitung_persegi(sisi)
        label_hasil.config(text=f"Luas: {luas}\nKeliling: {keliling}")

    tk.Button(win, text="Hitung", command=proses).pack()


def window_persegi_panjang():
    win = buka_window("Hitung Persegi Panjang", 300, 260)
    tk.Label(win, text="Panjang:").pack(pady=(15, 0))
    entry_panjang = tk.Entry(win)
    entry_panjang.pack()
    tk.Label(win, text="Lebar:").pack(pady=(10, 0))
    entry_lebar = tk.Entry(win)
    entry_lebar.pack()
    label_hasil = tk.Label(win, text="", font=("Arial", 10, "bold"), justify="left")
    label_hasil.pack(pady=15)

    def proses():
        panjang = ambil_float(entry_panjang, "Panjang")
        if panjang is None:
            return
        lebar = ambil_float(entry_lebar, "Lebar")
        if lebar is None:
            return
        luas, keliling = hitung_persegi_panjang(panjang, lebar)
        label_hasil.config(text=f"Luas: {luas}\nKeliling: {keliling}")

    tk.Button(win, text="Hitung", command=proses).pack()


def window_kubus():
    win = buka_window("Hitung Kubus", 300, 220)
    tk.Label(win, text="Panjang sisi:").pack(pady=(15, 5))
    entry_sisi = tk.Entry(win)
    entry_sisi.pack()
    label_hasil = tk.Label(win, text="", font=("Arial", 10, "bold"), justify="left")
    label_hasil.pack(pady=15)

    def proses():
        sisi = ambil_float(entry_sisi, "Panjang sisi")
        if sisi is None:
            return
        volume, luas_permukaan = hitung_kubus(sisi)
        label_hasil.config(text=f"Volume: {volume}\nLuas permukaan: {luas_permukaan}")

    tk.Button(win, text="Hitung", command=proses).pack()


def window_balok():
    win = buka_window("Hitung Balok", 300, 320)
    tk.Label(win, text="Panjang:").pack(pady=(15, 0))
    entry_panjang = tk.Entry(win)
    entry_panjang.pack()
    tk.Label(win, text="Lebar:").pack(pady=(10, 0))
    entry_lebar = tk.Entry(win)
    entry_lebar.pack()
    tk.Label(win, text="Tinggi:").pack(pady=(10, 0))
    entry_tinggi = tk.Entry(win)
    entry_tinggi.pack()
    label_hasil = tk.Label(win, text="", font=("Arial", 10, "bold"), justify="left")
    label_hasil.pack(pady=15)

    def proses():
        panjang = ambil_float(entry_panjang, "Panjang")
        if panjang is None:
            return
        lebar = ambil_float(entry_lebar, "Lebar")
        if lebar is None:
            return
        tinggi = ambil_float(entry_tinggi, "Tinggi")
        if tinggi is None:
            return
        volume, luas_permukaan = hitung_balok(panjang, lebar, tinggi)
        label_hasil.config(text=f"Volume: {volume}\nLuas permukaan: {luas_permukaan}")

    tk.Button(win, text="Hitung", command=proses).pack()


# ---------- Halaman: Menu Utama (muncul SETELAH login berhasil) ----------

def tampilkan_menu_utama(nama_user, kelas_user):
    bersihkan_root()
    root.title("Menu Utama - Tugas Pemrograman")
    root.geometry("320x460")

    tk.Label(root, text="MENU UTAMA", font=("Arial", 14, "bold")).pack(pady=(15, 0))
    tk.Label(root, text=f"Login sebagai: {nama_user} ({kelas_user})",
             font=("Arial", 9), fg="gray").pack(pady=(0, 10))

    tombol_menu = [
        ("Cek Bilangan Ganjil/Genap", window_ganjil_genap),
        ("Cek Bilangan Prima", window_prima),
        ("Hitung Persegi", window_persegi),
        ("Hitung Persegi Panjang", window_persegi_panjang),
        ("Hitung Kubus", window_kubus),
        ("Hitung Balok", window_balok),
    ]

    for teks, aksi in tombol_menu:
        tk.Button(root, text=teks, width=30, command=aksi).pack(pady=4)

    tk.Button(root, text="Logout", width=30, fg="red",
              command=tampilkan_halaman_auth).pack(pady=(15, 0))


# ---------- Halaman: Login / Daftar (tampil PERTAMA kali) ----------

def tampilkan_halaman_auth():
    bersihkan_root()
    root.title("Login / Daftar - Tugas Pemrograman")
    root.geometry("320x360")

    tk.Label(root, text="SELAMAT DATANG", font=("Arial", 14, "bold")).pack(pady=(20, 15))

    tk.Label(root, text="Nama:").pack()
    entry_nama = tk.Entry(root, width=30)
    entry_nama.pack(pady=(0, 10))

    tk.Label(root, text="Password:").pack()
    entry_password = tk.Entry(root, width=30, show="*")
    entry_password.pack(pady=(0, 15))

    def proses_login():
        nama = entry_nama.get().strip()
        password = entry_password.get()

        if not nama or not password:
            messagebox.showerror("Input tidak lengkap", "Nama dan password harus diisi.")
            return

        try:
            hasil = database.cek_login(nama, password)
        except FileNotFoundError:
            messagebox.showerror(
                "Error",
                "File credentials.json tidak ditemukan.\n"
                "Pastikan file itu ada di folder yang sama dengan program ini."
            )
            return
        except Exception as e:
            messagebox.showerror("Error", f"Gagal cek login:\n{e}")
            return

        if hasil is None:
            messagebox.showerror("Login gagal", "Nama atau password salah.")
        else:
            tampilkan_menu_utama(hasil["nama"], hasil["kelas"])

    def buka_form_daftar():
        win = buka_window("Daftar Akun Baru", 320, 300)

        tk.Label(win, text="Nama:").pack(pady=(15, 0))
        entry_nama_baru = tk.Entry(win)
        entry_nama_baru.pack()

        tk.Label(win, text="Kelas:").pack(pady=(10, 0))
        entry_kelas_baru = tk.Entry(win)
        entry_kelas_baru.pack()

        tk.Label(win, text="Password:").pack(pady=(10, 0))
        entry_password_baru = tk.Entry(win, show="*")
        entry_password_baru.pack()

        label_status = tk.Label(win, text="", font=("Arial", 9), fg="green")
        label_status.pack(pady=10)

        def proses_daftar():
            nama_baru = entry_nama_baru.get().strip()
            kelas_baru = entry_kelas_baru.get().strip()
            password_baru = entry_password_baru.get()

            if not nama_baru or not kelas_baru or not password_baru:
                messagebox.showerror("Input tidak lengkap", "Nama, kelas, dan password harus diisi.")
                return

            try:
                timer = database.simpan_data(nama_baru, kelas_baru, password_baru)
                label_status.config(text=f"Akun tersimpan pukul {timer}")
                messagebox.showinfo("Berhasil", "Akun berhasil didaftarkan!\nSilakan login.")
                win.destroy()
                entry_nama.delete(0, tk.END)
                entry_nama.insert(0, nama_baru)
            except FileNotFoundError:
                messagebox.showerror(
                    "Error",
                    "File credentials.json tidak ditemukan.\n"
                    "Pastikan file itu ada di folder yang sama dengan program ini."
                )
            except Exception as e:
                messagebox.showerror("Error", f"Gagal mendaftarkan akun:\n{e}")

        tk.Button(win, text="Daftar", command=proses_daftar).pack()

    tk.Button(root, text="Login", width=20, command=proses_login).pack(pady=4)
    tk.Button(root, text="Daftar Akun Baru", width=20, command=buka_form_daftar).pack(pady=4)


# ---------- Entry point ----------

root = tk.Tk()
root.resizable(False, False)
tampilkan_halaman_auth()
root.mainloop()
