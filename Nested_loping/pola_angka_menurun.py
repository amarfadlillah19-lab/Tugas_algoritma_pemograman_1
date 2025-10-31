# pola angka menurun
for i in range(5, 0, -1):           # loop luar → mulai dari 5 turun ke 1 (jumlah baris)
    for j in range(1, i + 1):       # loop dalam → cetak angka dari 1 sampai nilai i
        print(j, end='')            # cetak angka tanpa ganti baris
    print()                         # pindah ke baris baru setelah satu baris selesai

