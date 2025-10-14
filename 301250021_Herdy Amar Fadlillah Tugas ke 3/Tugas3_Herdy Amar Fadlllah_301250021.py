# Tugas 3 - Herdy Amar Fadlillah (301250021)
# Program untuk nentukan Bilangan Positif, Negatif, atau Nol

# minta input dari user
angka = int(input("masukan bilangan:"))

# nentuin bilangan positif, negatif, atau nol
if angka > 0:
    print("bilangan positif")
elif angka < 0:
    print("bilangan negatif")
else:
    print("bilangan nol")