#  Program Simulasi Login Sederhana
#  Dibuat oleh: Herdy Amar Fadlillah

USERNAME_BENAR = "admin"     # Username yang sah
PASSWORD_BENAR = "python"    # Password yang sah

maks_percobaan = 3           # Batas maksimum percobaan login
percobaan = 0                # Menghitung berapa kali user mencoba

while percobaan < maks_percobaan:
    print(f"Percobaan ke-{percobaan + 1} dari {maks_percobaan}")

    # Input dari pengguna (strip() membersihkan spasi di awal/akhir)
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()
    

    if username == USERNAME_BENAR and password == PASSWORD_BENAR:
        print("Login berhasil! Selamat datang, admin.")
        break  # keluar dari loop jika login benar
    else:
        percobaan += 1  # tambah jumlah percobaan
        sisa = maks_percobaan - percobaan

        if sisa > 0:
            print(f"Login gagal. Sisa percobaan: {sisa}")

# Bagian 5: Akhir program

print("\nProgram selesai.")
