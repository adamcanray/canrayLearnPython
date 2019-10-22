# ----- header 
# return adalah akan mengembalikan value kepada pemanggil function-nya.

# ----- start reading
# Perhatikan:
# * dalan sebuah function kita biasa me-return sebuah nilai/variabel yang nanti-nya akan ditampilkan
# * langsung kita implementasikan...
# ----- end.

# ----- start coding

# contoh 1:
# definisikan function yang menerima 2 parameter
def kali(nilai_1,nilai_2):
    return nilai_1 * nilai_2
# panggil function dengan memberikan 2 argument, lalu simpan ke variabel hasil
# nilai_1 = 10
# nilai_2 = 20
hasil = kali(10,20)
# print variabel hasil 
print(hasil)

# contoh 2:
# kita akan membuat sebuah function yang akan mereturn nilai fibonacci
def fib(n):
    # siapkan list kosong, untuk menyimpan deret fibonacci
    result = []
    # siapkan variabel awal
    a = 1
    b = 1
    # buat perulangan sebanyak nilai n, tergantung kondisi
    while a < n:
        # setiap perulangan, tambahkan nilai a ke dalam list result
        result.append(a)
        # operan nilai untuk menghasil kan deret fibponacci
        # buat var untuk menampung nilai b yang selalu bertambah
        temp_var = b
        # nilai b berisi a+b(nilainya selalu bertambah)
        b = a + b
        # nilai nya akan selalu bertambah kelipatan, karena temp_var = b dan b = a + b
        a = temp_var
    # kembalikan nilai list result
    return result

print(fib(40))
# ----- end.

# note: semoga teman-teman mudah memahami tentang penggunaan return keyword ini.