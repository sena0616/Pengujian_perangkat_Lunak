# ===== TAHAP 1: RED (komentar) =====
# def validasi_id_anggota(id_anggota):
#     pass


# ===== TAHAP 2: GREEN (komentar) =====
# def validasi_id_anggota(id_anggota):
#     if not isinstance(id_anggota, str):
#         raise TypeError("ID anggota harus string")
#     if len(id_anggota) != 5:
#         return False
#     if id_anggota[0] != "A":
#         return False
#     for c in id_anggota[1:]:
#         if c not in "0123456789":
#             return False
#     return True


# ===== TAHAP 3: REFACTOR (yang dipakai) =====
import re

POLA_ID = re.compile(r"A[0-9]{4}")


def validasi_id_anggota(id_anggota):
    if not isinstance(id_anggota, str):
        raise TypeError("ID anggota harus string")
    return POLA_ID.fullmatch(id_anggota) is not None