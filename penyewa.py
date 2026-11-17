# penyewa.py

class Penyewa:
    def __init__(self, id_penyewa, nama, no_telepon):
        self.id_penyewa = id_penyewa
        self.nama = nama
        self.no_telepon = no_telepon
        self.sewa_aktif = None

    def sewa_kamar(self, sewa):
        """Menghubungkan penyewa dengan transaksi sewa yang aktif."""
        if self.sewa_aktif is not None:
            raise ValueError("Penyewa masih memiliki sewa yang aktif!")

        if sewa.penyewa is not self:
            raise ValueError("Data penyewa pada transaksi sewa tidak sesuai!")

        sewa.proses_sewa()
        self.sewa_aktif = sewa
        return sewa

    def akhiri_sewa(self):
        """Mengakhiri sewa aktif milik penyewa."""
        if self.sewa_aktif is None:
            raise ValueError("Penyewa tidak memiliki sewa aktif!")

        self.sewa_aktif.proses_pengakhiran()
        self.sewa_aktif = None

    def info(self):
        return (
            f"ID Penyewa: {self.id_penyewa} | Nama: {self.nama} | "
            f"No. Telepon: {self.no_telepon}"
        )
