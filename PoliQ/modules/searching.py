
"""
searching.py
Modul untuk mencari data pasien PoliQ.
Menggunakan algoritma Linear Search.
"""


def cari_pasien(data, kata_kunci):
    """
    Mencari pasien berdasarkan nama, ID,
    atau nomor antrean.
    """

    # Menyiapkan tempat untuk hasil pencarian
    hasil = []

    # Mengubah kata kunci menjadi huruf kecil
    kata_kunci = kata_kunci.lower().strip()

    # Memeriksa setiap data pasien satu per satu
    for pasien in data:

        nama = pasien["nama"].lower()
        id_pasien = pasien["id"].lower()
        nomor = pasien["nomor_antrian"].lower()

        # Memeriksa apakah kata kunci cocok
        if (
            kata_kunci in nama
            or kata_kunci in id_pasien
            or kata_kunci in nomor
        ):
            hasil.append(pasien)

    return hasil
