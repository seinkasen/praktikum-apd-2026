from prettytable import PrettyTable
from database import data_akun, hitung_total_akun_rekursif
from utils import bersihkan_layar

def tambah_akun():
    bersihkan_layar()
    print("===========================")
    print("    TAMBAH AKUN BARU       ")
    print("===========================")
    app = input("Nama Aplikasi / Web : ").strip()
    uname = input("Username / Email    : ").strip()
    pwd = input("Password            : ").strip()

    if app != "" and uname != "" and pwd != "":
        if app in data_akun:
            print(f"\nAkun untuk '{app}' sudah ada! Gunakan menu Update jika ingin mengubah.")
        else:
            data_akun[app] = {"username": uname, "password": pwd}
            print(f"\nKredensial untuk '{app}' berhasil ditambahkan!")
    else:
        print("\nMohon mengisi semua data!")
    input("Tekan Enter untuk kembali.")

def lihat_akun(role):
    bersihkan_layar()
    print("===========================")
    print("        LIST AKUN          ")
    print("===========================")
    if len(data_akun) == 0:
        print("Belum ada data akun yang tersimpan di database.")
    else:
        table = PrettyTable()
        if role == "admin":
            table.field_names = ["No.", "Aplikasi / Web", "Username / Email", "Password"]
            index = 1
            for app, detail in data_akun.items():
                table.add_row([index, app, detail['username'], detail['password']])
                index += 1
        else:
            table.field_names = ["No.", "Aplikasi / Web", "Username / Email"]
            index = 1
            for app, detail in data_akun.items():
                table.add_row([index, app, detail['username']])
                index += 1
        print(table)
    input("\nTekan Enter untuk kembali.")

def update_password():
    bersihkan_layar()
    print("===========================")
    print("   UPDATE PASSWORD AKUN    ")
    print("===========================")
    if len(data_akun) == 0:
        print("Belum ada data akun yang tersimpan di database.")
    else:
        table = PrettyTable()
        table.field_names = ["No.", "Aplikasi / Web", "Username / Email"]
        list_keys = list(data_akun.keys())
        idx = 1
        for key in list_keys:
            table.add_row([idx, key, data_akun[key]['username']])
            idx += 1
        print(table)

        input_no = input("Masukkan Nomor Akun yang ingin diubah password-nya: ").strip()

        if input_no.isdigit():
            no_index = int(input_no) - 1
            if 0 <= no_index < len(list_keys):
                key_pilihan = list_keys[no_index]
                pass_baru = input(f"Masukkan Password Baru untuk '{key_pilihan}': ").strip()
                if pass_baru != "":
                    data_akun[key_pilihan]["password"] = pass_baru
                    print("\nPassword berhasil diperbarui!")
                else:
                    print("\nPassword baru tidak boleh kosong!")
            else:
                print("\nNomor akun tidak ditemukan!")
        else:
            print("\nInput harus berupa angka nomor akun!")
    input("\nTekan Enter untuk kembali.")

def hapus_akun():
    bersihkan_layar()
    print("===========================")
    print("        DELETE AKUN        ")
    print("===========================")
    if len(data_akun) == 0:
        print("Belum ada data akun yang tersimpan di database.")
    else:
        table = PrettyTable()
        table.field_names = ["No.", "Aplikasi / Web", "Username / Email"]
        list_keys = list(data_akun.keys())
        idx = 1
        for key in list_keys:
            table.add_row([idx, key, data_akun[key]['username']])
            idx += 1
        print(table)

        input_no = input("Masukkan Nomor Akun yang ingin dihapus: ").strip()

        if input_no.isdigit():
            no_index = int(input_no) - 1
            if 0 <= no_index < len(list_keys):
                key_pilihan = list_keys[no_index]
                akun_terhapus = data_akun.pop(key_pilihan)
                print(f"\nAkun '{key_pilihan}' ({akun_terhapus['username']}) berhasil dihapus!")
            else:
                print("\nNomor akun tidak ditemukan!")
        else:
            print("\nInput harus berupa angka nomor akun!")
    input("\nTekan Enter untuk kembali.")

def hitung_total_akun():
    bersihkan_layar()
    print("===========================")
    print("   TOTAL AKUN (REKURSIF)   ")
    print("===========================")
    total_hasil = hitung_total_akun_rekursif(list(data_akun.keys()))
    print(f"Total akun tersimpan di database: {total_hasil} buah")
    print("===========================")
    input("\nTekan Enter untuk kembali.")