import pwinput
from prettytable import PrettyTable
import json
import os
import time

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    
def cari_akun(username):
    akun_list = baca_akun()

    for akun in akun_list:
        if akun.get("username") == username:
            return akun_list, akun

    return akun_list, None

def baca_data():
    try:
        with open("data_pelanggan.json", "r") as file_json:
            return json.load(file_json)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]
    
def simpan_data(data):
    file_json = open("data_pelanggan.json", "w")
    json.dump(data, file_json, indent=4)
    file_json.close()
    print("Data Berhasil Ditambahkan!")
    

def tambah_data():
        while True:
            data = baca_data()
            nama_pemilik = input("Masukkan nama pemilik hewan: ").strip()
            if nama_pemilik == "":
                print("Nama pemilik tidak boleh kosong!")
                continue
            break
    
        while True:
            try:
                telepon = input("Masukkan Nomor Telepon Pelanggan (12 Digit): ")
                if telepon.isdigit() and len(telepon) == 12:
                    telepon = int(telepon)
                    break
                else:
                    print("Nomor telepon harus 12 digit!")
            except ValueError:
                print("Nomor telepon harus berupa angka!")

        while True:
            nama_hewan = input("Masukkan Nama Hewan: ").strip()
            if nama_hewan == "":
                print("Nama hewan tidak boleh kosong")
                continue
            break

        jenis_hewan_valid = ("anjing", "kucing", "hamster", "kelinci")
        while True:
            jenis_hewan = input("Masukkan Jenis Hewan (Anjing, Kucing, Hamster, dan Kelinci): ").strip().lower()
            if jenis_hewan == "":
                print("Nama hewan tidak boleh kosong")
                continue
            elif jenis_hewan not in jenis_hewan_valid:
                print("Jenis hewan hanya bisa sesuai pilihan")
                continue
            else:
                jenis_hewan = jenis_hewan.capitalize()
                break
                

        while True:
                input_umur = input("Masukkan umur hewan: ").strip()

                if not input_umur.isdigit():
                    print("Hanya boleh memasukan angka!")
                    continue

                elif len(input_umur) > 3:
                    print("Umur hewan tidak boleh lebih dari 3 digit!")
                    continue

                else:
                    umur_hewan = int(input_umur)
                    break

        jenis_paket_valid = ("a", "b", "c")
        while True:
            paket_jasa = input("Masukkan paket jasa (A, B, C): ").strip().lower()
            if paket_jasa == "":
                print("Paket jasa tidak boleh kosong")
                continue
            elif paket_jasa not in jenis_paket_valid:
                print("Paket jasa tidak valid!")
                continue
            else:
                paket_jasa = paket_jasa.upper()
                break

        pelanggan_baru = {
            "nama_pemilik" : nama_pemilik,
            "telepon" : telepon,
            "nama_hewan": nama_hewan,
            "jenis_hewan": jenis_hewan,
            "umur_hewan": umur_hewan,
            "paket_jasa": paket_jasa
        }
        
        data.append(pelanggan_baru)
        simpan_data(data)
        time.sleep(1.5)
        

def tampilkan_data():
    
    data = baca_data()

    if not data:
        print("Belum ada data pelanggan!")

    tabel = PrettyTable()
    tabel.field_names = ["No","Nama Pemilik", "No. Telepon","Nama Hewan", "Jenis Hewan", "Umur Hewan", "Paket Jasa", "Status Hewan" ]

    for index, p in enumerate (data, start=1):
        tabel.add_row([
            index,
            p.get("nama_pemilik"),
            p.get("telepon"),
            p.get("nama_hewan"),
            p.get("jenis_hewan"),
            p.get("umur_hewan"),
            p.get("paket_jasa"),
            p.get("status_grooming", "Belum")
        ])

    print(str(tabel))
    input("klik enter")
    return


