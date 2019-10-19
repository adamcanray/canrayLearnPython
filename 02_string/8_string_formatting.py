# ----- header
# formatting didalam string memungkinkan kita untuk menyisipkan isi dari sebuah variabel ke dalam sebuah string.

# ----- start reading
# Perhatikan:
# * di dalam fomatting string kita akan menggunakan sebuah operator % setelah sebuah string.
# * operaton % digunakan untuk menggabungkan string dengan sebuah variabel.
# * symbol formatting yang digunakan di-point ini:
# ------------ format lama:
# ------------ * %s -- untuk variabel string
# ------------ * %d -- untuk variabel numeric atau decimal
# ------------ format baru:
# ------------ * {} -- bisa untuk string maupun number.
# ----- end.

# ----- start coding
# Implementasi:
# string
string = "Muhammad Adam Canrayneldy"
# cara lama
print("hi, nama saya %s" % string)
print("hi, nama saya %s %s" % ('Adam','Canray'))
# cara baru
print("hi, nama saya {}".format(string))
print("hi, nama saya {} {}".format('Adam','Canray'))


# number
number = 18
# cara lama
print("umur saya %d tahun" % number)
print("saya makan %d kali dalam %d hari" % (5,1))
# cara baru
print("umur saya {} tahun".format(number))
print("saya makan {} kali dalam {} hari".format(5,1))

# ----- end.

# note: banyak sekali macam-macam formatting dalam python, silahkan teman-teman pelajari sendiri.