# Algeo02-22065
Tugas Besar 2 Aljabar dan Linear Geometri

Aplikasi Aljabar Vektor dalam Sistem Temu Balik Gambar

Content-Based Image Retrieval (CBIR) adalah sebuah proses yang digunakan untuk mencari dan mengambil gambar berdasarkan kontennya. Proses ini dimulai dengan ekstraksi fitur-fitur penting dari gambar, seperti warna, tekstur, dan bentuk. Setelah fitur-fitur tersebut diekstraksi, mereka diwakili dalam bentuk vektor atau deskripsi numerik yang dapat dibandingkan dengan gambar lain. 

Kemudian, CBIR menggunakan algoritma pencocokan untuk membandingkan vektor-fitur dari gambar yang dicari dengan vektor-fitur gambar dalam dataset. Hasil dari pencocokan ini digunakan untuk mengurutkan gambar-gambar dalam dataset dan menampilkan gambar yang paling mirip dengan gambar yang dicari. Proses CBIR membantu pengguna dalam mengakses dan mengeksplorasi koleksi gambar dengan cara yang lebih efisien, karena tidak memerlukan pencarian berdasarkan teks atau kata kunci, melainkan berdasarkan kesamaan nilai citra visual antara gambar-gambar tersebut. 

Dalam Tugas Besar ini, digunakan parameter warna dan tekstur dalam CBIR.

## Anggota Kelompok

| NIM      | Nama                         | Tanggung Jawab                                               |
|----------|------------------------------|--------------------------------------------------------------|
| 13522065 | Rafiki Prawhira Harianto     | Struktur Utama Website, Design, Testing                      |
| 13522088 | Muhamad Rafli Rasyiidin      | CBIR Texture, Optimasi Kecepatan Algoritma Pencarian         |
| 13522100 | M. Hanief Fatkhan Nashrullah | CBIR Color, Website Pagination, Optimasi Kecepatan Algoritma |

## Installation & Run Program

Dalam command line, buat git clone
`git clone https://github.com/Intermaze/Algeo02-22065`

Install Python version 3.11.6: https://www.python.org/downloads/
Pastikan add pip to PATH dengan installasi pythonnya

Install juga Node.js melalui : https://nodejs.org/en/

Setelah Python dan Node.js terinstall, buka terminal di folder src dari repository yang telah diclone

Kemudian, library yang digunakan python
`pip install -r requirements.txt`

Install pula package lain
`npm install`

Run programmnya
`npm run start`

Seharusnya terlihat output seperti ini
`* Running on http://127.0.0.1:5000`

Terakhir, buka link http://127.0.0.1:5000 menggunakan web browser Anda.

## Struktur Program

```md
test/
├─ dataset1/
├─ dataset2/
├─ dataset3/
├─ imagetest/
doc/
├─ Algeo02-22065.pdf
img/
├─ elaina1.png
├─ elaina2.png
├─ elaina3.png
├─ elaina4.png
src/
├─ app.py
├─ requirements.txt
├─ extraction_func.py
├─ load_features.py
├─ tailwind.config.js
├─ package.json
├─ feature_extraction.py
├─ package-lock.json
├─ dataset_features/
│  ├─ hsv/
│  │  ├─ sample.jpg.npy
│  ├─ texture/
│  │  ├─ sample.jpg.npy
├─ static/
│  ├─ css/
│  │  ├─ main.css
│  ├─ dataset/
│  │  ├─ sample.jpg
│  ├─ script/
│  │  ├─ script.js
│  │  ├─ pagination.js
│  ├─ src/
│  │  ├─ input.css
│  ├─ uploads/
│  │  ├─ image_sample.jpg
│  ├─ Image/
│  │  ├─ fotokelompok.jpg
│  │  ├─ sample.jpg
├─ templates/
│  ├─ index.html
│  ├─ about_page.html
.gitignore
README.md
```

## Screenshots
### Pencarian Dengan Parameter Warna
![Test 1](/img/elaina1.png)
![Test 2](/img/elaina2.png)

### Pencarian Dengan Parameter Tekstur
![Test 3](/img/elaina3.png)
![Test 4](/img/elaina4.png)

## Contact 
Rafiki : 13522065@std.stei.itb.ac.id

Rafli  : 13522088@std.stei.itb.ac.id

Hanif  : 13522100@std.stei.itb.ac.id
