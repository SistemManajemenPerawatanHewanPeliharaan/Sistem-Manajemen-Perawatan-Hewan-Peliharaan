import pwinput
from prettytable import PrettyTable
import json
import os
import time


def simpan_akun(data):
    file_json = open("data_akun.json", "w")
    json.dump(data, file_json, indent=4)
    file_json.close()
    
def baca_akun():
    if not os.path.exists("data_akun.json"):
        return[]
    try:
        file_json = open("data_akun.json", "r")
        data = json.load(file_json)
        file_json.close()
        return data
    except json.JSONDecodeError:
        return[]

def registrasi():
    print("==============================")
    print("|    MENU REGISTRASI AKUN    |")
    print("==============================")

    data = baca_akun()

    username = input("Masukkan Username: ")
    
    for akun in data:
        if akun["username"] == username:
            print("Username sudah terdaftar! Silahkan gunakan username lain.")
            return
        
    password = pwinput.pwinput("Masukkan Password: ", mask = "*")

    akun_baru = {
        "username" : username,
        "password" : password,
        "role" : "pelanggan"
    }

    data.append(akun_baru)
    simpan_akun(data)
    print("Registrasi akun berhasil! Silahkan Login.")

def baca_data():
    if not os.path.exists("data_pelanggan.json"):
        return[]
    try:
        file_json = open("data_pelanggan.json", "r")
        data = json.load(file_json)
        file_json.close()
        return data
    except json.JSONDecodeError:
        return[]   

def simpan_data(data):
    file_json = open("data_pelanggan.json", "w")
    json.dump(data, file_json, indent=4)
    file_json.close()
    print("Data Berhasil Ditambahkan!")

def tambah_data():
    data = baca_data()
    telepon = input("Masukkan Nomor Telepon Pelanggan: ")
    nama_hewan = input("Masukkan Nama Hewan: ")
    jenis_hewan = input("Masukkan Jenis Hewan: ")
    umur_hewan = input("Masukkan umur hewan: ")
    paket_jasa = input("Masukkan Paket (A, B, C): ")

    pelanggan_baru = {
        "telepon" : telepon,
        "nama_hewan": nama_hewan,
        "jenis_hewan": jenis_hewan,
        "umur_hewan": umur_hewan,
        "paket_jasa": paket_jasa
    }

    data.append(pelanggan_baru)
    simpan_data(data)

def tampilkan_data():
    data = baca_data()

    if not data:
        print("Belum ada data pelanggan!")

    tabel = PrettyTable()
    tabel.field_names = ["No","No. Telepon","Nama Hewan", "Jenis Hewan", "Umur Hewan", "Paket Jasa" ]

    for index, p in enumerate (data, start=1):
        tabel.add_row([
            index,
            p.get("telepon"),
            p.get("nama_hewan"),
            p.get("jenis_hewan"),
            p.get("umur_hewan"),
            p.get("paket_jasa"),
        ])

    print(str(tabel))

def lihat_antrian():
    data = baca_data()

    if not data:
        print("Belum ada antrian perawatan saat ini.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No. Antrian","No. Telepon","Nama Hewan", "Jenis Hewan", "Umur Hewan", "Paket Jasa" ]

    for index, p in enumerate (data, start=1):
            tabel.add_row([
                index,
                p.get("telepon"),
                p.get("nama_hewan"),
                p.get("jenis_hewan"),
                p.get("umur_hewan"),
                p.get("paket_jasa"),
            ])
    print("============================================")
    print("|          DAFTAR ANTRIAN PETHOUSE         |")
    print("============================================")
    print(tabel)

def ubah_data():
    data = baca_data()
    if not data:
        print("Belum ada data pelanggan!")
        return

    tampilkan_data()

    try:
        #Cek apakah nomor index ada di dalam list data
        index = int(input("Masukkan nomor pelanggan yang ingin diubah: ")) - 1

        if 0 <= index < len(data):
            print(f"Mengubah data untuk hewan: {data[index]['nama_hewan']}")

            data[index]["telepon"] = input("Masukkan No. Telepon baru (Kosongkan jika tetap): ") or data[index]["telepon"]
            data[index]["nama_hewan"] = input("Masukkan Nama Hewan Baru (Kosongkan jika tetap): ") or data[index]["nama_hewan"]
            data[index]["jenis_hewan"] = input("Masukkan Jenis Hewan Baru (Kosongkan jika tetap): ") or data[index]["jenis_hewan"]
            data[index]["umur_hewan"] = input("Masukkan Umur Hewan Baru (Kosongkan jika tetap): ") or data[index]["umur_hewan"]
            data[index]["paket_jasa"] = input("Masukkan Paket Jasa Baru (A/B/C) (Kosongkan jika tetap): ").upper() or data[index]["paket_jasa"]
            # or digunakan jika admin mengosongkan input (langsung tekan enter)
            # upper() agar huruf tidak pandang kapital atau huruf kecil "A" , "a" tetap bisa

            simpan_data(data)
            print("Data pelanggan berhasil diperbarui!")
        else:
            print("Nomor data pelanggan tidak ditemukan!")
    except ValueError:
        print("Input tidak Valid!")

