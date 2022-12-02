class Student:
    
    # atrybuty klasy
    uniwersytet = "UMK"
    mozliweKierunki = ["Kognitywistyka", "Psychologia", "Informatyka"]

    # metoda klasy
    def przywitajSie(self):
        print("Dzień dobry!")

    # konstruktor klasy (poznasz po specjalnej nazwie metody: __init__)
    def __init__(self, name, kierunek):
        self.imie  =  name # atrybut instancji
        self.kierunek = kierunek # atrybut instancji

        if kierunek in Student.mozliweKierunki: # dostęp do atrybutu klasy poprzez nazwę klasy
            self.wydzial = "Wydzial Psychologii"
        else:
            self.wydzial = "Spoza wydzialu"
        
    # metoda klasy
    def przedstawSie(self):
        self.przywitajSie()
        print(f"Mam na imię {self.imie}. Studiuję na kierunku {self.kierunek}.")


        
# GŁÓWNY PROGRAM 

# tworzenie instancji klasy
stud1 = Student("Gosia", "Kognitywistyka")
stud2 = Student("Adam", "Weterynaria")

# wywołanie metody klasy
stud1.przedstawSie()
stud2.przedstawSie()

# dostęp do atrybutu instancji
print(stud1.imie)

# dostęp do atrybutu klasy
print(stud1.uniwersytet)
print(Student.uniwersytet)
