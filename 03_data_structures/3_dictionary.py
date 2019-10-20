# ----- header
# dictionary atau kamus, ini mirip dengan List bedanya adalah 
# kita dapat mengakses isi(value)-nya dengan menggunakan kunci(key) bukannya index.

# ----- start reading
# Perhatikan:
# * cara membuat dictionary:
# ---------------------- * stok_buah = {'apel' : 10, 'jeruk' : 15} <-- key:'apel', value:10
# * cara memanggil dictionary:
# ---------------------- * print(stok_buah["apel"])  <-- berarti kita ingin menampikan nilai dari key "apel"
# ----- end.

# ----- start coding 
# Implementasi:

# membuat dictionary baru
stok_buah = {'apel':10, "jeruk":15, "salak":5}
# menampilkan dictionary
print(stok_buah)
print("Stok buah apel adalah = " + str(stok_buah['apel']))

# menghapus pasangan nilai dan kunci dari stok_buah
del stok_buah['apel']
print(stok_buah)

# menambahkan nilai dan kunci ke stok_buah
stok_buah['belimbing'] = 30
print(stok_buah)

# tampilkan key dari dictionary stok_buah
print(stok_buah.keys())
# tampilkan value dari dictionary stok_buah
print(stok_buah.values())

# ----- end. 

# note: silahkan teman-teman coba cari tekniklain terkait Dictionary dan pelajari sendiri, 
# ----- supaya lebih kuat pemahaman-nya.