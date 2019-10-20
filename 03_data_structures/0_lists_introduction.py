# ----- header
# mengenal list
# list dalam python adalah sebuah array, atau kumpulan nilai yang disimpan di dalam satu variabel

# ----- start reading
# Perhatikan:
# -- * list mungkin berisi item dengan tipe data yang berbeda,
# -- * tetapi biasanya semua item dalam list memiliki tipe yang sama.
# -- * sama seperti string yang kita pelajari sebelemunya,
# -- * sebuah list dapat kita akses nilai dari item/elemen-nya menggunakan index.
# -- * dan dapat diiris/slice seperti string.
# -- * list ada yang satu dimensi saja dan multi dimensi.
# -- * cara penulisan list:
# ------------------ * satu dimensi:
# ------------------ * kotak = [index-0, index-1, index-2]
# ------------------ * dua dimensi:
# ------------------ * kotak = [index-0, [index-0, index-1]]
# -- * cara pengaksesan kotak:
# ------ * satu dimensi:
# ----------- * print(kotak)
# ----------- * print(kotak[1])
# ----------- * print(kotak[0:2])
# ----------- * print(kotak[:])
# ------ * dua dimensi:
# ----------- * print(kotak[0][1]) -- artinya kita ingin menampilkan item-list dari list index ke-0 dan item index ke-1
# ----- end.

# ----- start coding
# Implementasi:
# list satu dimensi
kotak_satu = [1,3.0,5,6.8,7]
print(kotak_satu)
# kita cek type dari masing-masing item/elemen di dalam list
# ini akan membuktikan bahwa sebuah list bisa memiliki item/elemen dengan tipe data yang berbeda
print(type(kotak_satu[0])) # int
print(type(kotak_satu[1])) # float

# berisi string dan list(list di dalam list)
kotak_dua = ['Adam',"Canray",18,['Futsal',"Coding"]]
print(kotak_dua)
print(type(kotak_dua))

# print biodata saya
print("hi, nama saya %s %s, umur saya %d tahun.\nhobi saya %s dan %s" 
    % (kotak_dua[0],kotak_dua[1],kotak_dua[2],kotak_dua[3][0],kotak_dua[3][1]))
# ----- end.

# note: silahkan teman-teman ber-eksplorasi sendiri, semangat.