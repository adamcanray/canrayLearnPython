# ----- header
# Kata kunci in digunakan untuk memeriksa apakah List atau Dictionary berisi item tertentu

# ----- start reading
# Perhatikan:
# * keyword 'in' biasa digunakan untuk mengecek:
# ----- * apakah sebuah nilai itu terkandung didalam sebuah string, list ataupun dictionary.
# * in -- akan mengembalikan nilai True jika suatu nilai itu terkandung di suatu variabel.
# * not in -- akan mengembalikan nilai True jika suatu nilai itu tidak terkandung di suatu variabel.
# ----- end.

# ----- start coding
# buat list baru
list_buah = ['apel',"jambu",'jeruk']
# tampilkan
print("apel" in list_buah) # "apel" terkandung didalam list_buah -- true
print("apel" not in list_buah) # "apel" tidak terkandung didalam list_buah -- false: karena apel terkandung.

# buat dictionary baru
dict_buah = {"apel" : 10,'mangga' : 15,'kelapa' : 20}
# tampilkan
print("jeruk" in dict_buah.keys()) # apakah "jeruk" tekandung di dalam dict_buah -- false: karena tidak terkandung.
print("jeruk" not in dict_buah.keys()) # apakah "jeruk" tidak tekandung di dalam dict_buah -- true

# ----- end.

# note: silahkan coba-coba mengganti code diatas, lalu jalankan untuk melihat perubahan-nya.