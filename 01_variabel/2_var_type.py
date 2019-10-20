# ----- header
# dalam python ada dua buah type untuk number/nomor: integer dan float
# sebenarnya ada lagi tipe yang namanya complex(tidak akan dijelaskan disini, silahkan pelajari sendiri)
# perbedaan yang mencolok dari keduanya adalah:
# float itu angka decimal yang mempunya dot/titik(.) contoh: 2.5
# sedangkan integer itu hanya bilangan decimal yang bulat(tanpa titik, contoh: 1,25,100, dll)
# ----- start reading
# python memiliki built-in function type() -- untuk mengecek sebuah nilai/variabel itu type/tipe data nya apa
# ----- end.

# ----- start conding
# integer number
number = 10
# keluarkan tipe dari variabel number
print(type(number))

# float number
float_number = 2.5
# keluarkan tipe dari variabel float_number
print(type(float_number))

# string
string = "Muhammad Adam Canrayneldy"
# keluarkan tipe dari variabel string
print(type(string))

# array/list
# di dalam sebuah array berisi banyak element
# tipe data dari tiap-tiap element array itu bisa berbeda-beda
array = ['adam', 1, "maulie", 2.4]
# keluarkan tipe dari variabel array
print(type(array))
# output nya <class 'list'> --- karena dalam python array == list

# tuple
# tuple mirip seperti array
# beda-nya adalah sebuah tuple nantinya tidak bisa kita tambah, ubah, atau hapus item-nya.
tuple_ = ('adam', 1, "maulie", 2.4) 
print(type(tuple_))

# dictionary
# dictionary mirip seperti array/list, hanya saja kita menggunakan sebuah key sebagai pengganti index.
dict_ = {'apel' : 15, "jeruk" : 10, "mangga" : 5}
print(type(dict_))

# boolean
# boolean hanya bernilai True dan False
bool_ = True
print(type(bool_))

# ----- end.

# note: ini lah tipe data yang ada di dalam python, silahkan kalian pelajari lagi.
