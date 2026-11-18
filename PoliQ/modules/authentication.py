
"""
authentication.py
Modul untuk mengelola akun pengguna PoliQ.
Menggunakan file CSV.
"""

import csv
from pathlib import Path
from uuid import uuid4

# Menentukan lokasi file akun
ACCOUNT_FILE = Path(__file__).resolve().parent.parent / "data" / "akun.csv"

# Menentukan kolom akun
FIELDNAMES = ["id", "nama", "username", "password", "role"]


class Authentication:
    """
    Class untuk mengelola registrasi dan login pengguna.
    """

    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """Membaca data akun dari file CSV."""

        try:
            with open(
                ACCOUNT_FILE, "r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)
                return list(reader)

        except FileNotFoundError:
            return []

        except csv.Error as error:
            raise ValueError("File akun.csv tidak valid.") from error

    def save_accounts(self):
        """Menyimpan data akun ke file CSV."""

        ACCOUNT_FILE.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(
                ACCOUNT_FILE, "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=FIELDNAMES
                )

                writer.writeheader()
                writer.writerows(self.accounts)

        except (OSError, csv.Error) as error:
            raise OSError("Gagal menyimpan akun.") from error

    def register(self, nama, username, password):
        """Mendaftarkan akun pasien baru."""

        nama = nama.strip()
        username = username.strip()

        if not nama or not username or not password:
            raise ValueError("Semua data wajib diisi.")

        if len(username) < 4:
            raise ValueError("Username minimal 4 karakter.")

        if len(password) < 6:
            raise ValueError("Password minimal 6 karakter.")

        # Memeriksa username yang sudah digunakan
        for akun in self.accounts:
            if akun["username"].lower() == username.lower():
                raise ValueError("Username sudah digunakan.")

        akun_baru = {
            "id": str(uuid4()),
            "nama": nama,
            "username": username,
            "password": password,
            "role": "pasien"
        }

        self.accounts.append(akun_baru)
        self.save_accounts()

        return akun_baru

    def login(self, username, password):
        """Memeriksa username dan password pengguna."""

        for akun in self.accounts:
            if (
                akun["username"].lower() == username.strip().lower()
                and akun["password"] == password
            ):
                return akun

        return None
