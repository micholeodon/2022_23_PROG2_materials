class Kalkulator:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodawanie(self):
        return self.a + self.b
    
    def odejmowanie(self):
        return self.a - self.b
    
    def mnozenie(self):
        return self.a * self.b
    
    def dzielenie(self):
        return self.a / self.b


calc = Kalkulator(4,3)

print(calc.dodawanie())
print(calc.odejmowanie())
print(calc.mnozenie())
print(calc.dzielenie())