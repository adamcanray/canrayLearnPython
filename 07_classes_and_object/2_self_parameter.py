# ----- header
# Saatnya untuk menjelaskan parameter self yang digunakan dalam tugas sebelumnya. 

# ----- start reading
# Perhatikan:
# * Parameter self adalah konvensi Python. 
# * self adalah parameter pertama yang diteruskan ke metode kelas apa pun. 
# * Python akan menggunakan parameter mandiri untuk merujuk ke objek yang sedang dibuat.
# ----- end.

# ----- start coding
# Implementasi:
# class
class Calculator:
    # variabel
    current = 0
    def add(self, amount):
        while True:
            self.current += amount
            if amount > 0:
                break
        return self.current

    def get_current(self):
        return self.current

# panggil
print(Calculator().add(100))

# ----- end.

# note: semoga penjelasan diatas bisa membuat kalian paham fungsi dari parameter self itu sendiri.