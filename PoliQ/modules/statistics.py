
"""
statistics.py
Modul untuk menghitung statistik antrean pasien PoliQ.
"""


def hitung_statistik(data):
    """
    Menghitung jumlah pasien berdasarkan status antrean.
    """

    total = len(data)

    menunggu = 0
    dipanggil = 0
    dilayani = 0
    selesai = 0
    tidak_hadir = 0
    terlewat = 0

    # Memeriksa status setiap pasien
    for pasien in data:

        if pasien["status"] == "Menunggu":
            menunggu += 1

        elif pasien["status"] == "Dipanggil":
            dipanggil += 1

        elif pasien["status"] == "Sedang Dilayani":
            dilayani += 1

        elif pasien["status"] == "Selesai":
            selesai += 1

        elif pasien["status"] == "Tidak Hadir":
            tidak_hadir += 1

        elif pasien["status"] == "Terlewat":
            terlewat += 1

    # Mengumpulkan hasil statistik
    statistik = {
        "total": total,
        "menunggu": menunggu,
        "dipanggil": dipanggil,
        "dilayani": dilayani,
        "selesai": selesai,
        "tidak_hadir": tidak_hadir,
        "terlewat": terlewat
    }

    return statistik


def hitung_rata_rata_durasi(data):
    """
    Menghitung rata-rata lama pelayanan pasien
    yang sudah selesai.
    """

    total_durasi = 0
    jumlah_pasien = 0

    for pasien in data:

        if pasien["status"] == "Selesai":
            total_durasi += pasien["durasi"]
            jumlah_pasien += 1

    # Menghindari pembagian dengan nol
    if jumlah_pasien == 0:
        return 0

    rata_rata = total_durasi / jumlah_pasien

    return round(rata_rata, 2)


def format_waktu(menit):
    """
    Mengubah satuan menit menjadi jam dan menit.
    """

    jam = int(menit // 60)
    sisa_menit = int(menit % 60)

    if jam > 0:
        return f"{jam} jam {sisa_menit} menit"

    return f"{sisa_menit} menit"


def estimasi_waktu_tunggu(jumlah_pasien, rata_rata_durasi=10):
    """
    Memperkirakan waktu tunggu pasien berdasarkan
    jumlah pasien di depannya.
    """

    total_menit = jumlah_pasien * rata_rata_durasi

    return format_waktu(total_menit)
