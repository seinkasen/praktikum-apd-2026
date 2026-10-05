USERNAME_BENAR = "FAZRI"
PASSWORD_BENAR = "044"

total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0

print("======================================")
print("SISTEM REKAPITULASI TITIK API KARHUTLA")
print("======================================")

login_berhasil = False
while not login_berhasil :
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if username == "" or password == "":
        print("Username atau password tidak boleh kosong!")
        continue

    if username.upper() == USERNAME_BENAR.upper() and password == PASSWORD_BENAR:
        print("Login berhasil!")
        login_berhasil = True
        print("")
    elif username.upper() != USERNAME_BENAR.upper() and password == PASSWORD_BENAR:
        print("Username salah! silahkan cek kembali")
        login_berhasil = False
    elif username.upper() == USERNAME_BENAR.upper() and password != PASSWORD_BENAR:
        print("Password salah! silahkan cek kembali")
        login_berhasil = False
    else:
        print("Username dan password salah! silahkan cek kembali")
        login_berhasil = False

ulang_input = "Y"
while ulang_input.upper() == "Y":
    print("=====================================")
    print("INPUT SEBARAN DATA TITIK API KARHUTLA")
    print("=====================================")

    pulau = ""
    while True:
        pulau = input("Masukkan nama pulau (Kalimantan/Sumatera): ").strip().upper()
        if pulau == "":
            print("Nama pulau tidak boleh kosong!")
        elif pulau in ["KALIMANTAN", "SUMATERA"]:
            break
        else:
            print("Nama pulau invalid! Silahkan masukkan 'Kalimantan' atau 'Sumatera'.")

    if pulau == "KALIMANTAN":
        while True:
            lahan = input("Masukkan jenis lahan di Kalimantan (Gambut/Mineral): ").strip().upper()
            if lahan == "":
                print("Jenis lahan tidak boleh kosong!")
            elif lahan in ["GAMBUT", "MINERAL"]:
                break
            else:
                print("Jenis lahan invalid! Silahkan masukkan 'Gambut' atau 'Mineral'.")

    if pulau == "SUMATERA":
        while True:
            lahan = input("Masukkan jenis lahan di Sumatera (Gambut/Mineral): ").strip().upper()
            if lahan == "":
                print("Jenis lahan tidak boleh kosong!")
            elif lahan in ["GAMBUT", "MINERAL"]:
                break
            else:
                print("Jenis lahan invalid! Silahkan masukkan 'Gambut' atau 'Mineral'.")

    Jumlah_titik_api = 0
    while True:
        input_titikapi = input("Masukkan jumlah titik API: ").strip()
        if input_titikapi == "" or input_titikapi == 0:
            print("Jumlah titik API tidak boleh kosong!")
            continue

        if input_titikapi.isdigit():
            Jumlah_titik_api = int(input_titikapi)
            if Jumlah_titik_api > 0:
                break
            else:
                print("Jumlah titik API tidak boleh negatif!")
        else:
            print("Harap masukkan angka bulat yang valid.")

    luas_terbakar = Jumlah_titik_api * 5   
    print(f"Estimasi kerusakan lahan: {luas_terbakar} hektare")

    if pulau == "KALIMANTAN" and lahan == "GAMBUT":
        total_kalimantan_gambut += luas_terbakar
    elif pulau == "KALIMANTAN" and lahan == "MINERAL":
        total_kalimantan_mineral += luas_terbakar
    elif pulau == "SUMATERA" and lahan == "GAMBUT":
        total_sumatera_gambut += luas_terbakar
    elif pulau == "SUMATERA" and lahan == "MINERAL":
        total_sumatera_mineral += luas_terbakar

    while True:
        ulang_input = input("Apakah anda ingin memasukkan data lagi? (Ketik Y/T): ").strip().upper()
        if ulang_input == "":
            print("Input tidak boleh kosong! Silahkan ketik Y/T")
            continue
        if ulang_input.upper() in ["Y", "T"]:
            break
        else:
            print("Input tidak valid! Silahkan ketik Y/T")  

print("")
print("========================================")
print("RINGKASAN TOTAL ESTIMASI DAMAGE KARHUTLA")
print("========================================")
print(f"1. Kalimantan - Gambut : {total_kalimantan_gambut} Hektare")
print(f"2. Kalimantan - Mineral : {total_kalimantan_mineral} Hektare")
print(f"3. Sumatera - Gambut : {total_sumatera_gambut} Hektare")
print(f"4. Sumatera - Mineral : {total_sumatera_mineral} Hektare")
print("========================================")
total_all = (total_kalimantan_gambut + total_kalimantan_mineral + total_sumatera_gambut + total_sumatera_mineral)
print(f"Total estimasi damage keseluruhan : {total_all} Hektare")
print("========================================")
print("")
print("Program selesai.")
