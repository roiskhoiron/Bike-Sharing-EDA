# Dataset Berbagi Sepeda

**Hadi Fanaee-T**

Laboratorium Kecerdasan Buatan dan Dukungan Keputusan (LIAAD), Universitas Porto  
INESC Porto, Kampus FEUP  
Rua Dr. Roberto Frias, 378  
4200 - 465 Porto, Portugal

## Latar Belakang

Sistem berbagi sepeda adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari pendaftaran anggota, penyewaan, dan pengembalian menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari satu lokasi dan mengembalikannya di lokasi lain. Saat ini, ada lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari lebih dari 500 ribu sepeda. Saat ini, ada minat besar terhadap sistem ini karena perannya yang penting dalam masalah lalu lintas, lingkungan, dan kesehatan.

Selain aplikasi dunia nyata yang menarik dari sistem berbagi sepeda, karakteristik data yang dihasilkan oleh sistem ini menjadikannya menarik untuk penelitian. Berbeda dengan layanan transportasi lain seperti bus atau kereta bawah tanah, durasi perjalanan, posisi keberangkatan dan kedatangan secara eksplisit dicatat dalam sistem ini. Fitur ini mengubah sistem berbagi sepeda menjadi jaringan sensor virtual yang dapat digunakan untuk mendeteksi mobilitas di kota. Oleh karena itu, diharapkan sebagian besar peristiwa penting di kota dapat terdeteksi dengan memantau data ini.

## Set Data

Proses penyewaan sepeda sangat berkorelasi dengan kondisi lingkungan dan musiman. Misalnya, kondisi cuaca, curah hujan, hari dalam minggu, musim, jam dalam sehari, dll., dapat mempengaruhi perilaku penyewaan. Data inti berkaitan dengan log historis dua tahun yang sesuai dengan tahun 2011 dan 2012 dari sistem Capital Bikeshare, Washington D.C., AS, yang tersedia secara publik di [http://capitalbikeshare.com/system-data](http://capitalbikeshare.com/system-data). Kami mengagregasi data pada basis dua jam dan harian, kemudian mengekstraksi dan menambahkan informasi cuaca dan musiman yang sesuai. Informasi cuaca diambil dari [http://www.freemeteo.com](http://www.freemeteo.com).

## Tugas Terkait

- **Regresi**:  
  Prediksi jumlah penyewaan sepeda setiap jam atau setiap hari berdasarkan kondisi lingkungan dan musiman.
  
- **Deteksi Peristiwa dan Anomali**:  
  Jumlah sepeda yang disewa juga berkorelasi dengan beberapa peristiwa di kota yang mudah dilacak melalui mesin pencari. Misalnya, pencarian dengan query seperti "2012-10-30 washington d.c." di Google akan menampilkan hasil terkait dengan Badai Sandy. Beberapa peristiwa penting diidentifikasi dalam [1]. Oleh karena itu, data ini juga dapat digunakan untuk validasi algoritma deteksi anomali atau peristiwa.

## Berkas

- `Readme.txt`
- `hour.csv`: jumlah penyewaan sepeda yang diakumulasi setiap jam. Catatan: 17379 jam
- `day.csv`: jumlah penyewaan sepeda yang diakumulasi setiap hari. Catatan: 731 hari

## Karakteristik Dataset

Baik `hour.csv` dan `day.csv` memiliki kolom berikut, kecuali `hr` yang tidak tersedia di `day.csv`:

- `instant`: indeks catatan
- `dteday`: tanggal
- `season`: musim (1:musim semi, 2:musim panas, 3:musim gugur, 4:musim dingin)
- `yr`: tahun (0: 2011, 1:2012)
- `mnth`: bulan (1 sampai 12)
- `hr`: jam (0 sampai 23)
- `holiday`: apakah hari itu libur atau tidak (diambil dari [http://dchr.dc.gov/page/holiday-schedule](http://dchr.dc.gov/page/holiday-schedule))
- `weekday`: hari dalam minggu
- `workingday`: jika hari tersebut bukan akhir pekan atau libur, nilainya adalah 1, sebaliknya adalah 0.
- `weathersit`: 
  - 1: Cerah, Sedikit awan, Sebagian berawan
  - 2: Kabut + Berawan, Kabut + Awan terpecah, Kabut + Sedikit awan, Kabut
  - 3: Salju ringan, Hujan ringan + Badai + Awan terpecah, Hujan ringan + Awan terpecah
  - 4: Hujan lebat + Es + Badai + Kabut, Salju + Kabut
- `temp`: Suhu yang dinormalisasi dalam Celsius. Nilai dibagi dengan 41 (maksimum)
- `atemp`: Suhu yang dirasakan dinormalisasi dalam Celsius. Nilai dibagi dengan 50 (maksimum)
- `hum`: Kelembaban yang dinormalisasi. Nilai dibagi dengan 100 (maksimum)
- `windspeed`: Kecepatan angin yang dinormalisasi. Nilai dibagi dengan 67 (maksimum)
- `casual`: jumlah pengguna kasual
- `registered`: jumlah pengguna terdaftar
- `cnt`: jumlah total penyewaan sepeda termasuk pengguna kasual dan terdaftar

## Lisensi

Penggunaan dataset ini dalam publikasi harus mengutip publikasi berikut:

[1] Fanaee-T, Hadi, dan Gama, Joao, "Pelabelan peristiwa menggabungkan detektor ensembel dan pengetahuan latar belakang", Progress in Artificial Intelligence (2013): hlm. 1-15, Springer Berlin Heidelberg, doi:10.1007/s13748-013-0040-3.

@artikel{  
  tahun={2013},  
  issn={2192-6352},  
  jurnal={Progress in Artificial Intelligence},  
  doi={10.1007/s13748-013-0040-3},  
  judul={Pelabelan peristiwa menggabungkan detektor ensembel dan pengetahuan latar belakang},  
}