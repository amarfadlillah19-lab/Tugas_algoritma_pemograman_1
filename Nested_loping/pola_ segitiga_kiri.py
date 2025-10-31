# Pola segitiga kiri
# Baris ini hanya komentar judul: menjelaskan program mencetak pola segitiga kiri.
for i in range(-1, 6):  # i iterasi dari -1 sampai 5 (nilai akhir eksklusif); nilai awal -1 membuat baris pertama kosong
    for j in range(1, i + 1):  # untuk setiap i, ulangi j dari 1 sampai i (inklusif) -> jumlah '*' sebanyak i
        print("*", end="")  # cetak tanda bintang tanpa pindah baris (end="" membuat terus di baris yang sama)
    print()  # setelah mencetak baris bintang untuk nilai i, pindah ke baris baru
         