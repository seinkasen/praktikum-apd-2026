# Built in Function & Python Library
# import math

# print(math.sqrt(100))
# print(math.factorial(5))

# from datetime import datetime
# print(datetime.now())

# import calendar as kalender
# print(kalender.calendar(2026))

# import random
# print(random.randint(1, 5))

# buah = ["pisang", "rambutan", "manggis"]
# huruf = "abcd"
# print(random.choice(buah))
# print(random.choice(huruf))

# kumpulan_angka = "0123456789"
# pin_acak = ""
# for i in range(4):
#     pin_acak += random.choice(kumpulan_angka)
# print(pin_acak)

# kartu = ["As Wajik", "3 Hati", "7 Sekop"]
# random.shuffle(kartu)
# print(kartu)

# from prettytable import PrettyTable

# tabel = PrettyTable()
# tabel.field_names = ["NIM", "Nama Mahasiswa", "Prodi"]

# tabel.add_row(["2609106001", "Andi Alarice", "Informatika"])

# tabel.add_rows([
#     ["2609106002", "Hammam Nopal", "Informatika"],
#     ["2609106003", "Abimar LLM", "Sistem Informasi"]
# ])

# tabel.align["Nama Mahasiswa"] = "l"
# print(tabel)

# import inquirer
# pertanyaan = [
#     inquirer.List(
#         "menu",
#         message="Pilih menu aplikasi",
#         choices=["Tambah Data", "Lihat Data", "Keluar"],
#     ),
# ]
# jawaban = inquirer.prompt(pertanyaan)
# print(jawaban) 
# print(jawaban["menu"]) 