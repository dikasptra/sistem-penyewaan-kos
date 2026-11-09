from kamar import Kamar

daftar_kamar = [
    Kamar("101", "Reguler", 750_000),
    Kamar("102", "VIP AC", 1_200_000)
]

print("DAFTAR KAMAR KOS :")
for k in daftar_kamar:
    print(k.info())

print("\n CEK KETERSEDIAAN KAMAR :")
cari_nomor = input("Masukkan nomor kamar: ")

kamar_ditemukan = None
for k in daftar_kamar:
    if k.nomor_kamar == cari_nomor:
        kamar_ditemukan = k
        break

if kamar_ditemukan:
    if kamar_ditemukan.tersedia():
        print(f"-> Hasil: Kamar {kamar_ditemukan.nomor_kamar} ({kamar_ditemukan.tipe}) masih tersedia.")
    else:
        print(f"-> Hasil: Maaf, Kamar {kamar_ditemukan.nomor_kamar} tidak tersedia.")
else:
    print(f"-> Hasil: Kamar dengan nomor '{cari_nomor}' tidak ditemukan.")