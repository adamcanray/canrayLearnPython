# import module calculator
# import from
from calculator import Calculator
# buat object
calc = Calculator() # disini kita tidak memerlukan awalan modul calculator.Calculator() lagi
calc.add(50)
# tampilkan hasil dari function get_current pada module calculator
print(calc.get_current())

# import module my_module
from my_module import hello_world
# jalankan function hello_wolrd dengan memberi argument
hello_world("Canray") # function hello_wolrd dijalankan tanpa awalan my_module