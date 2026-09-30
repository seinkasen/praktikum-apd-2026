#---
#PENGULANGAN FOR (Counted Loop)

#1
#batas = 5
#for i in range(batas):
#   print("Perulangan ke-", i)

#2
#game = ["Genshin", 7.0, True]
#for i in game:
#print(i)

#3
#for i in range(1, 11, 1):
#    print(i)

#Struktur range pada for
#range(start, stop, step):

#4 Nested for
#for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#        print(f'{i} x {j} = {i * j}')
#    print('') #biar ada jarak tiap iterasi
#---

#---
#PENGULANGAN WHILE 

#Contoh 1
#jawab = "ya"
#itung = 0

#while(jawab == "ya"):
#    hitung += 1
#    jawab = input("Ulang lagi tidak? ")

#print(f"Total Perulangan : {hitung}")
#---

#---
#Kontrol Pengulangan

#Break

#1
#or i in range(10):
#   if i == 5:
#        break
#    print(i)

#2
#for i in range(20):
#    if i > 12:
#        break
#    print("perulangan ke: ", i)

#3
#angka_benar = 7 

#while True:
#    print("===Game tebak angka===")

#    angka_input = int(input("Masukkan angka (1-10): "))

#    if angka_benar == angka_input:
#        print("Angka yang kamu masukkan benar")
#        break
#    else:
#        print("Angka masih salah")

#Variasi lain untuk jika user menulis string "tujuh" instead of angka "7"
#while True:
#    print("===Game tebak angka===")

#    angka_input = (input("Masukkan angka (1-10): "))

#    if not angka_input.isdigit(): # "abc12" 
#        continue

#        print("Angka yang kamu masukkan benar")
#        break
#    else:
#        print("Angka masih salah")

#Continue
#1
#for i in range(10):
#    if i % 2 == 0:
#        continue
#    print(i)
#---

#Studi Kasus

n = int(input("Masukkan nilai n: "))
jumlah = 0
for i in range(1, n+1):
    if i % 2 != 0:
        jumlah += 1
print (f"Jumlah ganjil: {jumlah}")