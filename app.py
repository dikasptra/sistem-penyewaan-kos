from flask import Flask, render_template, request, redirect, url_for
from kamar import Kamar
from penyewa import Penyewa
from sewa import Sewa
from pembayaran import Pembayaran

app = Flask(__name__)

# Data awal kamar kos (F01)
daftar_kamar = [
    Kamar("101", "Reguler", 750_000),
    Kamar("102", "VIP AC", 1_200_000),
    Kamar("103", "Reguler", 750_000)
]
# Kamar 103 diset sudah disewa untuk menguji validasi penolakan (F06)
daftar_kamar[2].sewakan()

daftar_sewa = []
daftar_pembayaran = []
pesan_hasil = ""


@app.route("/")
def index():
    return render_template(
        "index.html",
        daftar_kamar=daftar_kamar,
        daftar_sewa=daftar_sewa,
        daftar_pembayaran=daftar_pembayaran,
        pesan=pesan_hasil
    )


@app.route("/sewa", methods=["POST"])
def sewa_kamar():
    global pesan_hasil
    id_penyewa = request.form["id_penyewa"]
    nama = request.form["nama"]
    no_telepon = request.form["no_telepon"]
    nomor_kamar = request.form["nomor_kamar"]
    tanggal_mulai = request.form["tanggal_mulai"]
    durasi_bulan = int(request.form["durasi_bulan"])

    kamar_ditemukan = None
    for k in daftar_kamar:
        if k.nomor_kamar == nomor_kamar:
            kamar_ditemukan = k
            break

    if not kamar_ditemukan:
        pesan_hasil = f"Gagal: Kamar {nomor_kamar} tidak ditemukan."
        return redirect(url_for("index"))

    # Buat objek Penyewa (F02) dan Sewa (F03)
    penyewa_baru = Penyewa(id_penyewa, nama, no_telepon)
    penyewa_baru.sewa_kamar(kamar_ditemukan)
    sewa_baru = Sewa(penyewa_baru, kamar_ditemukan, tanggal_mulai, durasi_bulan)

    # Cek validasi ketersediaan kamar (F06)
    if sewa_baru.proses_sewa():
        daftar_sewa.append(sewa_baru)
        pesan_hasil = f"Berhasil: {nama} menyewa Kamar {nomor_kamar}. Total: Rp{sewa_baru.hitung_total():,}"
    else:
        pesan_hasil = f"Ditolak (F06): Maaf, Kamar {nomor_kamar} sedang disewa!"

    return redirect(url_for("index"))


@app.route("/bayar", methods=["POST"])
def bayar_sewa():
    global pesan_hasil
    index_sewa = int(request.form["index_sewa"])
    jumlah = int(request.form["jumlah"])
    tanggal_bayar = request.form["tanggal_bayar"]

    sewa_dipilih = daftar_sewa[index_sewa]
    pembayaran_baru = Pembayaran(sewa_dipilih, jumlah, tanggal_bayar)
    pembayaran_baru.catat_pembayaran()
    daftar_pembayaran.append(pembayaran_baru)

    status = "Lunas" if pembayaran_baru.cek_lunas() else "Belum Lunas"
    pesan_hasil = f"Pembayaran {sewa_dipilih.penyewa.nama} sebesar Rp{jumlah:,} dicatat ({status})."
    return redirect(url_for("index"))


@app.route("/checkout/<int:index_sewa>", methods=["POST"])
def checkout(index_sewa):
    global pesan_hasil
    sewa_dipilih = daftar_sewa[index_sewa]
    sewa_dipilih.penyewa.akhiri_sewa(sewa_dipilih)
    pesan_hasil = f"Check-out berhasil: Kamar {sewa_dipilih.kamar.nomor_kamar} kembali tersedia."
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)