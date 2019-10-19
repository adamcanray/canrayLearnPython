# ----- header
# di dalam python kita bisa mengakses/mengambil sebuah character di dalam sebuah string,
# jika kita mengetahui posisi character tersebut berada pada index keberapa.

# ----- start reading
# Perhatian:
# * cara penulisan: string[index]
# * index di dalam string selalu dimulai dari index ke-0
# * untuk angka negative -0 itu sama saja dengan 0
# * jadi, untuk negative index-nya dimulai dari -1
# * whitespace/spasi akan dihitung index-nya dalam sebuah string
# ----- end.

# ----- start conding
string = "hallo saya Muhammad Adam Canrayneldy"
# saya ingin mengambil character 'h' pada kata 'hallo' diawal string lalu menyimpannya ke variabel
# karena index selalu dimulai dari index-0, maka saya bisa seperti ini:
get_char = string[0]
# saya akan tampilkan hasil nya ke console
print(get_char)
# ----- end.

# note: silahkan teman-teman coba untuk menganti index-nya, dan perhatikan perubahannya