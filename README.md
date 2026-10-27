# Sistem Manajemen Perawatan Hewan Peliharaan
**Program Studi :** Sistem Informasi <br>
**Kelas :** A 2026 <br>
**Mata Kuliah :** Pratikum Dasar-Dasar Pemograman <br>
**Nama Kelompok:** ASIX GACOR <br>
**Anggota Kelompok:**
1. Brian Hotlan Sitompul (2609116035)
2. Sarah Afifah Ramadhani	(2609116024)
3. Nova Cynthia	(2609116031)
4. Chirenia Orphayana Altris Ganggung	(2609116038)

## Deskripsi

Program ini digunakan untuk mengelola data perawatan hewan peliharaan dimana terdapat 2 role, yaitu Admin dan user. Kedua role harus login terlebih dahulu dengan menggunakan username dan password untuk masuk ke dalam program, setiap user wajib registrasi akun sebelum login. Role 'Admin' memiliki hak akses untuk menambah data pelanggan, menampilkan data pelanggan, melihat antrian, mengubah data pelanggan, menghapus data pelanggan dan melihat laporan keuangan. Sedangkan role 'User' hanya dapat melihat paket jasa, melihat antrian, melakukan pembayaraan dan top up. Berikut tipe - tipe kode yang kami gunakan pada program :

1. json (JavaScript Object Notation) berfungsi untuk membaca dan menyimpan data dalam format JSON, kami gunakan untuk menyimpan data akun setiap pengguna selesai melakukan penginputan username dan password saat registrasi, data pelanggan setiap admin selesai penginputan dan data peket jasa.
   
2. pwinput berfungsi untuk menyembunyikan password dengan cara menampilkan "**" saat penginputan. Jenis library ini kami gunakan ketika role 'Admin' dan 'User' ingin login dan memasukan password.

3. prettyTable berfungsi untuk merapikan dan menampilkan data dalam bentuk tabel, Jenis library ini kami gunakan untuk menampilkan data pelanggan dan antrian.

4. os berfungsi untuk mengatur dan berinteraksi dengan sistem operasi komputer, lebih spesifik kami menggunakan os.path.exists() jenis library ini kami gunakan untuk mengecek apakah akun dan data pelanggan sudah ada di data_akun.json dan data_pelanggan.json atau belum.

5. time berfungsi untuk mengatur waktu yang digunakan pada fitur cooldown atau jeda waktu hitung mundur (time.sleep) saat salah login sebanyak 3x kali.

6. function berfungsi untuk blok kode dalam fungsi untuk menjalankan tugas jika di panggil. Tipe data ini kami gunakan untuk beberapa tugas seperti simpan_akun(), tampilkan_data(), dll

7. Percabangan (if, elif, else) berfungsi dalam pengamnilan keputusan atau alur logika berdasarkan kondisi tertentu. Tipe kode ini kami gunakan untuk beberapa tugas seperti penentuan hak akses role (if akun["role"] == "admin":), penentuan menu (if pilihan == "1": ), dll

8. while True berfungsi untuk melakukan perulangan atau looping pada intruksi yang diberikan yang tidak akan berhenti, kecuali terdapat transfer statement (continue dan break). Jenis looping ini digunakan untuk membuat menu utama, menu admin, menu user serta validasi input memastikan umur hewan dan nomor telepon pelanggan harus berupa angka.

9. for berfungsi untuk melakukan pperulangan atau looping pada elemen list atau dictionary. Digunakan untuk mencari data akun yang cocok saat login, memproses isi database pelanggan, hingga membuat hitung mundur saat sistem terkunci.

10. list ( [] ) berfungsi untuk menyimpan banyak data dalam satu variabel secara berurutan yang dapat diubah. Tipe kode ini kami gunakan untuk menampung banyak data akun atau daftar pelanggan ( data.append() )

11. Dictionary ( {} ) digunakan untuk menyimpan data berpasangan (key-value) seperti data detail akun ( "username" , "password" , "role" ) dan detail pelanggan ( "telepon" , "nama_hewan" <dll)

12. 

## Flowchart
### Menu Utama

