# ----- header
# Fungsi __init__ digunakan untuk menginisialisasi objek yang dibuatnya.

# ----- start reading
# Perhatikan:  
# * __init__ adalah kependekan dari "inisialisasi". __init __ () selalu mengambil setidaknya satu argumen, 
# * self, yang mengacu pada objek yang sedang dibuat. 
# * Fungsi __init __ () mengatur setiap objek yang dibuat oleh kelas.
# ----- end.

# ----- start reading
# Implementasi:
# class
# contoh 1:
class Square:
    # deifinisikan function
    def __init__(self): # __init__ adalah method spesial
        # membuat nilai sides = 4
        self.sides = 4
# buat object
square = Square()
print(square.sides)

# contoh 2:
# class
class Car:
    def __init__(self, color):
        self.color = color

car = Car("blue") # Catatan: Anda tidak boleh memberikan/melewati parameter self secara eksplisit, hanya parameter warna
# tampilkan
print(car.color)

# ----- end.

# note: pelajari lagi agar pemahaman pada fungsi __init__ itu kuat.