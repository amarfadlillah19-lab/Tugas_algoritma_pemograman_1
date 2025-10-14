# Program buat konversi nilai angka ke nilai huruf

# minta input nilai dari user
nilai = int(input("Masukkan nilai: "))

# Cek rentang nilai dan tentuin nilai hurufnya
if 85 <= nilai <= 100:
    print("Nilai huruf: A")
elif 70 <= nilai <= 84:
    print("Nilai huruf: B")
elif 55 <= nilai <= 69:
    print("Nilai huruf: C")
elif 40 <= nilai <= 54:
    print("Nilai huruf: D")
else:
    print("Nilai huruf: E")
# Catatan: Asumsi nilai yang dimasukkan antara 0 sampai 100
