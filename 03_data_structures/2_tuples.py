# ----- header
# Tuple adalah kumpulan objek Python yang dipisahkan oleh koma. 
# Dalam beberapa hal tuple mirip dengan List dalam hal pengindeksan, 
# objek bersarang, dan pengulangan. 
# tetapi tupel tidak berubah seperti daftar yang dapat diubah

# ----- start reading
# Perhatikan:
# * Tuples hampir identik dengan list. Satu-satunya perbedaan yang signifikan antara tupel dan list 
# * adalah tupel tidak dapat diubah: Anda tidak dapat menambah, mengubah, atau menghapus elemen dari tupel. 
# * Tuple dibuat oleh operator koma yang diapit tanda kurung, misalnya (a, b, c). 
# * Satu item tuple harus memiliki koma trailing, seperti (d,)
# ----- end.

# ----- start coding
# implementasi:

# coba untuk mematikan komentar kode dibawah ini lalu jalankan.
# kode ini membuktikan bahwa Tuple tidak bisa diubah.
# kode:
# tuple_ubah = ('a','b','c')
# tuple_ubah[0] = 'd'
# print(tuple_ubah)

# empty tuple
tuple_kosong = ()
print(tuple_kosong)

# Satu cara penciptaan
tuple_satu = 'Adam',
print(tuple_satu)
# cara lain untuk melakukan hal yang sama
tuple_dua = ('Muhammad','Canrayneldy')
print(tuple_dua)

# Concatenation of Tuples(Penggabungan Tuple)
print(tuple_satu + tuple_dua)

# membuat Tuple bersarang
tuple_tiga = (tuple_satu, tuple_dua)
print(tuple_tiga)

# membuat tuple dengan pengulangan
# cara nya seperti ini:
tuple_empat = (tuple_satu,)*5 # menghasilkan tuple bersarang
print(tuple_empat)
# atau ini:
print(tuple_satu*5) # menghasilkan item tuple yang berlipat ganda

# ----- end.

# note: masih banyak sebetul nya teknik untuk menggunakan sebuah Tuple ini,
# ----- silahkan teman-teman coba cari tahu dan pelajari sendiri.
# ----- agar pemahaman teman-teman untuk Tuple ini kuat.