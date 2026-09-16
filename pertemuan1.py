print("Ini mau saya push")

#numerik

angka1 = 5
angka2 = 10
hasil = angka1 + angka2
print(hasil)

#float
a = 3.45
b = 1.23
hitung = a + b
print(hitung)

#string
nama = "Fazri"
hobi = "ngoding"
print(nama)
print(hobi)

print('''Halo saya fazri saya suka belajar ngoding Hari ini saya belajar bahasa pemrograman python''')

print("aku""rajin""praktikum")
print("aku"+"rajin")


teks = "Rahmat Flowchart"
print(teks[3])
print(teks[3:6])
print(teks[7:])
print(teks[:6])
print(teks[1:4:2])

#boolean
Hujan = False
Panas = True

#tipe data kolektif
#list 

biodata = ["Fazri", 18, "2026", 82.49, True, ["APD", "26"]]
print(biodata)

mata_kuliah = ["APD","Logika Matematika", "Kalkulus"]
print(mata_kuliah[0])
print(mata_kuliah[1])
print(mata_kuliah[2])
print(mata_kuliah[0:1])
print(mata_kuliah[:2])
print(mata_kuliah[1:])
print(mata_kuliah[::2])

#set
angka = {1, 2, 3, 4, 4, 5}
print(angka)

#dictionary
buku = {
'judul' : 'Atomic habits',
'penulis' : 'James Clear',
'halaman' : 320
}

#mengakses value dalam dictionary
print(buku['judul'])
print(buku['penulis'])
print(buku['halaman'])

#input
nama = input("Masukkan nama anda : ")
print(nama) 

gaji = int(input("Masukkan gaji anda : "))
print(gaji)

print(2 < 4)
print(5 > 5)
print(2 < 4 and 5 > 10)

zidan = {
    'pagi' : 'Kalkulus',
    'siang' : 'Algoritma Pemrograman Dasar',
    'sore' : 'Bahasa Inggris'
}
print(zidan['siang'])