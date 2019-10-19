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
# saya ingin mengambil character 'A' pada kata 'Adam' diawal string lalu menyimpannya ke variabel
# karena index selalu dimulai dari index-0, maka saya bisa seperti ini:
# menggunakan index yang Positive
get_char_p = string[20]
# menggunakan index yang Negative
get_char_n = string[-16]
# saya akan tampilkan hasil nya ke console
print(get_char_p) # output: A
print(get_char_n) # output: A
# ----- end.

# note: silahkan teman-teman coba untuk menganti index-nya, dan perhatikan perubahannya