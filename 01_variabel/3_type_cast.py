# mengubah tipe data dari suatu nilai
# -------------------------------------- start reading
# ada beberapa built-in function yang memungkinkan kita untuk mengubah tipe data dari sebuah nilai ataupun variabel.
# contoh:
# 1.-- Integer to Float
# ---- kita memiliki sebuah number dengan tipe data integer misalkan 10
# ---- lalu kita ingin mengubah tipe nya menjadi float, itu bisa.
# ---- menggunakan built-in function float(integer). contoh:
# --------- * float(10) -- maka akan dihasilkan output: 10.0 --> float
# 2.-- Float to Integer
# ---- kita memiliki sebuah number dengan tipe data float misalkan 15.0
# ---- lalu kita ingin mengubah tipe nya menjadi integer, itu bisa.
# ---- menggunakan built-in function int(float). contoh:
# --------- * int(15.0) -- maka akan dihasilkan output: 15 --> integer
# 3.-- Integer to String
# ---- kita memiliki sebuah number dengan tipe data integer misalkan 10
# ---- lalu kita ingin mengubah tipe nya menjadi string, itu bisa.
# ---- menggunakan built-in function str(integer). contoh:
# --------- * str(10) -- maka akan dihasilkan output: 10 --> string
# 4.-- Float to String
# ---- kita memiliki sebuah number dengan tipe data float misalkan 15.0
# ---- lalu kita ingin mengubah tipe nya menjadi string, itu bisa.
# ---- menggunakan built-in function str(float). contoh:
# --------- * str(15.0) -- maka akan dihasilkan output: 15.0 --> string
# 5.-- String to Integer
# ---- dalam kasus ini syaratnya adalah:
# --------------- * isi string harus angka, contoh: string = "123"
# --------------- * string harus berisi hanya angka bilangan bulat, contoh salah: string = "2.0"
# ---- jika string memenuhi syarat maka string bisa di konversi ke integer,
# ---- menggunakan built-in function int(string). contoh:
# --------- * int("10") -- maka akan dihasilkan output: 10 --> integer
# --------- * int("10.0") -- maka akan dihasilkan output: ERROR
# 6.-- String to Float
# ---- dalam kasus ini syaratnya adalah:
# --------------- * isi string harus angka, contoh: string = "123"
# ---- jika string memenuhi syarat maka string bisa di konversi ke float,
# ---- menggunakan built-in function float(string). contoh:
# --------- * float("10") -- maka akan dihasilkan output: 10.0 --> float
# --------- * float("12.5") -- maka akan dihasilkan output: 12.5 --> float
# -------------------------------------- end.

# merealisasikan penjelasan diatas
# -------------------------------------- start code
# 1.-- Integer to Float
number = 10
# tampilkan
print(float(number))
# 2.-- Float to Integer
float_number = 10.0
# tampilkan
print(int(float_number))
# 3.-- Integer to String
number = 15
# tampilkan
print(str(number) + " -- Integer to String")
# 4.-- Float to String
float_number = 15.0
# tampilkan
print(str(float_number) + " -- Float to String")
# 5.-- String to Integer
# string harus angka bulat
my_string = "120"
# tampilkan
print(int(my_string))
# 6.-- String to Float
# string harus angka
my_string = "150.0"
# tampilkan
print(float(my_string))
# -------------------------------------- end.
