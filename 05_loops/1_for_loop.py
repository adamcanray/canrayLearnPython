# ----- header
# for loop digunakan untuk beralih pada urutan yang diberikan.

# ----- start reading
# Perhatikan:
# * Pada setiap iterasi, variabel yang ditentukan dalam for loop akan ditugaskan ke nilai berikutnya dalam daftar.
# * langsung kita Implementasikan..
# -----end.

# ----- start conding
# Implementasi:
# range func
for i in range(5):
    print(i) # akan menghasilkan 0,1,2,3,4
# looping sebanyak element/item di list
_list = ['apel','jeruk','jambu',"mangga","salak"]
for buah in _list:
    print(buah) # mengeluarkan nilai dari item di dalam list

# perulangan for sebanyak character di dalam string
_string = "Adam, Canray"
for char in _string:
    print(char) # mengeluarkan character di dalam sebuah string

# perulangan for sebanyak character di dalam string
# setiap perulangannya variabel length ditambah 1
length = 0
for char in _string:
    length +=1 # menambahkan nilai 1 setiap perulangannya
# print apakah length dari _string itu sama dengan variabel length
print(len(_string) == length) # True

# -----end.

# note: silahkan pelajari sendiri agar kuat pemahamannya tentang for loop.