# ----- header
# default parameter sangat berguna ketika digunakan, 
# mengingat tidak selamanya pemanggil function itu melengkapi argumentnya 
# sesuai dengan parameter yang disediakan oleh function.

# ----- start reading
# Perhatikan:
# * sebuah parameter default akan bekerja/digunakan ketika pemanggil function tidak lengkap mengirimkan argument.
# * langsung implementasi..
# ----- end.

# ----- start coding
# Implementasi:

# contoh 1:
# mendefinisikan function dengan menerima 2 parameter
# 1 parameter yang harus wajib diisi
# dan 1 parameter yang ketika tidak diisi itu akan berisi nilai default(dalam contoh ini nilainya b = 10)
def kali(a,b = 10):
    # kembalikan nilai
    return a * b
# tampilkan nilai kembalian dari function
print(kali(5, 3)) # kita lengkap mengirim 2 argument, output: 5 * 3 = 15
print(kali(5)) # kita hanya 1 argument, output: 5 * 10(nilai default) = 50

# contoh 2:
def say(subjek, name = "Adam"):
    return "hallo %s, nama saya %s" % (subjek, name)

print(say('teman',"Canray")) # lengkap, output: hallo teman, nama saya Canray
print(say('teman')) # hanya 1 argument, output: hallo teman, nama saya Adam(NILAI DEFAULT)
# ----- end.

# note: semoga teman-teman memahami nya dengan mudah.