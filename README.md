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

