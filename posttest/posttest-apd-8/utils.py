import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cetak_garis():
    print("==================================================")

def validasi_pilihan_menu(max_pilihan):
    try:
        input_str = input(f"Pilih menu: (1-{max_pilihan}): ").strip()
        pilihan_angka = int(input_str)
        if 1 <= pilihan_angka <= max_pilihan:
            return pilihan_angka
        else:
            print("\nPilihan menu tidak tersedia!")
            input("Tekan Enter untuk mencoba lagi.")
            return None
    except ValueError:
        print("\nError: Input harus berupa angka!")
        input("Tekan Enter untuk mencoba lagi.")
        return None