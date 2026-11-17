# sewa.py

class Sewa:
    def __init__(self, penyewa, kamar, tanggal_mulai, durasi_bulan):
        self.__penyewa = penyewa
        self.__kamar = kamar
        self.__tanggal_mulai = tanggal_mulai
        self.__durasi_bulan = durasi_bulan
        self.__aktif = False

    @property
    def penyewa(self):
        return self.__penyewa

    @property
    def kamar(self):
        return self.__kamar

    def proses_sewa(self):
        # Validasi F06: Tolak jika kamar tidak tersedia
        if not self.__kamar.tersedia():
            print(f"[DITOLAK] Kamar {self.__kamar.nomor_kamar} sedang disewa! "
                  f"Penyewa {self.__penyewa.nama} tidak bisa menyewa kamar ini.")
            return False

        # Proses F03: Ubah status kamar menjadi disewa
        self.__kamar.sewakan()
        self.__aktif = True
        print(f"[BERHASIL] {self.__penyewa.nama} menyewa Kamar {self.__kamar.nomor_kamar} "
              f"selama {self.__durasi_bulan} bulan (Mulai: {self.__tanggal_mulai}).")
        print(f"Total Biaya Sewa: Rp{self.hitung_total():,}")
        return True

    def hitung_total(self):
        return self.__kamar.harga_per_bulan * self.__durasi_bulan

    def proses_pengakhiran(self):
        # Proses F05: Pengakhiran sewa & kembalikan status kamar
        if self.__aktif:
            self.__kamar.kosongkan()
            self.__aktif = False
            print(f"[CHECK-OUT] {self.__penyewa.nama} telah mengakhiri sewa "
                  f"Kamar {self.__kamar.nomor_kamar}. Status kamar kembali tersedia.")
        else:
            print("Info: Transaksi sewa ini sudah tidak aktif.")