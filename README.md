# Pengujian Perangkat Lunak

Repositori tugas dan latihan mata kuliah Pengujian Perangkat Lunak (IF25-40203),
Teknik Informatika, Institut Teknologi Sumatera.

Studi kasus yang dipakai: **PustakaKita**, layanan sirkulasi perpustakaan
(denda, kelayakan pinjam, dan perpanjangan).

## Isi repositori

| Folder | Pertemuan | Topik |
|---|---|---|
| [Demo_m09](Demo_m09) | 9 | Unit Testing dan Test-Driven Development (Red, Green, Refactor) |

Folder lain akan ditambahkan seiring pertemuan berikutnya.

## Struktur

```
Pengujian_perangkat_Lunak
├── .gitignore
├── README.md           # dokumen ini
└── Demo_m09
    ├── anggota.py
    ├── test_anggota.py
    ├── README.md       # penjelasan lengkap demo beserta screenshot
    └── ss/
```

## Cara menjalankan

Pasang Python dan pytest, lalu jalankan test dari dalam folder pertemuan:

```powershell
python -m pip install pytest
cd Demo_m09
python -m pytest -q
```

Penjelasan lengkap tiap tahap (Red, Green, Refactor) ada di
[Demo_m09/README.md](Demo_m09/README.md).