def ubah_data(): 
    bersihkan_layar()

    JENIS_HEWAN = ["Anjing", "Kucing", "Kelinci", "Hamster"]
    PAKET_JASA = ["A", "B", "C"]
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
            
            data[index]["nama_pemilik"] = input("Masukkan Nama Pemilik: ") or data[index]["nama_pemilik"]
            data[index]["telepon"] = input("Masukkan No. Telepon baru (Kosongkan jika tetap): ") or data[index]["telepon"]
            data[index]["nama_hewan"] = input("Masukkan Nama Hewan Baru (Kosongkan jika tetap): ") or data[index]["nama_hewan"]

            while True:
                print(f"\nJenis Hewan (sekarang: {data[index]['jenis_hewan']})")
                for no, jenis in enumerate(JENIS_HEWAN, start=1):
                    print(f"{no}. {jenis}")
                pilihan = input(f"Pilih (1-{len(JENIS_HEWAN)}) (Kosongkan jika tetap): ").strip()

                if not pilihan:
                    break
                if pilihan.isdigit() and 1 <= int(pilihan) <= len(JENIS_HEWAN):
                    data[index]["jenis_hewan"] = JENIS_HEWAN[int(pilihan) - 1]
                    break
                print("Pilihan tidak valid!")

            data[index]["umur_hewan"] = input("Masukkan Umur Hewan Baru (Kosongkan jika tetap): ") or data[index]["umur_hewan"]

            while True:
                print(f"\nPaket Jasa (sekarang: {data[index]['paket_jasa']})")
                for no, paket in enumerate(PAKET_JASA, start=1):
                    print(f"{no}. Paket {paket}")
                pilihan = input(f"Pilih (1-{len(PAKET_JASA)}) (Kosongkan jika tetap): ").strip()

                if not pilihan:
                    break
                if pilihan.isdigit() and 1 <= int(pilihan) <= len(PAKET_JASA):
                    data[index]["paket_jasa"] = PAKET_JASA[int(pilihan) - 1]
                    break
                print("Pilihan tidak valid!")
            data[index]["status_grooming"] = input("Masukkan Status Hewan (1: Sudah / 2: Belum): ").upper() or data[index]["status_grooming"]
            # or digunakan jika admin mengosongkan input (langsung tekan enter)
            # upper() apapun huruf yang diinput outputnya akan kapital

            simpan_data(data)
            print("Data pelanggan berhasil diperbarui!")
        else:
            print("Nomor data pelanggan tidak ditemukan!")
    except ValueError:
        print("Input tidak Valid!")

def hapus_data():
    bersihkan_layar()
    data = baca_data()
    if not data:
        print("Belum ada data untuk dihapus!")
        input("Tekan Enter untuk kembali")
        return

    tampilkan_data()
    try:
        index = int(input("Masukkan nomor data pelanggan yang ingin dihapus: ")) - 1
    except ValueError:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali")
        return

    if not (0 <= index < len(data)):
        print("Nomor data pelanggan tidak ditemukan!")
        input("\nTekan Enter untuk kembali")
        return

    nama_hewan = data[index].get("nama_hewan")
    nama_pemilik = data[index].get("nama_pemilik")

    while True:
        konfirmasi = input(f"Apakah anda yakin menghapus data hewan {nama_hewan} milik {nama_pemilik}? (y/n): ").strip().lower()
        if konfirmasi not in ("y", "n"):
            print("Input tidak valid! Masukkan y atau n.")
            continue
        break

    if konfirmasi == "y":
        data.pop(index)
        simpan_data(data)
        print("Data berhasil dihapus!")
    else:
        print("Penghapusan data dibatalkan.")

    input("\nTekan Enter untuk kembali")

def lihat_antrian():
    bersihkan_layar()
    try:
        data = baca_data()
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    antrian = [
        p for p in data 
        if str (p.get("status_grooming", "Belum")) == "Belum"
    ]

    print("======================================")
    print(f"|       TOTAL ANTRIAN : {len(antrian)}|")
    print("======================================")

    if not antrian:
        print("Tidak ada antrian saat ini.")
        input("\nTekan Enter untuk kembali")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama Pemilik", "Nama Hewan", "Paket"]
    for no, p in enumerate(antrian, start=1):
        table.add_row([
            no,
            p.get("nama_pemilik", p.get("username", "-")),
            p.get("nama_hewan", "-"),
            p.get("paket_jasa", "-")
        ])

    print(table)
    input("\nTekan Enter untuk kembali")


