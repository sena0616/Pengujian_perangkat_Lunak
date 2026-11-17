# Pengujian Perangkat Lunak

Repository dokumentasi praktikum, tugas, dan implementasi pengujian perangkat lunak pada mata kuliah **Pengujian Perangkat Lunak (IF25-40203)**, Program Studi Teknik Informatika, Institut Teknologi Sumatera.

Repository ini berisi kumpulan latihan dan tugas yang membahas penerapan konsep software testing, mulai dari Unit Testing, Test-Driven Development (TDD), hingga Automation Testing.

Studi kasus yang digunakan dalam praktikum ini adalah **PustakaKita**, sebuah layanan sirkulasi perpustakaan yang mencakup pengelolaan denda, kelayakan peminjaman, dan perpanjangan masa pinjam.

---

## Daftar Pertemuan

| Folder | Pertemuan | Materi | Deskripsi |
|:---|:---:|:---|:---|
| [Pertemuan_09](Pertemuan_09/) | 09 | Unit Testing & TDD | Implementasi pengujian menggunakan pendekatan Red, Green, Refactor. |
| [Pertemuan_10](Pertemuan_10/) | 10 | Automation Testing | Proyek pengujian otomatis menggunakan file Selenium IDE (.side). |

## Struktur Repository

```text
Pengujian_perangkat_Lunak/
│
├── Pertemuan_09/
│   │
│   ├── Demo_m09/
│   │   ├── anggota.py
│   │   ├── test_anggota.py
│   │   ├── README.md
│   │   └── ss/
│   │       ├── Tahap_Red.png
│   │       ├── Tahap_Green.png
│   │       └── Tahap_Refactor.png
│   │
│   └── Tugas_M09/
│       ├── peminjaman.py
│       └── test_peminjaman.py
│
├── Pertemuan_10/
│   └── PustakaKita_124140018.side
│
├── .gitignore
└── README.md
```

## Dokumentasi Praktikum

### Pertemuan 09 — Unit Testing dan Test-Driven Development

Pertemuan ini membahas pengujian unit untuk memastikan setiap fungsi berjalan sesuai dengan hasil yang diharapkan.

**Demo M09**

Implementasi Test-Driven Development (TDD) dengan tiga tahapan utama:

- **Red:** Membuat pengujian yang awalnya menghasilkan kegagalan.
- **Green:** Menulis kode agar pengujian berhasil.
- **Refactor:** Memperbaiki struktur kode tanpa mengubah fungsionalitas.

File utama:
- `anggota.py`
- `test_anggota.py`

**Tugas M09**

Implementasi pengujian fungsi peminjaman pada layanan PustakaKita menggunakan Pytest.

File utama:
- `peminjaman.py`
- `test_peminjaman.py`

### Pertemuan 10 — Automation Testing

Pertemuan ini berisi proyek automation testing untuk studi kasus PustakaKita.

File utama:
- `PustakaKita_124140018.side`

File tersebut merupakan proyek Selenium IDE yang digunakan sebagai dokumentasi pengujian otomatis.

---

## Teknologi dan Tools

| Tools | Kegunaan |
|:---|:---|
| Python | Bahasa pemrograman untuk implementasi fungsi dan unit testing. |
| Pytest | Framework untuk menjalankan pengujian unit. |
| Selenium IDE | Tools untuk membuat dan menjalankan pengujian otomatis. |
| Git & GitHub | Version control dan pengelolaan repository. |

## Cara Menjalankan Pengujian

### 1. Persiapan

Pastikan Python dan Pytest sudah terpasang.

```bash
python --version
python -m pytest --version
```

Jika Pytest belum tersedia, instal menggunakan:

```bash
pip install pytest
```

### 2. Menjalankan Demo M09

Masuk ke direktori Demo M09:

```bash
cd Pertemuan_09/Demo_m09
```

Jalankan pengujian:

```bash
python -m pytest -q
```

### 3. Menjalankan Tugas M09

Dari direktori utama repository, jalankan:

```bash
cd Pertemuan_09/Tugas_M09
```

Kemudian jalankan:

```bash
python -m pytest -v
```

### 4. Menjalankan Automation Testing M10

1. Instal atau buka Selenium IDE pada browser yang didukung.
2. Buka Selenium IDE.
3. Pilih opsi untuk membuka proyek yang sudah ada.
4. Pilih file `Pertemuan_10/PustakaKita_124140018.side`.
5. Jalankan test case yang tersedia.

---

## Tujuan Praktikum

Melalui rangkaian praktikum ini, diharapkan dapat memahami dan menerapkan:

- Konsep dasar pengujian perangkat lunak.
- Implementasi Unit Testing menggunakan Pytest.
- Pendekatan Test-Driven Development (Red, Green, Refactor).
- Pengujian fungsi berdasarkan skenario yang telah ditentukan.
- Penerapan Automation Testing menggunakan Selenium IDE.
- Pengelolaan kode dan dokumentasi menggunakan Git dan GitHub.

---

## Informasi Repository

| Keterangan | Detail |
|:---|:---|
| Mata Kuliah | Pengujian Perangkat Lunak |
| Kode Mata Kuliah | IF25-40203 |
| Program Studi | Teknik Informatika |
| Institusi | Institut Teknologi Sumatera |
| Studi Kasus | PustakaKita |
| Repository | Pengujian Perangkat Lunak |

---

*Repository ini disusun sebagai dokumentasi kegiatan praktikum dan penyelesaian tugas mata kuliah Pengujian Perangkat Lunak.*
