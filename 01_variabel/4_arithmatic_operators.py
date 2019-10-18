# operator aritmatika di dalam python

# -------------------------------------- start reading
# operator dalam python:
# -- 1. penjumlahan(+)
# ----- contoh penggunaan: 10 + 10 <-- hasil: 20
# -- 2. pengurangan(-)
# ----- contoh penggunaan: 10 - 5 <-- hasil: 5
# -- 3. perkalian(*)
# ----- contoh penggunaan: 10 * 5 <-- hasil: 50
# -- 4. pembagian(/)
# ----- contoh penggunaan: 10 / 5 <-- hasil: 2
# -- 5. modulus/sisa bagi(%)
# ----- contoh penggunaan: 5 % 2 <-- hasil: 1
# -- 6. perpangkatan(**)
# ----- contoh penggunaan: 10 ** 3 <-- hasil: 1000
# -------------------------------------- end.

# -------------------------------------- start code
# var nilai a dan b
a = 10
b = 5
# print a dan b
print("nilai a = " + str(a) + "\nnilai b = " + str(b))
# -- 1. penjumlahan(+)
jumlah = a + b
print("a + b hasilnya = " + str(jumlah))
# -- 2. pengurangan(-)
kurang = a - b
print("a - b hasilnya = " + str(kurang))
# -- 3. perkalian(*)
kali = a * b
print("a x b hasilnya = " + str(kali))
# -- 4. pembagian(/)
bagi = a / b
print("a : b hasilnya = " + str(int(bagi)))
# -- 5. modulus/sisa bagi(%)
modulus = a % b
print("a : b sisa baginya adalah = " + str(modulus))
# -- 6. perpangkatan(**)
pangkat = a ** b
print("a pangkat b hasilnya = " + str(pangkat))
# -------------------------------------- end.

# note: semua hasil yang di print adalah konversi dari integer ke string.
# ----- kita sudah belajar konversi tipe data pada point 3_type_cast.py