def registrasi():
    bersihkan_layar()
    print("==============================")
    print("|    MENU REGISTRASI AKUN    |")
    print("==============================")

    data = baca_akun()

    username = input("Masukkan Username: ")
    
    for akun in data:
        if akun["username"] == username:
            print("Username sudah terdaftar! Silahkan gunakan username lain.")
            continue

    while True:
        password = pwinput.pwinput("Masukkan Password (Min 4 Digit): ", mask = "*")
        pin = pwinput.pwinput("Masukkan pin untuk top up: ").strip()

        if not password:
            print("Password tidak boleh kosong")
        elif not (len(password) >= 4): #perintah yang dimana password harus memiliki minimal jumlah 4 digit
            print("Password minimal harus memiliki panjang 4 digit")
        elif not pin:
            print("Pin tidak boleh kosong")
        elif any(akun.get("pin") == pin for akun in data):
                print("Pin sudah terdaftar! Silahkan gunakan pin lain.")
                continue
        if not pin.isdigit():
                print("Hanya boleh memasukan angka!")
                continue
        else:
            break
    akun_baru = {
        "username" : username,
        "password" : password,
        "role" : "pelanggan",
        "pin" : pin,
        "saldo_paw" : 0
    }

    data.append(akun_baru)
    simpan_akun(data)
    print("Registrasi akun berhasil! Silahkan Login.")
    time.sleep(2)

def login():
    bersihkan_layar()
    print("==============================")
    print("|       SISTEM LOGIN         |")
    print("==============================")

    data = baca_akun()

    if not data:
        print("Belum ada akun di database.")
        return
    
    coba = 0
    maks_coba = 3

    while True:
        username = input("Masukkan Username: ")
        password = pwinput.pwinput("Masukkan Password: ", mask = "*")

        login_berhasil = False
        for akun in data:
            if akun["username"] == username and akun ["password"] == password:
                login_berhasil = True
                print(f"Login Berhasil! Selamat Datang, {username}")
                time.sleep(2)


                if akun ["role"] == "admin":
                    print("Masuk ke Menu Admin")
                    menu_admin()
                else:
                    print("Masuk ke Menu Pelanggan")
                    menu_pelanggan(username)
                return

        if not login_berhasil:
            coba += 1   
            kesempatan = 3 - coba   
            print("Username atau Password salah!")

            if kesempatan > 0:
                print(f"Sisa kesempatan login anda {kesempatan} kali lagi.")
            else:
                print("Anda telah 3x salah memasukkan data.")
                print("Sistem terkunci. Mohon coba lagi setelah 60 detik")

                for detik in range(60, 0, -1): #60 adalah detik awal, 0 adalah tujuan akhir dan -1 adalah step penurunan
                    print(f"Silahkan tunggu {detik} detik tersisa")
                    time.sleep(1)
                print("Waktu cooldown selesai. Silahkan masukkan ulang username dan password anda.")

                coba = 0


