from database import users
from utils import bersihkan_layar

def menu_login():
    bersihkan_layar()
    print("===========================")
    print("         LOGIN           ")
    print("===========================")
    input_user = input("Username : ").strip()
    input_pass = input("Password : ").strip()

    if input_user in users and users[input_user]["password"] == input_pass:
        role = users[input_user]["role"]
        print(f"\nLogin berhasil! Selamat datang {input_user}! Role kamu '{role.upper()}' ya!")
        input("Tekan Enter untuk melanjutkan.")
        return input_user, role
    else:
        print("\nUsername atau password salah!")
        input("Tekan Enter untuk mencoba lagi.")
        return None, None

def menu_register():
    bersihkan_layar()
    print("===========================")
    print("     REGISTER PENGGUNA     ")
    print("===========================")
    reg_user = input("Masukkan Username Baru: ").strip()
    reg_pass = input("Masukkan Password Baru: ").strip()

    if reg_user != "" and reg_pass != "":
        if reg_user in users:
            print("\nUsername sudah terdaftar! Mohon gunakan username lain ^^.")
        else:
            users[reg_user] = {"password": reg_pass, "role": "user"}
            print(f"\nRegistrasi berhasil! Akun '{reg_user}' telah dibuat.")
    else:
        print("\nUsername dan password tidak boleh kosong!")

    input("Tekan Enter untuk kembali ke menu utama.")