Pada bagian menu utama terdapat pilihan login bagi Pengguna yang sudah memiliki akun, registrasi bagi Pengguna yang belum memiliki akun, dan exit. Pada bagian login, apa bila Pengguna melakukan lebih dari 3 kali percobaan gagal maka akan diberi jeda waktu 60 detik. Sedangkan pada bagian registrasi, apabila username sudah pernah digunakan, maka Pengguna akan diminta memasukkan ulang namanya. <br>

<br>
<img width="1773" alt="PA ASIXX-Page-1revisi drawio" src="https://github.com/user-attachments/assets/989a2988-faa4-4019-9807-cc2a7ea132ca" />

### Menu SuperAdmin

Pada role SuperAdmin terdapat pilihan:

#### 0. Logout
Jika ``SuperAdmin`` memilih opsi ini maka sistem akan mengeluarkan user sebagai ``SuperAdmin`` dan tampilan akan kembali ke ``menu utama``

#### 1. Tambah Data Pelanggan
``SuperAdmin`` menginput kebutuhan data pelanggan seperti nomor telepon pelanggan, nama pemilik hewan peliharaan, nama hewan peliharaan, jenis hewan peliharaan dan umur hewan peliharaan dan tambah jenis paket. Setelah itu sistem akan secara otomatis menampilkan output data pelanggan baru. Untuk input nomor telepon dan umur hanya bisa diinput dengan angka.

#### 2. Lihat Data Pelanggan
``SuperAdmin`` dapat melihat data pelanggan secara spesifik dengan pilihan menu ini.

#### 3. Lihat Antrian
``SuperAdmin`` dapat melihat secara garis besar berapa antrian pelanggan ``PetHouse``.

#### 4. Perbarui Data Pelanggan
``SuperAdmin`` dapat memperbarui data dari pelanggan apabila pelanggan tersebut ingin mengganti paket yang tersedia dengan menginput nomor antrian terlebih dahulu. Jika ``SuperAdmin`` menginput dengan teks dan bukan angka, maka sistem akan otomatis menampilkan ``"input tidak valid"`` atau jika nomor antrian/data tidak tercatat sebagai pelanggan, maka sistem akan secara otomatis menampilkan ``"tambahkan pelanggan terlebih dahulu"``.

#### 5. Hapus Data Pelanggan
``SuperAdmin`` dapat menghapus data pelanggan dengan menginput nomor antrian dan jika ``SuperAdmin`` menginput selain angka maka sistem akan menampilkan ``"input tidak valid"``.

#### 6. Lihat Laporan Keuangan
``SuperAdmin`` dapat melihat laporan keuangan yang menampilkan total dari pendapatan dan total dari pelanggan yang sudah melakukan transaksi.

<br>
<img width="1602" alt="PA ASIXX-Page-2revisi drawio" src="https://github.com/user-attachments/assets/43d8a22f-66e6-4403-9b9c-c037825c19cf" />

### Menu User

Pada role ``User`` yang merupakan role khusus pelanggan PetHouse, terdapat opsi:

#### 0. Logout
Jika ``User`` memilih opsi ini maka sistem akan mengeluarkan pelanggan sebagai ``User`` lalu akan kembali ke ``Menu Utama``.

#### 1. Lihat Paket
``User`` dapat melihat 3 jenis paket dengan opsi ini.

#### 2. Lihat Antrian
``User`` dapat melihat berapa total dari antrian pelanggan

#### 3. Pembayaran
``User`` dapat melakukan pembayaran dengan opsi ini dengan menginput nomor antrian dan input pin yang dibuat di ``Menu Utama`` lalu sistem akan menampilkan ``"pembayaran Berhasil"``.

#### 4. TopUp
``User`` dapat melakukan topup ke akun yang dibuat di PetHouse dari mata uang ``Rupiah`` lalu dikonversi ke mata uang ``Paw`` yang merupakan mata uang pada PetHouse sendiri. Topup dilakukan dengan menginput pin  terlebih dahulu dan kemudian memilih opsi topup.

<br>
<img width="1891" alt="PA ASIXX-Page-3revisi drawio" src="https://github.com/user-attachments/assets/447d8d69-8235-4164-81eb-aab5f3876c07" />

