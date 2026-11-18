
"""
ui.py
Modul untuk membuat tampilan aplikasi PoliQ.
Menggunakan library Tkinter.
"""

import tkinter as tk
from tkinter import messagebox

from modules.authentication import Authentication


class QueueApp:
    """
    Class utama untuk mengatur tampilan aplikasi PoliQ.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("PoliQ - Sistem Antrean Pasien")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Membuat objek autentikasi
        self.auth = Authentication()

        # Menampilkan halaman login
        self.show_login()

    def clear_window(self):
        """Menghapus seluruh komponen pada jendela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        """Menampilkan halaman login."""

        self.clear_window()

        judul = tk.Label(
            self.root,
            text="POLIQ",
            font=("Arial", 26, "bold")
        )
        judul.pack(pady=20)

        keterangan = tk.Label(
            self.root,
            text="Sistem Manajemen Antrean Pasien Poli Umum",
            font=("Arial", 11)
        )
        keterangan.pack(pady=5)

        tk.Label(
            self.root,
            text="Username",
            font=("Arial", 11)
        ).pack(pady=(20, 5))

        self.username_entry = tk.Entry(
            self.root,
            font=("Arial", 12),
            width=30
        )
        self.username_entry.pack()

        tk.Label(
            self.root,
            text="Password",
            font=("Arial", 11)
        ).pack(pady=(15, 5))

        self.password_entry = tk.Entry(
            self.root,
            font=("Arial", 12),
            width=30,
            show="*"
        )
        self.password_entry.pack()

        tombol_login = tk.Button(
            self.root,
            text="Login",
            font=("Arial", 11, "bold"),
            width=20,
            command=self.login
        )
        tombol_login.pack(pady=20)

        tombol_daftar = tk.Button(
            self.root,
            text="Daftar Akun Pasien",
            font=("Arial", 10),
            command=self.show_register
        )
        tombol_daftar.pack()

    def login(self):
        """Memproses login pengguna."""

        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            akun = self.auth.login(username, password)

            if akun is None:
                messagebox.showerror(
                    "Login Gagal",
                    "Username atau password salah."
                )
                return

            if akun["role"] == "admin":
                self.show_admin(akun)

            else:
                self.show_patient(akun)

        except (OSError, ValueError) as error:
            messagebox.showerror("Kesalahan", str(error))

    def show_register(self):
        """Menampilkan halaman registrasi pasien."""

        self.clear_window()

        tk.Label(
            self.root,
            text="REGISTRASI PASIEN",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Label(self.root, text="Nama Lengkap").pack()
        self.nama_entry = tk.Entry(self.root, width=30)
        self.nama_entry.pack(pady=5)

        tk.Label(self.root, text="Username").pack()
        self.reg_username = tk.Entry(self.root, width=30)
        self.reg_username.pack(pady=5)

        tk.Label(self.root, text="Password").pack()
        self.reg_password = tk.Entry(
            self.root, width=30, show="*"
        )
        self.reg_password.pack(pady=5)

        tk.Button(
            self.root,
            text="Daftar",
            width=20,
            command=self.register
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="Kembali ke Login",
            command=self.show_login
        ).pack()

    def register(self):
        """Memproses pendaftaran akun pasien."""

        nama = self.nama_entry.get()
        username = self.reg_username.get()
        password = self.reg_password.get()

        try:
            self.auth.register(nama, username, password)

            messagebox.showinfo(
                "Berhasil",
                "Akun pasien berhasil dibuat."
            )

            self.show_login()

        except (ValueError, OSError) as error:
            messagebox.showerror("Registrasi Gagal", str(error))

    def show_admin(self, akun):
        """Menampilkan halaman utama admin."""

        self.clear_window()

        tk.Label(
            self.root,
            text="DASHBOARD ADMIN",
            font=("Arial", 22, "bold")
        ).pack(pady=30)

        tk.Label(
            self.root,
            text=f"Selamat datang, {akun['nama']}",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Logout",
            width=20,
            command=self.show_login
        ).pack(pady=20)

    def show_patient(self, akun):
        """Menampilkan halaman utama pasien."""

        self.clear_window()

        tk.Label(
            self.root,
            text="DASHBOARD PASIEN",
            font=("Arial", 22, "bold")
        ).pack(pady=30)

        tk.Label(
            self.root,
            text=f"Selamat datang, {akun['nama']}",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Logout",
            width=20,
            command=self.show_login
        ).pack(pady=20)
