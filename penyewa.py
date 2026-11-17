# penyewa.py
from sewa import Sewa

class Penyewa:
    def __init__(self, id_penyewa, nama, no_telepon):
        self.__id_penyewa = id_penyewa
        self.__nama = nama
        self.__no_telepon = no_telepon

    @property
    def id_penyewa(self):
        return self.__id_penyewa

    @property
    def nama(self):
        return self.__nama

    @property
    def no_telepon(self):
        return self.__no_telepon

    def sewa_kamar(self, kamar, tanggal_mulai, durasi_bulan):
        sewa_baru = Sewa(self, kamar, tanggal_mulai, durasi_bulan)
        if sewa_baru.proses_sewa():
            return sewa_baru
        return None

    def akhiri_sewa(self, sewa):
        sewa.proses_pengakhiran()

    def info(self):
        return f"[{self.__id_penyewa}] {self.__nama} (Telp: {self.__no_telepon})"