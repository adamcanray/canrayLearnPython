# ----- header
# Class pada dasarnya adalah templat untuk membuat objek Anda. 

# ----- start reading
# Perhatikan:
# * Objek menggabungkan variabel dan function menjadi satu kesatuan. 
# * Objek mendapatkan variabel dan functionnya dari class. 
# * Anda dapat menganggap suatu objek sebagai struktur data tunggal yang berisi data serta function. 
# * biasakan menulis nama class diawali dengan huruf mesar, contoh: class MyClass:
# * Function objek disebut method(function yang berada di dalam class)
# * class bisa berisi properti(variabel dalam class) dan method(function di dalam class)
# ----- end.

# ----- start coding
# class
class MyClass:
    # properti
    variabel = "ini adalah variabel"
    # method
    def foo(self): # self parameter akan dijelaskan pada taks file 2_self_parameter.py
        print("hello from function foo")

# variabel object
my_object = MyClass()
# memanggil method foo() yang ada di dalam class MyClass
my_object.foo()

# ----- end.

# note: semoga penjelasan diatas mudah untuk teman-teman pahami.