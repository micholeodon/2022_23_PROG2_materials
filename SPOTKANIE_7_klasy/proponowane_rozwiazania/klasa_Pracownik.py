class Pracownik:

    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

class Firma:

    def __init__(self):

        self.listaPracownikow = set()

    def zatrudnijPracownika(self, pracownik:Pracownik):
        self.listaPracownikow.add(pracownik)

    def zwolnijPracownika(self, pracownik:Pracownik):
        self.listaPracownikow.remove(pracownik)

    def obliczWydatkiFirmy(self):
        wydatki = 0
        for p in self.listaPracownikow:
            wydatki += p.pensja

        return wydatki

jan = Pracownik("Jan", "Kowalski", 1200)
ola = Pracownik("Aleksandra", "Nowak", 14800)

IBM = Firma()
IBM.zatrudnijPracownika(jan)
IBM.zatrudnijPracownika(jan) # dzieki implementacji w postaci zbioru (linia 12) nie mozna zatrudnic tej samej osoby wiele razy
IBM.zatrudnijPracownika(jan)
IBM.zatrudnijPracownika(ola)
print(IBM.obliczWydatkiFirmy())
IBM.zwolnijPracownika(jan)
print(IBM.obliczWydatkiFirmy())