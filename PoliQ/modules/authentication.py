
"""
authentication.py
Modul untuk mengelola akun dan proses login PoliQ.
"""

import json
from pathlib import Path
from uuid import uuid4

# Menentukan lokasi file akun
ACCOUNT_FILE = Path(__file__).resolve().parent.parent / "data" / "akun.json"


class Authentication:
    """
    Class untuk mengelola registrasi dan login pengguna.
    """

    def __init__(self):
        # Memuat data akun saat objek dibuat
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """
        Membaca data akun dari file JSON.
        """

        try:
            with open(ACCOUNT_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Format data akun tidak valid.")

            return data

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            raise ValueError("File akun.json rusak.")

    def save_accounts(self):
        """
        Menyimpan data akun ke file JSON.
        """

        ACCOUNT_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(ACCOUNT_FILE, "w", encoding="utf-8") as file:
            json.dump(
                self.accounts,
                file,
                indent=4,
                ensure_ascii=False
            )

    def register(self, nama, username, password):
        """
        Mendaftarkan akun pasien baru.
        """

        nama = nama.strip()
        username = username.strip()

        if not nama or not username or not password:
            raise ValueError("Semua data wajib diisi.")

        if len(username) < 4:
            raise ValueError("Username minimal 4 karakter.")

        if len(password) < 6:
            raise ValueError("Password minimal 6 karakter.")

        # Memeriksa apakah username sudah digunakan
        for akun in self.accounts:
            if akun["username"].lower() == username.lower():
                raise ValueError("Username sudah digunakan.")

        # Membuat akun pasien baru
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
        """
        Memeriksa username dan password pengguna.
        """

        for akun in self.accounts:

            if (
                akun["username"].lower() == username.strip().lower()
                and akun["password"] == password
            ):
                return akun

        return None
