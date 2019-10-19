# ----- header
# python memiliki built-in funciton/function bawaan yaitu len() yang bisa kita gunakan 
# untuk menghitung panjang dari sebuah string.

# ----- start reading
# Perhatikian:
# * len("string") -- ini akan mengembalikan nilai panjang dari "string" yaitu: 6
# * break dan spasi akan terhitung 1 dengan len()
# ----- end.

# ----- start conding
# buat variabel string dengan """ini artinya sebuah string bisa lebih dari 1 baris tanpa menggunakan \n sebagai break."""
# break dan spasi akan terhitung 1 dengan len()
name = """
Adam Canray
Adam Canray
"""
# tampilkan hasil
lens = len(name)
print(lens)
# ----- end.