#FITUR TOP UP dan PEMBAYARAN
def top_up(username):
    bersihkan_layar()
    akun_list, akun = cari_akun(username)

    akun = None
    for a in akun_list:
        if a["username"] == username:
            akun = a
            break

    if akun is None:
        print("Akun tidak ditemukan")
        input("\nTekan enter untuk kembali ke menu pelanggan")
        return
    
    print("=====================")
    print("| TOP UP SALDO PAW  |")
    print("=====================")
    print("Rp. 10.000 = 10 Paw")
    print("Minimal Top Up = Rp. 10.000 (10 Paw)")

    while True:
            nominal = input("Masukkan nominal rupiah yang ingin di Top - Up: ")
            if not nominal.isdigit():
                print("Input harus berupa angka positif tidak minus (-)!")
                continue
            rupiah = int(nominal)
            if rupiah < 10000:
                print("Minimal top up adalah Rp.10.000!")
                continue
            break
    
    #verifikasi PIN
    pin_tersimpan = akun.get("pin")
    if not pin_tersimpan:
        print("Akun kamu belum mempunyai PIN.")
        time.sleep(2)
        return
                
    percobaan = 3
    while percobaan > 0:
        pin_input = pwinput.pwinput("Masukkan PIN Anda: ").strip()
        if pin_input == pin_tersimpan:
            break
        percobaan -= 1
        print(f"PIN salah! Sisa percobaan: {percobaan}")
    else:
        print("PIN salah 3 kali. Transaksi dibatalkan.")
        time.sleep(2)
        return
        
    paw = rupiah // 1000
    akun["saldo_paw"] = akun.get("saldo_paw", 0) + paw
    simpan_akun(akun_list)
    print(f"Top up berhasil!")
    print(f"Menambah {paw} Paw. Total saldo Paw Anda: {akun['saldo_paw']} Paw")
    input("\nTekan enter untuk kembali ke menu pelanggan")

def baca_transaksi():
    if not os.path.exists("laporan_keuangan.json"):
        return[]
    try:
        file_json = open("laporan_keuangan.json", "r")
        data = json.load(file_json)
        file_json.close()
        return data
    except json.JSONDecodeError:
        return[]

def simpan_transaksi(data):
    file_json = open("laporan_keuangan.json", "w")
    json.dump(data, file_json, indent=4)
    file_json.close() 

def pembayaran(username):
    harga_paket = {"A":30, "B":20, "C":10}

    akun_list = baca_akun()
    user_akun = None

    for akun in akun_list:
        if akun["username"] == username:
            user_akun = akun
            break

    if user_akun is None:
        time.sleep(2)
        return

    if "saldo_paw" not in user_akun:
        user_akun["saldo_paw"] = 0
    
    #validasi status pembayaran
    data = baca_data()
    daftar = [
        (i, p) for i, p in enumerate(data)
        if p.get("username_akun") == username
        and p.get("status_pembayaran", "belum") != "Lunas"
    ]

    if not daftar:
        print("Tidak ada tagihan yang harus dibayar.")
        input("\nTekan Enter untuk kembali ke Menu Utama")
        return

    
    print("==========================")
    print("|   PEMBAYARAN LAYANAN   |")
    print("==========================")
    print(f"Saldo Paw anda saat ini: {user_akun['saldo_paw']} Paw")

    print("================== PESANAN ANDA ====================")
    for no, (i, p) in enumerate(daftar, start=1):
        biaya_paket = harga_paket.get(p.get("paket_jasa"), 0)
        print(f"{no}. {p.get('nama_hewan')} | Paket {p.get('paket_jasa')} | {biaya_paket} Paw")

    # pilih pesanan yang dibayar
    try:
        pilih = int(input("\nPilih nomor pesanan yang ingin dibayar: ")) - 1
    except ValueError:
        print("Input harus berupa angka!")
        time.sleep(2)
        return

    if not (0 <= pilih < len(daftar)):
        print("Nomor pesanan tidak valid!")
        time.sleep(2)
        return

    index_data, pesanan = daftar[pilih]
    pilihan_paket = pesanan.get("paket_jasa")

    # biaya otomatis sesuai paket yang dipesan
    if pilihan_paket not in harga_paket:
        print("Harga untuk paket ini tidak ditemukan!")
        time.sleep(2)
        return

    biaya = harga_paket[pilihan_paket]

    print(f"\nHewan : {pesanan.get('nama_hewan')}")
    print(f"Paket : {pilihan_paket}")
    print(f"Biaya : {harga_paket} Paw")
    
    #validasi saldo minus
    if user_akun["saldo_paw"] < biaya:
        print("Saldo anda tidak mencukupi!. Silahkan top up!")
        time.sleep(1)
        return

    #verifikasi pin
    pin_tersimpan = user_akun.get("pin")
    if not pin_tersimpan:
        print("Akun kamu belum mempunyai PIN.")
        return
    
    percobaan = 3
    while percobaan > 0:
        pin_input = pwinput.pwinput("Masukkan PIN Anda: ").strip()
        if pin_input == pin_tersimpan:
            break
        percobaan -= 1
        print(f"PIN salah! Sisa percobaan: {percobaan}")
    else:
        print("PIN salah 3 kali. Transaksi dibatalkan.")
        return
    
    #kurangi saldo
    user_akun["saldo_paw"] -= biaya
    simpan_akun(akun_list)
    data[index_data]["status_pembayaran"] = "Lunas"
    simpan_data(data)
    print("Pembayaran berhasil!")
    time.sleep(1)

    #simpan transaksi
    transaksi = baca_transaksi()
    invoice_id = f"INV-{int(time.time())}"
    data_transaksi = {
        "invoice" : invoice_id,
        "username" : username,
        "paket" : pilihan_paket,
        "biaya" : biaya,
        "waktu" : time.strftime("%Y-%m-%d %H:%M:%S")
    }
    transaksi.append(data_transaksi)
    simpan_transaksi(transaksi)

    #Cetak INVOICE
    print("=================================")
    print("|      INVOICE PEMBAYARAN       |")
    print("=================================")
    print(f" No. Invoice  : {invoice_id}")
    print(f" Waktu        : {data_transaksi['waktu']}")
    print(f" Username     : {username}")
    print(f" Paket Jasa   : Paket {pilihan_paket}")
    print(f" Biaya        : {biaya} Paw")
    print(f" Sisa Saldo   : {user_akun['saldo_paw']} Paw")
    print(" Status       : SUCCESS!")
    print("|===============================|")

    input("\nTekan Enter untuk kembali ke Menu Utama")

