class Pembayaran:
    def __init__(self, sewa, jumlah, tanggal_bayar):
        self.sewa = sewa
        self.jumlah = jumlah
        self.tanggal_bayar = tanggal_bayar

    def catat_pembayaran(self):
        status = "Lunas" if self.cek_lunas() else "Belum Lunas"
        print(f"-> Hasil: Pembayaran Rp{self.jumlah:,} pada {self.tanggal_bayar} berhasil dicatat | Status: {status}")

    def cek_lunas(self):
        return self.jumlah >= self.sewa.hitung_total()
