# ----- header
# mengakses variabel di dalam objek. 

# ----- start reading
# Perhatikan:
# * kita dapat mengubah nilai variabel yang didefinisikan dalam kelas untuk instance berbeda (objek) dari kelas ini.
# * langsung ke Implementasi..
# ----- end.

# ----- start coding
# Implementasi:

# contoh 1:
# class
class MyClass:
    # variabel didalam class(properti)
    variabel1 = 1
    variabel2 = 2
    # function didalam class(method)
    def foo(self): # self parameter akan dijelaskan pada taks file 2_self_parameter.py
        print("hallo saya adalah function foo!")

# buat objek
my_object = MyClass()
# buat objek baru
my_object1 = MyClass()

my_object.variabel2 = 5 # mengubah value yang disimpan didalam variabel1 pada object my_object

# tampilkan nilai variabel2 pada masing masing object
print(my_object.variabel2) # output: 5 -- karena sudah diubah dengan cara diatas.
print(my_object1.variabel2) # output: 2 -- tetap dua karena memang di object my_object1 itu tidak merubah si variabel2

# memanggil function dari object my_object
my_object.foo()

# tampilkan nilai variabel1 dari object my_object
print(my_object.variabel1)


# contoh 2:
# class
class Car:
    color = ""
    def description(self):
        description_string = "Ini adalah mobil berwarna %s" % self.color
        return description_string

# objeck
car1 = Car()
car2 = Car()

# isi varibel color di dalam class Car
car1.color = "biru"
car2.color = "merah"

# tampilkan nilai
print(car1.description())
print(car2.description())

# ----- end.

# note: silahkan pelajari sendiri tentang peng-akses-an variabel dalam class ini, semoga mudah dipahami.