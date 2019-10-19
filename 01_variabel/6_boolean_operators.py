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

print("\nTeknik Berantai:")
# code diata masih menggunakan perbandingan biasa,
# di python kita bisa mengunakan teknik berantai dalam menantukan perbandingan seperti kasus ini.
# contoh:
# kita ciptakan satu buah variabel dengan nilai 15
nilai_tiga = 15
# tampilkan nilai
print("nilai_satu = " + str(nilai_satu) + "\nnilai_dua = " + str(nilai_dua) + "\nnilai_tiga = " + str(nilai_tiga))
# True
# kita akan membandingkan tiga buah variabel sekaligus atau lebih, teknik ini disebut teknik berantai
berantai_true = nilai_dua < nilai_satu < nilai_tiga
print("1. apakah (nilai_dua < nilai_satu) dan (nilai_satu < nilai_tiga)?\njawab: " + str(berantai_true))
# False
# kita akan membandingkan tiga buah variabel sekaligus atau lebih, teknik ini disebut teknik berantai
berantai_false = nilai_satu < nilai_dua < nilai_tiga
print("2. apakah (nilai_satu < nilai_dua) dan (nilai_dua < nilai_tiga)?\njawab: " + str(berantai_false) + " -- karena nilai_satu tidak kurang dari nilai_dua")

# ---------------------------- end.