def riwayat_transaksi(username, role):

    transaksi = baca_transaksi()
    if not transaksi:
        print("Belum ada data Transaksi")
        return

    print("================================")
    print("|      RIWAYAT TRANSAKSI       |")
    print("================================")

    ditemukan = False
    for t in transaksi:
        if role == "pelanggan" and t["username"] != username:
            continue

        ditemukan = True
        print("=================================")
        print(f" No. Invoice : {t['invoice']}")
        print(f" Waktu       : {t['waktu']}")
        print(f" Username    : {t['username']}")
        print(f" Paket Jasa  : Paket {t['paket']}")
        print(f" Biaya       : {t['biaya']} Paw")
        print("=================================")

        if role == "pelanggan" and not ditemukan:
            print("Anda belum memiliki Riwayat Transaksi.")
            time.sleep(2)
            return
        input("\n Tekan enter untuk kembali ke Menu Pelanggan")

def laporan_ringkas_admin():
    
    transaksi = baca_transaksi()
    if not transaksi:
        print("Belum ada data Transaksi untuk laporan.")
        return

    total_pendapatan = 0
    jumlah_transaksi = len(transaksi)
    penghitung_paket = {"A" : 0, "B" : 0, "C" : 0}

    for t in transaksi:
        total_pendapatan += t.get("biaya", 0)
        paket = t.get("paket")
        if paket in penghitung_paket:
            penghitung_paket[paket] += 1

    # Paket terlaris
    max_terjual = max(penghitung_paket.values())
    if max_terjual == 0:
        paket_terlaris = "Belum ada penjualan"
    else:
        terlaris = [k for k, v in penghitung_paket.items() if v == max_terjual]
        paket_terlaris = ",".join([f"Paket{p}" for p in terlaris])

    print("============================================")
    print("|          LAPORAN RINGKAS ADMIN           |")
    print("============================================")
    print(f" Total Transaksi  : {jumlah_transaksi}")
    print(f" Total Pendapatan : {total_pendapatan} Paw")
    print(f" Paket Terlaris   : {paket_terlaris}")
    print("============================================")

                
