
"""
main.py
Program utama untuk menjalankan aplikasi PoliQ.
"""

import tkinter as tk
from tkinter import messagebox

from modules.ui import QueueApp


def main():
    """Menjalankan aplikasi PoliQ."""

    try:
        root = tk.Tk()
        app = QueueApp(root)
        root.mainloop()

    except (OSError, ValueError) as error:
        messagebox.showerror("Kesalahan Aplikasi", str(error))


if __name__ == "__main__":
    main()
