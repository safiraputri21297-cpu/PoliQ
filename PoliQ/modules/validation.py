
"""
validation.py
Modul untuk memvalidasi data pasien PoliQ.
"""


def validate_patient(nama, keluhan):
    """
    Memeriksa apakah nama dan keluhan pasien valid.
    """

    # Menghapus spasi di awal dan akhir teks
    nama = nama.strip()
    keluhan = keluhan.strip()

    # Memeriksa nama pasien
    if nama == "":
        raise ValueError("Nama pasien wajib diisi.")

    if len(nama) > 100:
        raise ValueError("Nama pasien maksimal 100 karakter.")

    # Memeriksa keluhan pasien
    if keluhan == "":
        raise ValueError("Keluhan pasien wajib diisi.")

    if len(keluhan) > 200:
        raise ValueError("Keluhan maksimal 200 karakter.")

    return nama, keluhan


def validate_status(status):
    """
    Memeriksa apakah status antrean sesuai pilihan.
    """

    status_valid = [
        "Menunggu",
        "Dipanggil",
        "Sedang Dilayani",
        "Selesai",
        "Tidak Hadir",
        "Terlewat"
    ]

    if status not in status_valid:
        raise ValueError("Status antrean tidak valid.")

    return status
