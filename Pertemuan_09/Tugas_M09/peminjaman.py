"""
Tugas Minggu 9: Unit Testing dan TDD, modul peminjaman PustakaKita.
Varian NIM 124140018.
"""

import re

DENDA_PER_HARI = 1500
GRACE_PERIOD = 1
DENDA_MAKS = 20000
BATAS_REGULER = 4
BATAS_PREMIUM = 7


# ===== TAHAP 1: RED =====
# def hitung_denda(hari_terlambat):
#     raise NotImplementedError
#
#
# def cek_kelayakan_pinjam(tier, jumlah_aktif):
#     raise NotImplementedError


# ===== TAHAP 2: GREEN =====
# --- hitung_denda siklus 1 ---
# def hitung_denda(hari_terlambat):
#     return (hari_terlambat - GRACE_PERIOD) * DENDA_PER_HARI

# --- hitung_denda siklus 2 ---
# def hitung_denda(hari_terlambat):
#     if hari_terlambat <= GRACE_PERIOD:
#         return 0
#     denda = (hari_terlambat - GRACE_PERIOD) * DENDA_PER_HARI
#     if denda > DENDA_MAKS:
#         return DENDA_MAKS
#     return denda

# --- hitung_denda siklus 3 ---
# def hitung_denda(hari_terlambat):
#     if hari_terlambat < 0:
#         raise ValueError("hari_terlambat tidak boleh negatif")
#     if hari_terlambat <= GRACE_PERIOD:
#         return 0
#     denda = (hari_terlambat - GRACE_PERIOD) * DENDA_PER_HARI
#     if denda > DENDA_MAKS:
#         return DENDA_MAKS
#     return denda

# --- cek_kelayakan_pinjam siklus 4 ---
# def cek_kelayakan_pinjam(tier, jumlah_aktif):
#     if tier == "Reguler":
#         return jumlah_aktif < BATAS_REGULER
#     return jumlah_aktif < BATAS_PREMIUM

# --- cek_kelayakan_pinjam siklus 5 ---
# def cek_kelayakan_pinjam(tier, jumlah_aktif):
#     if jumlah_aktif < 0:
#         raise ValueError("jumlah_aktif tidak boleh negatif")
#     nama = tier.lower()
#     if nama == "reguler":
#         return jumlah_aktif < BATAS_REGULER
#     if nama == "premium":
#         return jumlah_aktif < BATAS_PREMIUM
#     raise ValueError("tier tidak dikenal")


# ===== TAHAP 3: REFACTOR =====
def hitung_denda(hari_terlambat):
    if hari_terlambat < 0:
        raise ValueError("hari_terlambat tidak boleh negatif")
    if hari_terlambat <= GRACE_PERIOD:
        return 0
    return min((hari_terlambat - GRACE_PERIOD) * DENDA_PER_HARI, DENDA_MAKS)


def cek_kelayakan_pinjam(tier, jumlah_aktif):
    if jumlah_aktif < 0:
        raise ValueError("jumlah_aktif tidak boleh negatif")
    if not isinstance(tier, str):
        raise ValueError("tier tidak dikenal")
    nama = tier.lower()
    if nama == "reguler":
        return jumlah_aktif < BATAS_REGULER
    if nama == "premium":
        return jumlah_aktif < BATAS_PREMIUM
    raise ValueError("tier tidak dikenal")


def validasi_id_anggota(id_anggota):
    """True jika ID anggota valid: huruf A kapital diikuti tepat empat angka (0-9)."""
    if not isinstance(id_anggota, str):
        raise TypeError("id_anggota harus berupa string")
    return re.fullmatch(r"A[0-9]{4}", id_anggota) is not None