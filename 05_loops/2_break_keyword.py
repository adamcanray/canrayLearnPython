# ----- header
# break adalah sebuah keyword yang bisa kita gunakan untuk menghentikan perulangan.

# ----- start reading
# Perhatikan:
# * kita bisa menggunakan break saat sudah sesuai denga kondisi tertentu, misal:
# ------------ * ketika variabel nomor nilai nya sudah mencapai 5, maka hentikan perulangan. 
# ----- end.

# ----- start coding
# Implementasi:

# contoh 1
# var nomor
nomor = 0
# while True: -- akan melakukan perulangan terus-menerus karena nilai-nya selalu True.
# maka dari itu dengan menggunakan break lah kita dapat menghentikan sebuah perulangan.
while True:
    # setiap perulangan nomor akan ditambah 1
    nomor += 1
    # cetak nomor
    print(nomor)
    # cek jika nomor sudah bernilai 5
    if ( nomor == 5):
        # cetak pesan
        print("berhenti, nomor sudah bernilai %d" % nomor)
        # maka hentikan perulangan
        break

# contoh 2
# list buahan
pohon = ['apel',"jeruk","kelapa"]
while True:
    buah = pohon.pop()
    print(buah)
    # 
    if (buah == 'kelapa'):
        break
# ----- end.

# note: silahkan teman-teman pelajari lagi sendiri.