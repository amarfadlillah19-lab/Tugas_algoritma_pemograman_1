# Program kasir sederhana untuk ngitung total bayar setelah diskon

# minta input total belanja dari user
total_belanja = float(input("Masukkan total belanja: Rp "))

# menentuin diskon berdasarkan total belanja
if total_belanja >= 500000:
    diskon = 0.2 * total_belanja
elif total_belanja >= 250000:
    diskon = 0.1 * total_belanja
else:
    diskon = 0

# ngitung total bayar setelah diskon
total_bayar = total_belanja - diskon

# nampilin hasilnya
print(f"Total Belanja : Rp {total_belanja:,.0f}")
print(f"Diskon        : Rp {diskon:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")
