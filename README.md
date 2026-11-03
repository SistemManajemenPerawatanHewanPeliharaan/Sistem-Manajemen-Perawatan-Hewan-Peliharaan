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
<img width="400" alt="Screenshot 2026-11-02 203541" src="https://github.com/user-attachments/assets/cbc630c2-c9e9-4827-b7ff-ead0a5a08f3a" />

a. Apabila user menginput text ataupun input selain dari opsi yang diberikan, program akan menampilkan ``"Pilihan tidak Valid."`` dan akan kembali meminta user untuk menginput setelah 1 detik.

<br>
<img width="300" alt="Screenshot 2026-11-02 203750" src="https://github.com/user-attachments/assets/c7bd2c2c-60f7-4224-8760-9e7170a915fe" />

#### Menu Login
Program akan meminta meng-*input*kan Username dan Password yang sudah dibuat di menu registrasi sebelumnya. <br>
a. Login berhasil sebagai ``SuperAdmin``, khusus ``SuperAdmin`` Username dan Password sudah disediakan. <br>
<img width="300" alt="Screenshot 2026-11-02 205828" src="https://github.com/user-attachments/assets/220e3a29-ba96-436a-a7fe-6f31e59ec785" />

b. Login berhasil sebagai ``User``, untuk ``User`` **wajib** melakukan registrasi terlebih dahulu agar akunnya terdaftar.

<br>
<img width="300" alt="Screenshot 2026-11-02 205911" src="https://github.com/user-attachments/assets/f8c24e2d-b6fa-4cae-9cd3-4362f0c189a1" />

c. Apabila password salah, percobaan salah hanya 3 kali apabila lebih dari 3 kali maka akan diberi jeda 60 detik untuk men-_input___ username dan password kembali.

<br>
<img width="300" alt="Screenshot 2026-11-02 204408" src="https://github.com/user-attachments/assets/d5677731-c4c9-4ea7-b450-c14326b235eb" />

### Menu Registrasi
Program akan meminta meng-*input*kan username, password, dan pin untuk top-up atau pembayaran nanti. <br>
a. Registrasi berhasil setelah meng-_input_ username dan password baru.

<br>
<img width="300" alt="Screenshot 2026-11-02 205402" src="https://github.com/user-attachments/assets/ce4df161-1fda-4d20-a4d2-c0d0718a34ab" />

b. Apabila username sudah terpakai 

<br>
<img width="300" alt="Screenshot 2026-11-02 205429" src="https://github.com/user-attachments/assets/ea4d03de-3d0a-4681-9963-71975a0f5369" />

### SuperAdmin
#### menu superadmin
<img width="300" alt="Screenshot 2026-11-02 211939" src="https://github.com/user-attachments/assets/2ef3cd4f-0422-4cdb-abf3-e945d728cc0d" />

#### tambah data pelanggan
<img width="300" alt="Screenshot 2026-11-02 212151" src="https://github.com/user-attachments/assets/db1f8cd8-7789-4e6d-9029-5bf585e8a360" />

#### lihat data pelanggan
<img width="500" alt="Screenshot 2026-11-02 212214" src="https://github.com/user-attachments/assets/8cbe8f2b-f6b4-4663-a613-373c5e7fbd3d" />

#### lihat antrian pelanggan
<img width="300" alt="Screenshot 2026-11-02 212228" src="https://github.com/user-attachments/assets/d57d418f-0c5d-4736-b2f6-2223814f6cf1" />

#### perbarui data pelanggan
<img width="500" alt="Screenshot 2026-11-02 212312" src="https://github.com/user-attachments/assets/522ab9b5-9b3e-4920-881b-00319118a4ea" />

#### hapus data pelanggan
<img width="500" alt="Screenshot 2026-11-02 212531" src="https://github.com/user-attachments/assets/2f4e86b9-e046-4260-8de2-c8fd09c8ea9b" />

#### lihat laporan keuangan
<img width="300" alt="Screenshot 2026-11-02 212547" src="https://github.com/user-attachments/assets/d557b949-f0b8-46dc-92f7-bb26db008c07" />



### User

<img width="1030" height="545" alt="image" src="https://github.com/user-attachments/assets/cb13696f-120e-4c04-a16c-7d252b06ec0c" />

<img width="727" height="232" alt="image" src="https://github.com/user-attachments/assets/dab0ad32-72c2-4485-ae4c-868f2ed2028c" />

<img width="411" height="330" alt="image" src="https://github.com/user-attachments/assets/7f4defe7-e86a-4a71-a0fb-ae8b445cd192" />

<img width="486" height="413" alt="image" src="https://github.com/user-attachments/assets/f07dfc8c-7a6d-4588-9a93-007c5d304ea2" />

<img width="565" height="293" alt="image" src="https://github.com/user-attachments/assets/7a1865e5-0f1b-4e94-acba-2cd10f1be882" />

<img width="452" height="422" alt="image" src="https://github.com/user-attachments/assets/a77a3c20-d00e-4b0b-b8cf-2e8c4d11308d" />

<img width="701" height="661" alt="image" src="https://github.com/user-attachments/assets/e5604284-af85-44a2-867d-3962d82b8d0c" />

<img width="395" height="407" alt="image" src="https://github.com/user-attachments/assets/5c447ed6-93c6-4f42-b057-64aa573bda58" />







