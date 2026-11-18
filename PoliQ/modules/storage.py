
"""
storage.py
Modul untuk membaca dan menyimpan data pasien PoliQ.
"""

import json
from pathlib import Path

# Menentukan lokasi file pasien.json
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "pasien.json"


def load_data():
    """
    Membaca data pasien dari file JSON.
    """

    try:
        # Membuka file dalam mode membaca
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Memastikan data berbentuk list
        if not isinstance(data, list):
            raise ValueError("Format data pasien tidak valid.")

        return data

    except FileNotFoundError:
        # Jika file belum ditemukan, mengembalikan list kosong
        return []

    except json.JSONDecodeError:
        # Jika isi file JSON rusak
        raise ValueError("File pasien.json tidak dapat dibaca.")


def save_data(data):
    """
    Menyimpan data pasien ke dalam file JSON.
    """

    # Memastikan data berbentuk list
    if not isinstance(data, list):
        raise ValueError("Data pasien harus berbentuk list.")

    # Membuat folder data jika belum tersedia
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Membuka file dalam mode menulis
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
