# kamar.py

class Kamar:
    def __init__(self, nomor_kamar, tipe, harga_per_bulan):
        self.nomor_kamar = nomor_kamar
        self.tipe = tipe
        self.__status = "tersedia"
        self.harga_per_bulan = harga_per_bulan 

    @property
    def harga_per_bulan(self):
        return self.__harga_per_bulan

    @harga_per_bulan.setter
    def harga_per_bulan(self, harga):
        if harga <= 0:
            raise ValueError("Harga kamar harus lebih dari 0!")
        self.__harga_per_bulan = harga

    @property
    def status(self):
        return self.__status

    def tersedia(self):
        return self.__status == "tersedia"

    def sewakan(self):
        self.__status = "disewa"

    def kosongkan(self):
        self.__status = "tersedia"

    def info(self):
        return f"Kamar {self.nomor_kamar} ({self.tipe}) - Rp{self.__harga_per_bulan:,}/bln | Status: {self.__status}"