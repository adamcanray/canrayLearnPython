# class calculator
class Calculator:
    # inisialisasi, current = 0
    def __init__(self):
        self.current = 0
    # curent akan ditambahkan amount dari parameter yang diterima
    def add(self, amount):
        self.current += amount
    # ambil nilai current
    def get_current(self):
        return self.current