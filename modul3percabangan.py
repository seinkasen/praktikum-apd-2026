#Percabangan if
angka = 6
if angka < 10: # Kondisi percabangan IF
    print("Angka kurang dari 10") 
#Tanda titik dua (:) wajib diletakkan pada akhir baris pengecekkan kondisi.

#Percabangan IF ELSE
umur = int(input("Masukkan umur: ")) # Input umur

#Misalkan, umur = 17

if umur >= 17:
    print("Kamu sudah bisa membuat KTP") # Blok IF dijalankan karena kondisi True
else:
    print("Kamu belum bisa membuat KTP") # Blok ELSE tidak dijalankan karena kondisi IF True

#Percabangan IF ELIF ELSE
kendaraan = input("Masukkan jenis kendaraan anda: ") 

#Misalnya, kendaraan = "mobil"
kendaraan = "mobil"

#Percabangan
if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000

print("Tarif parkir kendaraan anda adalah: ", tarif_parkir)


#Latsol
# Nilai lebih dari sama dengan 90 = A
# Nilai lebih dari sama dengan 80 = B
# Nilai lebih dari sama dengan 70 = C
# Nilai lebih dari 50 dan kurang dari 69 = D

nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 50 and nilai <= 69:
    print("Nilai D")
else:
    print("Nilai E")

#Bentuk Awal Percabangan IF/ELSE
umur = 20
if umur >= 18:
    status = "Dewasa"
else:
    status = "Belum Dewasa"

#Bentuk Ternary Operator (bentuk lain dari if else)
status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print(status)


#Tiket Masuk
umur = int(input("Masukkan umur: "))
status = " Boleh Masuk" if umur >= 16 else "Tidak Boleh Masuk"
print(status)


#Diskon
totalbeli = int(input("Total Pembelian: Rp"))

if totalbeli >200000:
    print("Diskon 30%")
elif totalbeli >100000:
    print("Diskon 10%")
elif totalbeli >100000 and totalbeli <100000:
    print("No Diskon")
else:
    print("-")

#if bercabang
Hujan = True
Mendung = False

if Hujan:
    print("Pake Jas Hujan")

    if Mendung:
        print("Bawa Payung")

else:
    print("Aman aja pok")