class Osoba:

    def __init__(self, name, surname, phone):
        self.imie = name 
        self.nazwisko = surname 
        self.tel = phone 

    def __str__(self) -> str:
        return f"{self.nazwisko}, {self.imie}: {self.tel}"

    def zmienImie(self, noweImie):
        self.imie = noweImie

    def zmienNazwisko(self, noweNazwisko):
        self.nazwisko = noweNazwisko
    
    def zmienTelefon(self, nowyTelefon):
        self.tel = nowyTelefon


class ksiazkaTelefoniczna:

    def __init__(self):
        self.listaOsob = set() # set by ksiazka nie zawierala powtorzen

    def dodajOsobe(self, osoba: Osoba):
        self.listaOsob.add(osoba)

    def usunOsobe(self, osoba:Osoba):
        self.listaOsob.remove(osoba)

    def podajLiczbeOsob(self):
        return len(self.listaOsob)

    def wyswietlKsiazke(self):
        for o in self.listaOsob:
            print(o)


k = ksiazkaTelefoniczna()
o1 = Osoba("Jan", "Kowalski", 123234231)
o2 = Osoba("Jerzy", "Nowak", 647232553)
o3 = Osoba("Ludmila", "Stachura", 213424000)
k.dodajOsobe(o1)
k.wyswietlKsiazke()
o1.zmienImie("Henryk")
k.wyswietlKsiazke()
k.usunOsobe(o1)
k.wyswietlKsiazke()
k.dodajOsobe(o2)
k.dodajOsobe(o3)
k.wyswietlKsiazke()


