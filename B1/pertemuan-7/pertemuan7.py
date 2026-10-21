# Fungsi & Prosedur

#----------------------------------------------------------
# FUNGSI 

# Membuat Fungsi
# def nama_fungsi():
#     pernyataan
#     return hasil yang diinginkan


# Fungsi tanpa Parameter
# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas

# print("Luas persegi panjang:", luas_persegi_panjang())

# Fungsi dengan Parameter
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# print("Luas persegi:", luas_persegi(7))

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas

# def total_harga_tanah(panjang, lebar, harga = 100000):
#     total = luas_persegi_panjang(panjang, lebar) * harga
#     return total

# print("Luas persegi panjang:", luas_persegi_panjang(7, 4))
# print("Total harga tanah:", total_harga_tanah(7, 4))  

# Fungsi Rekursif
# def faktorial(n):
#     #Base Case: Kondisi fungsi berhenti
#     if n = 0 or n = 1:
#         return 1
#     #Rekursive Case: Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")
# #Output
# Hasil dari faktorial 4! adalah 24
#----------------------------------------------------------

#----------------------------------------------------------
# PROSEDUR

# Tanpa parameter
# def pengumuman():
#     print("Hari ini Pengujian Proyek Akhir")

# Pemanggilan Prosedur
# pengumuman()


# Dengan parameter
# def sapa_pengguna(nama_pengguna):
#     print(f"Halo, selamat datang {nama_pengguna}")

# Pemanggilan Prosedur
# sapa_pengguna("Citra")

#Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"

#Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

#Mengakses variabel lokal
# data()
#Mengakses variabel global
# print("Nama:", nama)
# print("Prodi:", prodi)
#Output
# Nama: Teknik Kedokteran
# Prodi: Kedokteran Lanjut
# Nama: Larry
# Prodi: Informatika
