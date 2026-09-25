import sys

#DATA DIRI
NAMA = "Fazri"
NIM = "44"

#LANGGANAN
BIAYA_LANGGANAN = 1500000

#VALIDASI LOGIN
print("[ ANGKASA MUSIC STREAMING SERVICE ]")
print("[        You are the star         ]")

nama_input = input("Masukkan nama : ")
nim_input = input("Masukkan NIM (2 digit terakhir) : ")

if nama_input != NAMA or nim_input != NIM:
    print("Gagal Login: Mohon cek kembali nama atau NIM anda.")
    sys.exit()

print(" ")
print("Login Berhasil!")
print(" ")

#MENU PAKET
print("[ Pilihan Paket Langganan ]")
print("Biaya Awal: Rp", (BIAYA_LANGGANAN))
print("Paket Orbit:     (Admin 1%) akses dasar ke lagu-lagu populer")
print("Paket Nebula:    (Admin 3%, akses lagu premium dan playlist kustom")
print("Paket Galaxy:    (Admin 5%), akses lagu premium, playlist kustom, dan mode offline")
print("Paket Supernova: (Admin 7%), akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
print(" ")

pilihan = input("Pilih paket langganan (1/2/3/4): ")

#PAKET & FITUR
if pilihan == "1":
    nama_paket = "Orbit"
    persen_admin = 0.01
    fitur = "Akses dasar ke lagu-lagu populer"
elif pilihan == "2":
    nama_paket = "Nebula"
    persen_admin = 0.03
    fitur = "Akses lagu premium dan playlist custom"
elif pilihan == "3":
    nama_paket = "Galaxy"
    persen_admin = 0.05
    fitur = "Akses lagu premium, playlist kustom, dan mode offline"
elif pilihan == "4":
    nama_paket = "Supernova"
    persen_admin = 0.07
    fitur = "Akses lagu premium, playlist kustom, dan mode offline, dan konten eksklusif artis"
else:
    print("Pilihan paket tidak valid! silahkan dicek kembali")
    sys.exit()

biaya_admin = int(BIAYA_LANGGANAN) * (persen_admin)
total_bayar = int(BIAYA_LANGGANAN) + (biaya_admin)

print(" ")

#HASIL AKHIR
print("=" * 45)
print("[ STRUK PEMBAYARAN ANGKASA ]")
print(" ")
print(f"Nama Pengguna   : {nama_input}")
print(f"Paket Dipilih   : Paket {nama_paket}")
print(" ")
print(f"Biaya langganan  : Rp {BIAYA_LANGGANAN:,.0f}".replace(",", "."))
print(f"Biaya admin      : Rp {biaya_admin:,.0f}".replace(",", "."))
print(" ")
print(f"TOTAL BAYAR      : Rp {total_bayar:,.0f}".replace(",", "."))
print(" ")
print("Fitur Paket:")
print(f"{fitur}")
print(" ")
print("[ Terima kasih telah berlangganan di ANGKASA! ]")
print("=" * 45)