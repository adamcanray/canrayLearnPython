# boolean adalah jenis nilai yang hanya bisa benar(True) atau salah(False)

# ---------------------------- start reading
# contoh:
# * mengahasilkan nilai False
# -- kita memiliki variabel: equal = 5 == 10
# -- yang didalamnya itu mengecek: angka 5 itu sama dengan atau tidak dengan angka 10
# -- kita tau jawabnya pasti tidak ya, karena angka 5 tidak sama dengan angka 10
# -- maka variabel equal menghasilkan nilai: False
# * mengahasilkan nilai True
# -- kita memiliki variabel: equal = 5 == 5
# -- yang didalamnya itu mengecek: angka 5 itu sama dengan atau tidak dengan angka 5
# -- kita tau jawabnya pasti benar ya, karena angka 5 itu sama dengan angka 5
# -- maka variabel equal menghasilkan nilai: True
# ---------------------------- end.

# ---------------------------- start coding
# tetapkan nilai awal
nilai_satu = 10
nilai_dua = 5

# 1. operator sama dengan
equal = nilai_satu == nilai_dua
# print hasil nya
print("1. apakah " + str(nilai_satu) + " itu sama dengan " + str(nilai_dua) + "?\njawab: " + str(equal))
# 2. operator lebih dari
g_than = nilai_satu > nilai_dua
# print hasil nya
print("2. apakah " + str(nilai_satu) + " itu lebih besar dari " + str(nilai_dua) + "?\njawab: " + str(g_than))
# 3. operator kurang dari
l_than = nilai_satu < nilai_dua
# print hasil nya
print("3. apakah " + str(nilai_satu) + " itu kurang dari " + str(nilai_dua) + "?\njawab: " + str(l_than))

# ---------------------------- end.
