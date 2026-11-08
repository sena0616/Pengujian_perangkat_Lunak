# Pengujian Perangkat Lunak

Repositori tugas dan latihan mata kuliah Pengujian Perangkat Lunak (IF25-40203), Teknik Informatika, Institut Teknologi Sumatera.

Studi kasus yang digunakan: **PustakaKita**, layanan sirkulasi perpustakaan (denda, kelayakan pinjam, dan perpanjangan).

## Isi Repositori

| Folder | Pertemuan | Topik |
|---|---|---|
| [Demo_m09](Demo_m09) | 9 | Unit Testing dan Test-Driven Development (Red, Green, Refactor) |
| [Tugas_M09](Tugas_M09) | 9 | Pengujian fungsi peminjaman menggunakan Pytest |

## Struktur

```text
Pengujian_perangkat_Lunak/
├── .gitignore
├── README.md
├── Demo_m09/
│   ├── anggota.py
│   ├── test_anggota.py
│   ├── README.md
│   └── ss/
│       ├── Tahap_Red.png
│       ├── Tahap_Green.png
│       └── Tahap_Refactor.png
└── Tugas_M09/
    ├── peminjaman.py
    └── test_peminjaman.py
```

## Cara Menjalankan

Pastikan Python dan pytest sudah terpasang.

**1. Menjalankan Demo M09**

```powershell
cd Demo_m09
python -m pytest -q
```

**2. Menjalankan Tugas M09**

```powershell
cd Tugas_M09
python -m pytest -v
```

Untuk melihat dokumentasi lengkap Demo M09, kunjungi [Demo_m09/README.md](Demo_m09/README.md).