def hapus_data():
    data = baca_data()
    if not data:
        print("Belum ada data untuk dihapus!")
        return

    tampilkan_data()

    try:
        index = int(input("Masukkan nomor data pelanggan yang ingin dihapus: ")) - 1

        if 0 <= index < len(data):
            pelanggan_dihapus = data.pop(index)
            simpan_data(data)
            print("Data berhasil diihapus!")
        else:
            print("Nomor data pelanggan tidak ditemukan!")
    except ValueError:
        print("Input tidak Valid!")

def login():
    print("==============================")
    print("|       SISTEM LOGIN         |")
    print("==============================")

    data = baca_akun()

    if not data:
        print("Belum ada akun di database.")
        return

    username = input("Masukkan Username: ")
    password = pwinput.pwinput("Masukkan Password: ", mask = "*")

    login_berhasil = False
    for akun in data:
        if akun["username"] == username and akun ["password"] == password:
            login_berhasil = True
            print(f"Login Berhasil! Selamat Datang, {username}")


            if akun ["role"] == "admin":
                print("Masuk ke Menu Admin")
                menu_admin()
            else:
                print("Masuk ke Menu Pelanggan")
                menu_pelanggan()
            break

    if not login_berhasil:
        print("Username atau Password salah!")

def menu_admin():
    while True:
        print("============================================")
        print("|          MENU MANAJEMEN PETHOUSE         |")
        print("============================================")
        print("| 1. Tambah Data Pelanggan                 |")
        print("| 2. Tampilkan Data Pelanggan              |")
        print("| 3. Lihat Antrian                         |")
        print("| 4. Ubah Data Pelanggan                   |")
        print("| 5. Hapus Data Pelanggan                  |")
        print("| 6. Lihat Laporan Keuangan                |") #Belum ada
        print("| 0. Log Out                               |")
        print("============================================")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            lihat_antrian()
        elif pilihan == "4":
            ubah_data()
        elif pilihan == "5":
            hapus_data()
        elif pilihan == "6":
            print("otw bosqu") #otw
        elif pilihan == "0":
            print("Log Out Berhasil.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih angka(1-5)!")

def menu_pelanggan():
    while True:
        print("============================================")
        print("|          MENU CUSTOMER PETHOUSE          |")
        print("============================================")
        print("| 1. Lihat Paket                           |")
        print("| 2. Lihat Antrian                         |")
        print("| 3. Pembayaran                            |")
        print("| 4. Top Up                                |")
        print("| 0. Log Out                               |")
        print("============================================")
        pilihan = input("Masukkan pilihan (0-4): ")

        if pilihan == "1":
            print("belum woila")
        elif pilihan == "2":
            lihat_antrian()
        elif pilihan == "3":
            print("otw")
        elif pilihan == "4":
            print("otw bosq")
        elif pilihan == "0":
            print("Log Out Berhasil.")
            break
        else:
            print("Pilihan tidak valid!")

def main():
    if not os.path.exists("data_akun.json"):
        akun_admin = [
            {"username": "admin", "password" : "123", "role" : "admin"}
        ]
        simpan_akun(akun_admin)

    while True:
        print("===================================")
        print("|     MENU LOGIN & REGISTRASI     |")
        print("===================================")
        print("| 1. Login                        |")
        print("| 2. Registrasi                   |")
        print("| 3. Keluar Program               |")
        print("===================================")

        pilihan = input('Pilih Menu (1-3): ')

        if pilihan == "1":
            login()
        elif pilihan == "2":
            registrasi()
        elif pilihan == "3":
            print("Terima Kasih")
            break
        else:
            print("Pilihan tidak valid!")
main()