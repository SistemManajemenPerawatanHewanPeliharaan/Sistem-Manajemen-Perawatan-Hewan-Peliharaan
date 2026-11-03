# Sistem Manajemen Perawatan Hewan Peliharaan
**Program Studi :** Sistem Informasi <br>
**Kelas :** A 2026 <br>
**Mata Kuliah :** Pratikum Dasar-Dasar Pemograman <br>
**Nama Kelompok:** A6 - ASIX GACOR <br>

# Anggota Kelompok

1. Brian Hotlan Sitompul (2609116035)
2. Sarah Afifah Ramadhani	(2609116024)
3. Nova Cynthia	(2609116031)
4. Chirenia Orphayana Altris Ganggung	(2609116038)

# Peran dan Tanggung Jawab

| Nama Anggota | NIM | Peran & Tanggung Jawab | GitHub |
| :---: | :--- | :---: | :--- |
| *Brian Hotlan Sitompul* | 2609116035 | Peran| @Nairbeeeeee (https://github.com/Nairbeeeeee) |
| *Sarah Afifah Ramadhani* | 2609116024 | Peran | @sarahafifahramadhani (https://github.com/sarahafifahramadhani) |
| *Chirenia Orphayana Altris Ganggung* | 2609116038 | Peran | @ChireniaOrphayanaAltrisGanggung (https://github.com/ChireniaOrphayanaAltrisGanggung) |
| *Nova Cynthia* | 2609116031 | Peran | @novacynthia11-commits (https://github.com/novacynthia11-commits) |

## Deskripsi

Program ini digunakan untuk mengelola data perawatan hewan peliharaan dimana terdapat 2 role, yaitu Admin dan user. Kedua role harus login terlebih dahulu dengan menggunakan username dan password untuk masuk ke dalam program, setiap user wajib registrasi akun sebelum login. Role 'Admin' memiliki hak akses untuk menambah data pelanggan, menampilkan data pelanggan, melihat antrian, mengubah data pelanggan, menghapus data pelanggan dan melihat laporan keuangan. Sedangkan role 'User' hanya dapat melihat paket jasa, melihat antrian, melakukan pembayaraan dan top up. Berikut tipe - tipe kode yang kami gunakan pada program :

1. ``json (JavaScript Object Notation)`` berfungsi untuk membaca dan menyimpan data dalam format JSON, kami gunakan untuk menyimpan data akun setiap pengguna selesai melakukan penginputan username dan password saat registrasi, data pelanggan setiap admin selesai penginputan dan data peket jasa.
   
2. ``pwinput`` berfungsi untuk menyembunyikan password dengan cara menampilkan "**" saat penginputan. Jenis library ini kami gunakan ketika role 'Admin' dan 'User' ingin login dan memasukan password.

3. ``prettyTable`` berfungsi untuk merapikan dan menampilkan data dalam bentuk tabel, Jenis library ini kami gunakan untuk menampilkan data pelanggan dan antrian.

4. ``os`` berfungsi untuk mengatur dan berinteraksi dengan sistem operasi komputer, lebih spesifik kami menggunakan os.path.exists() jenis library ini kami gunakan untuk mengecek apakah akun dan data pelanggan sudah ada di data_akun.json dan data_pelanggan.json atau belum.

5. ``time`` berfungsi untuk mengatur waktu yang digunakan pada fitur cooldown atau jeda waktu hitung mundur (time.sleep) saat salah login sebanyak 3x kali.

6. ``function`` berfungsi untuk blok kode dalam fungsi untuk menjalankan tugas jika di panggil. Tipe data ini kami gunakan untuk beberapa tugas seperti simpan_akun(), tampilkan_data(), dll

7. ``Percabangan (if, elif, else)`` berfungsi dalam pengamnilan keputusan atau alur logika berdasarkan kondisi tertentu. Tipe kode ini kami gunakan untuk beberapa tugas seperti penentuan hak akses role (if akun["role"] == "admin":), penentuan menu (if pilihan == "1": ), dll

8. ``while True`` berfungsi untuk melakukan perulangan atau looping pada intruksi yang diberikan yang tidak akan berhenti, kecuali terdapat transfer statement (continue dan break). Jenis looping ini digunakan untuk membuat menu utama, menu admin, menu user serta validasi input memastikan umur hewan dan nomor telepon pelanggan harus berupa angka.

9. ``for`` berfungsi untuk melakukan pperulangan atau looping pada elemen list atau dictionary. Digunakan untuk mencari data akun yang cocok saat login, memproses isi database pelanggan, hingga membuat hitung mundur saat sistem terkunci.

10. ``list ( [] )`` berfungsi untuk menyimpan banyak data dalam satu variabel secara berurutan yang dapat diubah. Tipe kode ini kami gunakan untuk menampung banyak data akun atau daftar pelanggan ( data.append() )

11. ``Dictionary ( {} )`` digunakan untuk menyimpan data berpasangan (key-value) seperti data detail akun ( "username" , "password" , "role" ) dan detail pelanggan ( "telepon" , "nama_hewan" <dll)

12. ``Error Handling`` berfungsi untuk mencegah program berhenti mendadak saat terjadi excpection. Kami menggunakan "try" dan "except", except json.JSONDecodeError: menangani error jika file JSON kosong atau rusak saat di baca, except ValueError menangani kesalahan input seperti meminta input angka int(input()) tetapi admin malah memasukan huruf.

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

#### 1. Membuat Pesanan
``User`` dapat menambah pesanan dengan menginput kebutuhan input data seperti nomor telepon pemilik hewan peliharaan, nama hewan, jenis hewan, umur hewan, dan memilih paket grooming. Setelah itu data yang telah diinput akan disimpan ke data pelanggan

#### 2. Lihat Paket
``User`` dapat melihat 3 jenis paket dengan opsi ini.

#### 3. Lihat Antrian
``User`` dapat melihat berapa total dari antrian pelanggan

#### 4. Pembayaran
``User`` dapat melakukan pembayaran dengan opsi ini dengan menginput nomor antrian dan input pin yang dibuat di ``Menu Utama`` lalu sistem akan menampilkan ``"pembayaran Berhasil"``.

#### 5. TopUp
``User`` dapat melakukan topup ke akun yang dibuat di PetHouse dari mata uang ``Rupiah`` lalu dikonversi ke mata uang ``Paw`` yang merupakan mata uang pada PetHouse sendiri. Topup dilakukan dengan menginput pin  terlebih dahulu dan kemudian memilih opsi topup.

<br>
<img width="1559" alt="PA ASIXX-Page-3-revisi sekian drawio" src="https://github.com/user-attachments/assets/a725dfc3-0c56-4077-9c9c-3badc5e23227" />

## Output

### Menu Utama
Menu utama memiliki 3 opsi, yang pertama adalah ``Login``, kedua adalah ``Registrasi`` dan yang ketiga adalah ``Keluar Program``. Pilihan pertama adalah jika user sudah membuat akun, pilihan kedua jika user belum memiliki akun, pilihan ketiga jika user ingin program berhenti berjalan. 

<br>
<img width="362" height="206" alt="image" src="https://github.com/user-attachments/assets/250510dc-294e-443a-8d77-8f81a01841e6" />




a. Apabila user menginput text ataupun input selain dari opsi yang diberikan, program akan menampilkan ``"Pilihan tidak Valid."`` dan akan kembali meminta user untuk menginput setelah 1 detik.

<br>
<img width="372" height="243" alt="image" src="https://github.com/user-attachments/assets/a3ed41ab-6898-4506-9f62-64cb4024095e" />

#### Menu Login
Program akan meminta meng-*input*kan Username dan Password yang sudah dibuat di menu registrasi sebelumnya. <br>
a. Login berhasil sebagai ``SuperAdmin``, khusus ``SuperAdmin`` Username dan Password sudah disediakan. <br>
<img width="433" height="180" alt="image" src="https://github.com/user-attachments/assets/f1d5cfcd-e7b7-4ff7-acfe-1f4a410da164" />



b. Login berhasil sebagai ``User``, untuk ``User`` **wajib** melakukan registrasi terlebih dahulu agar akunnya terdaftar. <br>
<img width="382" height="192" alt="image" src="https://github.com/user-attachments/assets/a62fb706-3ffd-41ad-a93d-0efa536bcfff" />


c. Apabila password salah, percobaan salah hanya 3 kali apabila lebih dari 3 kali maka akan diberi jeda 60 detik untuk men-_input___ username dan password kembali. <br>
<img width="418" height="258" alt="image" src="https://github.com/user-attachments/assets/cc96fc3d-7747-4a70-9384-f956c203ec92" />


### Menu Registrasi
Program akan meminta meng-*input*kan username, password, dan pin untuk top-up atau pembayaran nanti. <br>
a. Registrasi berhasil setelah meng-_input_ username dan password baru. <br>
<img width="436" height="210" alt="image" src="https://github.com/user-attachments/assets/276c74f2-a3f3-4c67-ae8e-b96ac561ef54" />


b. Apabila username sudah terpakai. <br>
<img width="565" height="182" alt="image" src="https://github.com/user-attachments/assets/d4a9f490-6bb5-41cc-9f46-8eef560d8c03" />


### SuperAdmin

**1. Tambah data pelanggan** 

Pada opsi ini dapat diisi dengan nama pemilik hewan, nomor telepon pemilik yang harus diisi dengan 12 digit angka, nama hewan, jenis hewan yang harus sesuai dengan daftar hewan pada sistem, umur hewan dengan limit 3 angka dan input paket. <br>
<img width="770" height="776" alt="image" src="https://github.com/user-attachments/assets/43ac9277-c1d3-41bb-abc5-8e620266242a" />



**2. Lihat data pelanggan** 

Opsi ini menampilkan data data yang telah diinput pelanggan dan status dari hewan tersebut, apakah statusnya sudah digrooming atau belum digrooming. <br>
<img width="968" height="300" alt="image" src="https://github.com/user-attachments/assets/cf989c44-c8f1-4192-9be7-088e2cdaa7b1" />


**3. Lihat antrian pelanggan** 

Opsi ini menampilkan total antrian pelanggan dan data nama pemilik, nama hewan dan paket yang dipilih. <br>
<img width="445" height="341" alt="image" src="https://github.com/user-attachments/assets/3935541b-59bc-46f7-ad09-530b4261ca2d" />


**4. Perbarui data pelanggan** 

Opsi ini ``SuperAdmin`` dapat mengubah data pelanggan apabila pelanggan ingin mengubah beberapa datanya. <br>
<img width="1181" height="872" alt="image" src="https://github.com/user-attachments/assets/fb0d6596-9487-42a5-9118-21e61507bd12" />


**5. Hapus data pelanggan** 

Opsi ini ``SuperAdmin`` dapat menghapus data pelanggan dengan menginput nomor antrian pelanggan. <br>
<img width="1000" height="331" alt="image" src="https://github.com/user-attachments/assets/26872079-ad4b-41c5-bab9-1bce118fef45" />


**6. Lihat laporan keuangan** 

Opsi ini menampilkan rekapitulasi harian mencakup total transaksi, total pendapatan dan paket terlaris. <br>
<img width="462" height="247" alt="image" src="https://github.com/user-attachments/assets/82e9a814-1532-49da-b785-391737305fc3" />


### User

**1. Pendaftaran online** 

Pada opsi ``User`` dapat mendaftarkan hewan peliharaannya secara online dengan meng-_input_ data data yang dibutuhkan. <br>
<img width="1030" height="545" alt="image" src="https://github.com/user-attachments/assets/cb13696f-120e-4c04-a16c-7d252b06ec0c" />

**2. Lihat paket** 

Opsi ini menampilkan daftar paket yang tersedia. <br>
<img width="727" height="232" alt="image" src="https://github.com/user-attachments/assets/dab0ad32-72c2-4485-ae4c-868f2ed2028c" />

**3. Lihat antrian** 

Opsi ini menampilkan daftar pelanggan secara singkat dan menampilkan jumlah total dari antrian. <br> 
<img width="411" height="330" alt="image" src="https://github.com/user-attachments/assets/7f4defe7-e86a-4a71-a0fb-ae8b445cd192" />

**4. Pembayaran layanan** 

Opsi ini menampilkan data pemesanan terlebih dahulu lalu ``User`` dapat memilih pemesanan mana yang akan dibayar dengan saldo yang dimiliki. Apabila saldo tidak mencukupi, maka ``User`` akan diminta untuk topup terlebih dahulu. <br>
<img width="486" height="413" alt="image" src="https://github.com/user-attachments/assets/f07dfc8c-7a6d-4588-9a93-007c5d304ea2" />

**5. Topup saldo paw** 

Opsi ini dipilih apabila ``User`` ingin mengisi saldo dengan mata uang ``Paw`` untuk bisa melakukan pembayaran pada ``PetHouse``. <br>
<img width="565" height="293" alt="image" src="https://github.com/user-attachments/assets/7a1865e5-0f1b-4e94-acba-2cd10f1be882" />

**6. Riwayat pembayaran** 

Opsi ini menampilkan riwayat transaksi ``User`` pada ``petHouse``. <br>
<img width="452" height="422" alt="image" src="https://github.com/user-attachments/assets/a77a3c20-d00e-4b0b-b8cf-2e8c4d11308d" />

**7. Status hewan**

Opsi ini menampilkan kepada ``User`` apakah hewan peliharaanya sudah digrooming atau belum. <br> 
<img width="395" height="407" alt="image" src="https://github.com/user-attachments/assets/5c447ed6-93c6-4f42-b057-64aa573bda58" />

**8. Invoice setelah transaksi**

Apabila ``User`` telah melakukan transaksi maka sistem akan menampilkan invoice pembayaran. <br>
<img width="701" height="661" alt="image" src="https://github.com/user-attachments/assets/e5604284-af85-44a2-867d-3962d82b8d0c" />
