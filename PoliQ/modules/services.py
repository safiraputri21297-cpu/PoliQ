
"""
services.py
Modul untuk mengelola proses antrean pasien PoliQ.
"""

from datetime import datetime
from uuid import uuid4

from modules.storage import load_data, save_data
from modules.validation import validate_patient, validate_status


class QueueManager:
    """
    Class untuk mengelola data dan proses antrean pasien.
    """

    def __init__(self):
        # Mengambil data pasien dari file JSON
        self.patients = load_data()

    def refresh_data(self):
        """Memuat ulang data pasien."""
        self.patients = load_data()
        return self.patients

    def save(self):
        """Menyimpan data pasien ke JSON."""
        save_data(self.patients)

    def get_patients(self):
        """Mengambil seluruh data pasien."""
        return self.patients

    def add_patient(self, nama, keluhan):
        """
        Mendaftarkan pasien baru dan memberikan
        nomor antrean secara otomatis.
        """

        # Memeriksa input pasien
        nama, keluhan = validate_patient(nama, keluhan)

        sekarang = datetime.now()
        tanggal = sekarang.strftime("%Y-%m-%d")
        waktu = sekarang.strftime("%H:%M:%S")

        # Mengambil jumlah antrean pada hari ini
        antrean_hari_ini = [
            pasien for pasien in self.patients
            if pasien["tanggal"] == tanggal
        ]

        # Membuat nomor antrean otomatis
        nomor = len(antrean_hari_ini) + 1
        nomor_antrian = f"A{nomor:03d}"

        # Membuat data pasien baru
        pasien_baru = {
            "id": str(uuid4()),
            "nomor_antrian": nomor_antrian,
            "tanggal": tanggal,
            "waktu_daftar": waktu,
            "nama": nama,
            "keluhan": keluhan,
            "status": "Menunggu",
            "waktu_mulai": "",
            "waktu_selesai": "",
            "durasi": 0
        }

        # Menambahkan pasien ke dalam daftar
        self.patients.append(pasien_baru)

        # Menyimpan perubahan ke JSON
        self.save()

        return pasien_baru

    def call_next(self):
        """
        Memanggil pasien berikutnya berdasarkan
        urutan nomor antrean.
        """

        waiting = [
            pasien for pasien in self.patients
            if pasien["tanggal"] == datetime.now().strftime("%Y-%m-%d")
            and pasien["status"] == "Menunggu"
        ]

        if not waiting:
            return None

        # Mengurutkan antrean berdasarkan nomor
        waiting.sort(
            key=lambda pasien: int(pasien["nomor_antrian"][1:])
        )

        pasien = waiting[0]
        pasien["status"] = "Dipanggil"

        self.save()

        return pasien

    def update_status(self, patient_id, status):
        """
        Mengubah status pelayanan pasien.
        """

        validate_status(status)

        for pasien in self.patients:

            if pasien["id"] == patient_id:

                sekarang = datetime.now()

                if status == "Sedang Dilayani":
                    pasien["waktu_mulai"] = sekarang.strftime(
                        "%H:%M:%S"
                    )

                elif status == "Selesai":
                    pasien["waktu_selesai"] = sekarang.strftime(
                        "%H:%M:%S"
                    )

                    # Menghitung lama pelayanan pasien
                    if pasien["waktu_mulai"]:
                        mulai = datetime.strptime(
                            pasien["waktu_mulai"], "%H:%M:%S"
                        )

                        selesai = datetime.strptime(
                            pasien["waktu_selesai"], "%H:%M:%S"
                        )

                        durasi = (selesai - mulai).total_seconds() / 60

                        if durasi < 0:
                            durasi += 1440

                        pasien["durasi"] = round(durasi, 2)

                pasien["status"] = status

                self.save()
                return pasien

        raise ValueError("Data pasien tidak ditemukan.")

    def average_duration(self, *durasi):
        """
        Menghitung rata-rata durasi pelayanan.
        Menggunakan *args.
        """

        if not durasi:
            return 10

        return sum(durasi) / len(durasi)

    def filter_patients(self, **kriteria):
        """
        Menyaring pasien berdasarkan kriteria.
        Menggunakan **kwargs.
        """

        hasil = self.patients

        for kolom, nilai in kriteria.items():
            hasil = [
                pasien for pasien in hasil
                if pasien.get(kolom) == nilai
            ]

        return hasil
