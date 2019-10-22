# ----- header
# function adalah cara yang mudah untuk membagi kode kita menjadi blok yang berguna, 
# membuatnya lebih mudah dibaca dan membantu menggunakannya kembali.

# ----- start reading
# Perhatikan:
# * functiondalam Python didefinisikan dengan menggunakan keyword def
# * dan diikuti dengan nama dari function
# ----- end.

# ----- start coding
# tanpa menggunakan function
print("-----tanpa menggunakan function-----")
# penulisan kode harus berulang kali
print("halo nama saya Adam!")
print("halo nama saya Adam!")
print("halo nama saya Adam!")

# menggunakan function
print("-----menggunakan function-----")
# definisikan funciton
def halo():
    print("halo nama saya Adam!")

# hanya tinggal panggil function
halo()
halo()
halo()
# ----- end.

# note: silahkan panggil function menggunakan for atau while looping agar efektif.