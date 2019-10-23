# ---- header
# file ini untuk me READ/BACA sebuah file .txt

# ---- start reading
# Perhatikan:
# * anggap kita mempunya sebuah inputan berupa file .txt
# * yang isi nya akan kita read pada file ini
# * kita menggunakna built-in function open()
# * parameter pertama adalah "letak dannama_file", parameter kedua adalah methodnya: read itu "r", write itu "w"
# * readlines() -- akan menghasilkan nilai array, setiap baris nya akan dipisah menjadi array
# * readline() -- akan menghasilkan nilai baris pertama yang ada di suatu file .txt
# ---- end.

# ---- start coding
# Implementasi:
# contoh 1:
# buat variabel untuk menyimpan perintah open file
f = open("D:/belajar/belajarPython/latihan_course_pycharm/Introduction to Python/09_file_input_output/0_read_file/input.txt", "r")
# buat perulangan sebanyak array-nya -- menggunakan readline() menjadi array
for line in f.readlines():
    # print line(baris)
    print(line)
# selalu close file di akhir setelah kita open file
f.close()

# 
print("---batas---")

# contoh 2:
# buat variabel untuk menyimpan perintah open file
f1 = open("D:/belajar/belajarPython/latihan_course_pycharm/Introduction to Python/09_file_input_output/0_read_file/input_1.txt", "r")

# tampilkan array hasil readlines()
# print(f1.readlines())
# tampilkan baris pertama
# print(f1.readline())
# tampilkan baris pertama cara 2
# print(f1.readlines()[0])

# tampilkan semua text menggunakan loop
for line in f1.readlines():
    print(line)


f1.close()

# ---- end.

# note: komentari bagian perulangan for loop jika kalian ingin menampilkan kode diatasnya(array hasil readlines, dll) 