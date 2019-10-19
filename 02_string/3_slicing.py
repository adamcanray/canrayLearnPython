# ----- header
# teknik slicing seperti nama-nya(mengiris) 
# dia bisa mengiris sebuah string agar menjadi sub-string(STRING yang diambil langsung dari STRING).

# ----- start reading
# Perhatikan:
# * slicing hampir mirip dengan indexing, tetapi berbeda
# * slicing membutuhkan 2 buah index dan terpisah dengan colon(:)
# * kita yang menentukan ingin mengambil sub-string dari index ke-berapa sampai index berapa
# -- * slicing akan mengambil sub-string dari indexAwal sampai indexAkhir
# contoh penggunaan:
# ---------------- string[indexAwal:indexAkhir]
# ---------------- string[2:6]
# ----- end.

# ----- start coding
# kita buat variabel string
string = "saya Canray"
# kita buat variabel untuk mengambil "Canray" di dalam variabel string
sub_string = string[5:11]
# tampilkan 
print(sub_string)
# ----- end.

# note: perintah ini--> string[5:11] 
# ----- artinya kita ingin mengambil sub-string dimulai dari index ke-5 sampai SEBELUM index ke 11(berarti index ke-10)