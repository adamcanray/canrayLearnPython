# ----- header
# keyword continue digunakan untuk melewati sisa kode di dalam loop 
# untuk loop yang saat ini dieksekusi dan kembali ke untuk atau sementara pernyataan.

# ---- start reading
# Perhatikan:
# * keyword continue sama seperti break dalam penulisan
# * tetapi berbeda dalam fungsi.
# ---- end.

# ---- start coding
# Implementasi:

# contoh 1
print("contoh 1:")
for i in range(5):
    # jika i bernilai 3
    if (i == 3):
        # maka continue
        continue
    # efect nya adalah ketika di print di bawah sini, nilai 3 tidak akan muncul
    print(i)

# contoh 2
print("contoh 2:")
for x in range(10):
    # cek jika var x itu genap
    if ( x % 2 == 0 ):
        continue
    # efect nya adalah ketika di print di bawah sini, nilai yang genap tidak akan muncul
    # karena di continue
    print(x)

# ---- end.

# note: semoga teman-teman mudah mengerti apa fungsi dari keyword continue ini.