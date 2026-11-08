"""
Tugas Minggu 9: test untuk peminjaman.py.

Ketentuan:
- pakai @pytest.mark.parametrize untuk menguji beberapa titik batas sekaligus
- pakai minimal satu fixture
- pakai pytest.raises untuk input yang tidak valid

Jalankan: pytest test_peminjaman.py -v
"""
import pytest

from peminjaman import cek_kelayakan_pinjam, hitung_denda


# Tulis test Anda di bawah ini.

# ===== Siklus 1: denda setelah masa tenggang =====
def test_denda_setelah_tenggang():
    # Arrange
    hari = 3
    # Act
    hasil = hitung_denda(hari)
    # Assert
    assert hasil == 3000   # (3 - 1) x 1500


# ===== Siklus 2: grace period dan cap =====
@pytest.mark.parametrize("hari, harapan", [
    (0, 0),
    (1, 0),         # tepat di grace period
    (2, 1500),      # satu hari setelah grace
    (14, 19500),    # terakhir sebelum cap
    (15, 20000),    # (15-1) x 1500 = 21000, kena cap
    (100, 20000),
])
def test_hitung_denda(hari, harapan):
    assert hitung_denda(hari) == harapan


# ===== Siklus 3: input negatif =====
@pytest.mark.parametrize("hari", [-1, -5, -100])
def test_hari_negatif_ditolak(hari):
    with pytest.raises(ValueError):
        hitung_denda(hari)


# ===== Siklus 4: kelayakan pinjam =====
@pytest.fixture
def batas():
    return {"reguler": 4, "premium": 7}


def test_reguler_tepat_batas_tidak_layak(batas):
    assert cek_kelayakan_pinjam("Reguler", batas["reguler"]) is False


def test_reguler_satu_di_bawah_batas_layak(batas):
    assert cek_kelayakan_pinjam("Reguler", batas["reguler"] - 1) is True


def test_premium_tepat_batas_tidak_layak(batas):
    assert cek_kelayakan_pinjam("Premium", batas["premium"]) is False


def test_premium_satu_di_bawah_batas_layak(batas):
    assert cek_kelayakan_pinjam("Premium", batas["premium"] - 1) is True


# ===== Siklus 5: huruf besar/kecil, tier tidak dikenal, jumlah negatif =====
@pytest.mark.parametrize("tier", ["reguler", "REGULER", "Reguler", "rEgUlEr"])
def test_tier_reguler_tidak_peka_huruf(tier, batas):
    assert cek_kelayakan_pinjam(tier, batas["reguler"] - 1) is True
    assert cek_kelayakan_pinjam(tier, batas["reguler"]) is False


@pytest.mark.parametrize("tier", ["premium", "PREMIUM", "Premium", "pReMiUm"])
def test_tier_premium_tidak_peka_huruf(tier, batas):
    assert cek_kelayakan_pinjam(tier, batas["premium"] - 1) is True
    assert cek_kelayakan_pinjam(tier, batas["premium"]) is False


@pytest.mark.parametrize("tier", ["Gold", "", "VIP", "regular"])
def test_tier_tidak_dikenal_ditolak(tier):
    with pytest.raises(ValueError):
        cek_kelayakan_pinjam(tier, 1)


@pytest.mark.parametrize("tier", ["Reguler", "Premium"])
def test_jumlah_negatif_ditolak(tier):
    with pytest.raises(ValueError):
        cek_kelayakan_pinjam(tier, -1)

# ===== Siklus 6: nol pinjaman dan tier bukan string =====
def test_nol_pinjaman_layak():
    assert cek_kelayakan_pinjam("Reguler", 0) is True
    assert cek_kelayakan_pinjam("Premium", 0) is True


def test_tier_bukan_string_ditolak():
    with pytest.raises(ValueError):
        cek_kelayakan_pinjam(None, 1)