users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"}
}

data_akun = {
    "MLBB": {"username": "Lebron_James", "password": "BronBronny"}
}

def ambil_info_sistem():
    return "Dictionary Aktif"

def hitung_total_akun_rekursif(daftar_kunci, index=0):
    if index >= len(daftar_kunci):
        return 0
    return 1 + hitung_total_akun_rekursif(daftar_kunci, index + 1)