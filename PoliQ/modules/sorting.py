
"""
sorting.py
Modul untuk mengurutkan data pasien PoliQ.
Menggunakan algoritma Bubble Sort.
"""


def urutkan_pasien(data, kunci="nomor_antrian", descending=False):
    """
    Mengurutkan data pasien menggunakan Bubble Sort.

    kunci digunakan untuk menentukan bagian data
    yang akan diurutkan.

    descending=True untuk urutan terbesar ke terkecil.
    """

    # Membuat salinan data agar data asli tidak berubah
    hasil = data.copy()

    jumlah = len(hasil)

    # Proses pengurutan Bubble Sort
    for i in range(jumlah - 1):

        for j in range(jumlah - i - 1):

            nilai1 = hasil[j][kunci]
            nilai2 = hasil[j + 1][kunci]

            # Mengubah nomor antrean menjadi angka
            if kunci == "nomor_antrian":
                nilai1 = int(nilai1[1:])
                nilai2 = int(nilai2[1:])

            # Menentukan urutan pengurutan
            if descending:
                kondisi = nilai1 < nilai2
            else:
                kondisi = nilai1 > nilai2

            # Menukar posisi data jika urutannya salah
            if kondisi:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

    return hasil