def menu_admin():
    while True:
        
        print("============================================")
        print("|          MENU MANAJEMEN PETHOUSE         |")
        print("============================================")
        print("| 1. Tambah Data Pelanggan                 |")
        print("| 2. Tampilkan Data Pelanggan dan Hewan    |")
        print("| 3. Lihat Antrian                         |")
        print("| 4. Perbarui Data Pelanggan               |")
        print("| 5. Hapus Data Pelanggan                  |")
        print("| 6. Lihat Laporan Keuangan                |") 
        print("| 0. Log Out                               |")
        print("============================================")

        pilihan = input("Masukkan pilihan (0-6): ")

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
            laporan_ringkas_admin()
        elif pilihan == "0":
            print("Log Out Berhasil!")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih angka(1-6)!")
            time.sleep(1)

def menu_pelanggan(username):
    while True:
        bersihkan_layar()
        print("============================================")
        print("|          MENU CUSTOMER PETHOUSE          |")
        print("============================================")   
        print("| 1. Pendaftaran Online                    |")
        print("| 2. Lihat Paket                           |")
        print("| 3. Lihat Antrian                         |")
        print("| 4. Pembayaran                            |")
        print("| 5. Top Up Saldo Paw                      |")
        print("| 6. Riwayat Pembayaran                    |")
        print("| 7. Status Hewan                          |")
        print("| 0. Log Out                               |")
        print("============================================")
        pilihan = input("Masukkan pilihan (0-7): ")

        if pilihan == "1":
            isi_data_sendiri(username)
        if pilihan == "2":
            bersihkan_layar()
            print("============================================================")
            print("|                       DAFTAR PAKET                       |")
            print("============================================================")
            print("| - Paket A : 30 Paw (Grooming + rapihin bulu + vitamin)   |")
            print("| - Paket B : 20 Paw (Grooming + vitamin)                  |")
            print("| - Paket C : 10 Paw (Grooming)                            |")
            print("============================================================")
            input("\nTekan Enter untuk kembali")
        elif pilihan == "3":
            lihat_antrian()
        elif pilihan == "4":
            pembayaran(username)
        elif pilihan == "5":
            top_up(username)
        elif pilihan == "6":
            riwayat_transaksi(username, role="pelanggan")
        elif pilihan == "7":
            lihat_status_hewan(username)
        elif pilihan == "0":
            print("Log Out Berhasil.")
            break
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)

def status_hewan():
    bersihkan_layar()
    data = baca_data()

    if not data:
        print("belum ada data pelanggan! ")
        input("\nTekan enter untuk kembali")
        return

    tampilkan_data()

    try:
        index = int(input("Masukkan nomor hewan yang ingin diubah statusnya: ")) - 1

        if not (0 <= index < len(data)):
            print("Nomor data pelanggan tidak ditemukan!")
            input("\nTekan enter untuk kembali")
            return

        nama_hewan = data[index].get("nama_hewan")
        status_sekarang = data[index].get("status_hewan", "Belum")

        print(f"\n Hewan: {nama_hewan}")
        
        print("1. Sudah selesai grooming")
        print("2. Belum selesai grooming")

        pilihan = input("Pilih status(1-2): ").strip()

        if pilihan == "1":
            data[index]["status_grooming"] = "Sudah"
        elif pilihan == "2":
            data[index]["status_grooming"] = "Belum"

        else:
            print("pilihan tidak valid!")
            input("\nTekan enter untuk kembali")
            return

        simpan_data(data)
        print("Status hewan berhasil diperbarui!")
        input("\nTekan enter untuk kembali")

    except ValueError:
        print("Input tidak valid")
        input("tekan enter untuk kembali")

