import pytest
from anggota import validasi_id_anggota


@pytest.fixture
def anggota_terdaftar():
    return ["A1001", "A1002", "A1006"]


@pytest.mark.parametrize("id_anggota, harapan", [
    ("A1001", True),  ("a1001", False),
    ("A100", False),  ("A10011", False),
    ("B1001", False), ("A10O1", False),
])
def test_format_id(id_anggota, harapan):
    assert validasi_id_anggota(id_anggota) is harapan


def test_anggota_terdaftar_valid(anggota_terdaftar):
    for id_anggota in anggota_terdaftar:
        assert validasi_id_anggota(id_anggota)


def test_bukan_string_ditolak():
    with pytest.raises(TypeError):
        validasi_id_anggota(1001)