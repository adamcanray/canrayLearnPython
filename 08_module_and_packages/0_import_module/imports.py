# import module calculator
import calculator
# buat object
# ambil class Calculator() dari modul calculator
calc = calculator.Calculator()
# beri argument pada function add di class Calculator
calc.add(100)
# tampilkan ke console, function yang me-return nilai current yaitu get_current pada class Calculator
print(calc.get_current())


# import module my_module
import my_module
# jalankan function hello_world di dalam modul my_module
my_module.hello_world("Canray")