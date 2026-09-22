#List harga makananan yang dibeli mbak Taylor
harga_makanan = [15000, 16000, 19000, 20000, 21000, 22000]

#Biaya tambahan dari aplikasi
biaya_aplikasi = 5000

#Variabel mata uang
kurs_eur = 17000

#Variable nim saya
nim = 44

#Menghitung total harga makanan tanpa menggunakan sum
makanan_1 = harga_makanan[0]
makanan_2 = harga_makanan[1]
makanan_3 = harga_makanan[2]
makanan_4 = harga_makanan[3]
makanan_5 = harga_makanan[4]
makanan_6 = harga_makanan[5]

total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + biaya_aplikasi

#Hitung rata rata harga
rata_rata = total_bayar / len(harga_makanan)

#Variabel bolean dengan nim !=rata_rata
bolean = nim != rata_rata   

#Konversi total bayar ke EUR
total_bayar_eur = total_bayar / kurs_eur

#Menampilkan hasil perhitungan
print("=== PESANAN MBA TAYLOR WARUNG Gizi Rendah ===")
print("Makanan 1                   : Rp", makanan_1)
print("Makanan 2                   : Rp", makanan_2)
print("Makanan 3                   : Rp", makanan_3)
print("Makanan 4                   : Rp", makanan_4)
print("Makanan 5                   : Rp", makanan_5)
print("Makanan 6                   : Rp", makanan_6)
print("Biaya tambahan dari Go-Cek  : Rp", biaya_aplikasi)
print("Total Bayar (IDR)           : Rp", total_bayar)
print("Total Bayar (EUR)           : €", round(total_bayar_eur, 2))
print("Rata-rata Harga             : Rp", round(rata_rata, 2))
print("NIM                         :", nim)
print("Boolean                     :", bolean)

#Slice Index Negatif
print("=== SLICE INDEX NEGATIF ===")
print("Makanan 1 sampai 6 (Index Negatif):", harga_makanan[-6:])