def lihat_status_hewan(username):
    bersihkan_layar()
    data = baca_data()

    hewan_user = []

    for p in data:
        if p.get("username_akun") == username:
            hewan_user.append(p)

    if not hewan_user:
        print("Anda belum memiliki data hewan yang terdaftar!")
        input("\nTekan enter untuk kembali")
        return

    print("=====================================")
    print("|        STATUS HEWAN ANDA          |")
    print("=====================================")

    for hewan in hewan_user:

        print("-------------------------------------")
        print(f"Nama Hewan       : {hewan.get('nama_hewan')}")
        print(f"Jenis Hewan      : {hewan.get('jenis_hewan')}")
        print(f"Paket Jasa       : {hewan.get('paket_jasa')}")
        print(f"Status Grooming  : {hewan.get('status_grooming', 'Belum')}")
    print("=====================================")

    input("\nTekan Enter untuk kembali")


def isi_data_sendiri(username):
    bersihkan_layar()
    data = baca_data()

    print("=====================================")
    print("|      ISI DATA HEWAN ANDA          |")
    print("=====================================")

    # nama pemilik
    while True:
        nama_pemilik = input("Nama Pemilik: ").strip()
        if nama_pemilik:
            break
        print("Nama pemilik tidak boleh kosong!")

    # telepon
    while True:
        telepon = input("No. Telepon: ").strip()
        if not telepon.isdigit():
            print("Nomor telepon hanya boleh berisi angka!")
        elif not (10 <= len(telepon) <= 12):
            print("Nomor telepon harus 10-12 digit!")
        else:
            break

    # nama hewan
    while True:
        nama_hewan = input("Nama Hewan: ").strip()
        if nama_hewan:
            break
        print("Nama hewan tidak boleh kosong!")

    # jenis hewan (pilihan)

    while True:
        JENIS_HEWAN = ["Anjing", "Kucing", "Kelinci", "Hamster"]

        print("\nJenis Hewan:")
        for no, jenis in enumerate(JENIS_HEWAN, start=1):
            print(f"{no}. {jenis}")
        pilihan = input(f"Pilih (1-{len(JENIS_HEWAN)}): ").strip()
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(JENIS_HEWAN):
            jenis_hewan = JENIS_HEWAN[int(pilihan) - 1]
            break
        print("Pilihan tidak valid!")

    # umur
    while True:
            input_umur = input("umur hewan: ").strip()

            if not input_umur.isdigit():
                print("Hanya boleh memasukan angka!")
                continue

            elif len(input_umur) > 3:
                print("Umur hewan tidak boleh lebih dari 3 digit!")
                continue

            else:
                umur_hewan = int(input_umur)
                break

    # paket (pilihan)
    while True:
        PAKET_JASA = ["A", "B", "C"]
        harga_paket = {"A":30, "B":20, "C":10}
        print("\nPaket Jasa:")
        for no, paket in enumerate(PAKET_JASA, start=1):
            print(f"{no}. Paket {paket} ({harga_paket[paket]} Paw)")
        pilihan = input(f"Pilih (1-{len(PAKET_JASA)}): ").strip()
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(PAKET_JASA):
            paket_jasa = PAKET_JASA[int(pilihan) - 1]
            break
        print("Pilihan tidak valid!")

    data.append({
        "username_akun": username,
        "nama_pemilik": nama_pemilik,
        "telepon": telepon,
        "nama_hewan": nama_hewan,
        "jenis_hewan": jenis_hewan,
        "umur_hewan": umur_hewan,
        "paket_jasa": paket_jasa,
        "status_grooming": "Belum",
        "status_pembayaran": "Belum",
    })

    simpan_data(data)
    print("\nData hewan berhasil ditambahkan! Silahkan lanjut ke menu pembayaran.")
    input("\nTekan enter untuk kembali")

def main():
    if not os.path.exists("data_akun.json"):
        akun_admin = [
            {"username": "admin", "password" : "123", "role" : "admin"}
        ]
        simpan_akun(akun_admin)

    while True:
        bersihkan_layar()
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
            time.sleep(1)


while True:
    try:
        main()
        break
    except KeyboardInterrupt:
            print("\nWOI JANGAN!")
    except EOFError:
        print("\nWOI JANGAN!")
