# ----- header
# operator boolean membandingkan pernyataan dan mengembalikan hasil dalam nilai boolean.
# ----- start reading
# Perhatikan:
# * operator boolean -- and -- akan mengahasilkan nilai True jika nilai dikedua sisi and itu benar.
# * operator boolean -- or  -- akan mengembalikan True ketika setidaknya satu ekspresi di kedua sisi or adalah True.
# ----- end.

# ----- start coding
# Implementasi:
name = "adam"
age = 18
# or
print(name == "adam" or age == 17) # True karena setidak-nya ada satu kondisi yang True.
# or not
# cek apakah name mengandung "david" -- False
# atau tidak, cek apakah name mengandung "adam" dan age == 17 -- False
print(name is "david" or not (name is "adam" and age == 17)) # hasil nya True
# and
print(name == "adam" and age == 17) # False karena hanya satu kondisi yang True.
# and not
print(name == "adam" and not age == 17) # True karena age itu tidak benar == 17

# ----- end.

# note: silahkan teman-teman coba poelajari sendiri, semangat.