from database import ambil_info_sistem
from utils import bersihkan_layar, validasi_pilihan_menu
from auth import menu_login, menu_register
from features import tambah_akun, lihat_akun, update_password, hapus_akun, hitung_total_akun

def tampilkan_menu_awal():
    bersihkan_layar()
    print("===========================")
    print("   ACCOUNT MANAGER - LOGIN   ")
    print("===========================")
    print("1. Login")
    print("2. Register (jika belum mempunyai akun)")
    print("3. Keluar program")
    print("===========================")
    print("")

def main():
    while True:
        tampilkan_menu_awal()
        
        pilihan_awal_angka = validasi_pilihan_menu(3)
        if pilihan_awal_angka is None:
            continue
        
        pilihan_awal = str(pilihan_awal_angka)

        if pilihan_awal == "1":
            logged_in_user, logged_in_role = menu_login()
            if logged_in_user is not None:
                while True:
                    bersihkan_layar()
                    print("===========================")
                    print(" ACCOUNT MANAGER - MAIN MENU ")
                    print("===========================")
                    print(f"Pengguna Aktif : {logged_in_user} | Info: {ambil_info_sistem()}")
                    print("===========================")

                    if logged_in_role == "admin":
                        print("1. Tambah Akun Baru (Create)")
                        print("2. Lihat Semua Akun (Read)")
                        print("3. Perbarui Password Akun (Update)")
                        print("4. Hapus Akun (Delete)")
                        print("5. Hitung Total Akun (Rekursif)")
                        print("6. Logout")
                        batas_maks_menu = 6
                    else:
                        print("1. Lihat Semua Akun (Read - Akses Terbatas)")
                        print("2. Logout")
                        batas_maks_menu = 2
                    
                    print("===========================")

                    pilihan_menu_angka = validasi_pilihan_menu(batas_maks_menu)
                    if pilihan_menu_angka is None:
                        continue
                    
                    pilihan_menu = str(pilihan_menu_angka)

                    if logged_in_role == "admin":
                        if pilihan_menu == "1":
                            tambah_akun()
                        elif pilihan_menu == "2":
                            lihat_akun("admin")
                        elif pilihan_menu == "3":
                            update_password()
                        elif pilihan_menu == "4":
                            hapus_akun()
                        elif pilihan_menu == "5":
                            hitung_total_akun()
                        elif pilihan_menu == "6":
                            print("\nBerhasil logout dari sistem.")
                            input("Tekan Enter untuk kembali ke halaman utama.")
                            break
                    else:
                        if pilihan_menu == "1":
                            lihat_akun("user")
                        elif pilihan_menu == "2":
                            print("\nBerhasil logout dari sistem.")
                            input("Tekan Enter untuk kembali ke halaman utama.")
                            break

        elif pilihan_awal == "2":
            menu_register()

        elif pilihan_awal == "3":
            print("\nTerima Kasih sudah menggunakan program ini!")
            break

if __name__ == "__main__":
    main()