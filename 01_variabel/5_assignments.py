# pengenalan assignment operators pada python

# ----------------------- start reading
# operator:
# -- 1. =   --- contoh: c = a + b  <-- var c akan berisi nilai hasil a + b
# -- 2. +=  --- contoh: c += a  <-- var c akan berisi nilai c ditambah nilai a. c = c + a
# -- 3. -=  --- contoh: c -= a  <-- var c akan berisi nilai c dikurang nilai a. c = c - a
# -- 4. *=  --- contoh: c *= a  <-- var c akan berisi nilai c dikali nilai a. c = c * a
# -- 5. /=  --- contoh: c /= a  <-- var c akan berisi nilai c dibagi nilai a. c = c / a
# -- 6. %=  --- contoh: c %= a  <-- var c akan berisi nilai c modulus nilai a. c = c % a -- c akan berisi sisa bagi dari c : a
# -- 7. **= --- contoh: c **= a  <-- var c akan berisi nilai c pangkat nilai a. c = c ** a
# -- 8. //= --- contoh:  c //= a  <-- var c akan berisi nilai c dibagi nilai a. c = c // a
# --- operator // akan mengembalikan nilai hasil pembagian dengan bulat(tidak ada dot/titik) jika angka pertama yang dibagi adalah integer, contoh: 12 // 11 = 1
# --- operator // akan mengembalikan nilai hasil pembagian float(memiliki dot/titik) jika angka pertama yang dibagi adalah float, contoh: 12.0 // 11 = 1.0
# ----------------------- end

# ----------------------- start code
# buat variabel
a = 10
b = 5
c = 0
# tampilkan variabel
print("nilai awal:\na = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c))
# 1. operator assignment '='
c = a + b
print("c = a + b ---- jadi nilai c sekarang = " + str(c))
# 2. operator assignment '+='
c += a
print("c += a ------- jadi nilai c sekarang = " + str(c))
# 3. operator assignment '-='
c -= a
print("c -= a ------- jadi nilai c sekarang = " + str(c))
# 4. operator assignment '*='
c *= a
print("c *= a ------- jadi nilai c sekarang = " + str(c))
# 5. operator assignment '/='
c /= a
print("c /= a ------- jadi nilai c sekarang = " + str(c))
# 6. operator assignment '%='
c %= a
print("c %= a ------- jadi nilai c sekarang = " + str(c))
# 7. operator assignment '**='
c **= a
print("c **= a ------- jadi nilai c sekarang = " + str(c))
# 8. operator assignment '//='
c //= a
print("c //= a ------- jadi nilai c sekarang = " + str(c))
# ----------------------- end
