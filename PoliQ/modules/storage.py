
"""
storage.py
Modul untuk membaca dan menyimpan data pasien PoliQ.
Menggunakan file CSV.
"""

import csv
from pathlib import Path

# Menentukan lokasi file pasien.csv
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "pasien.csv"

# Menentukan kolom data pasien
FIELDNAMES = [
    "id",
    "nomor_antrian",
    "tanggal",
    "waktu_daftar",
    "nama",
    "keluhan",
    "status",
    "waktu_mulai",
    "waktu_selesai",
    "durasi"
]


def load_data():
    """
    Membaca data pasien dari file CSV.
    """

    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        # Mengubah durasi menjadi angka
        for pasien in data:
            pasien["durasi"] = float(pasien["durasi"])

        return data

    except FileNotFoundError:
        return []

    except (csv.Error, ValueError, KeyError) as error:
        raise ValueError("File pasien.csv tidak valid.") from error


def save_data(data):
    """
    Menyimpan data pasien ke file CSV.
    """

    if not isinstance(data, list):
        raise ValueError("Data pasien harus berbentuk list.")

    # Membuat folder data jika belum tersedia
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=FIELDNAMES
            )

            # Menulis judul kolom
            writer.writeheader()

            # Menulis seluruh data pasien
            writer.writerows(data)

    except (OSError, csv.Error) as error:
        raise OSError("Gagal menyimpan data pasien.") from error
