# ---- header
# operasi dalam list di Python,
# adalah bagaimana cara kita dalam memanipulasi sebuah item/element di dalam list.

# ----- start reading
# Perhatikan:
# * dalam pengoprasian sebuah list ada banyak sekali caranya
# * dipoint ini saya akan menjelaskan kasus yang cukup sederhana saja tetapi akan sering digunakan.
# * dalam pengoprasian sebuah list kita bisa menggunakan fungsi dan method bawaan atau code kita sendiri.
# ----- end.

# ----- start coding
# Implementasi:

# membuat sebuah list buah
buah = ['apel','nanas','salak']

# CREATE
# menambahkan satu item/element pada akhir list menggunakan apend()
buah.append("jeruk") # hanya menerima satu parameter saja
print(buah)
# menggunakan teknik
buah += ['lemon','mangga'] # bisa memasukan item lebih dari satu
print(buah)
# menambahkan satu item juga bisa menggunakan insert(index, item)
buah.insert(0,"nangka")
print(buah)

# EDIT
# mengubah nilai dari item di dalam list
buah[0] = "jambu"
print(buah)

# DELETE
# teknik slicing dalam operasi list
# menghapus sebuah dari list
buah[0:1] = [] # menghapus 1 item di index 0 
print(buah)
buah[0:2] = [] # menghapus 2 item di index 0 dan index 1
print(buah)


# REPLACE
buah[0:1] = ["pear"] # menggantikan 1 item di index 0
print(buah)
buah[0:2] = ["leci"] # menggantikan 2 item di index 0 dan index 1
print(buah)

# CLEAR
buah[:] = [] # menghapus semua item pada list
print(buah)

# ----- end.

# note: ada banyak sekali teknik untuk memanipulasi sebuah list di dalam Python,
# ----- silahkan teman-teman cari tahu sendiri.