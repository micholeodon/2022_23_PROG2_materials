import random
from time import sleep

class Student:
    # prywatne atrybuty klasy - poznasz po __ na poczatku nazwy; mozna sie do nich dobrac w srodku klasy Student
    __możliweStany = ["śpi", "neutralny", "nieszczęśliwy", "szczęśliwy", "naukowa mania", "zmęczony", "martwy"]
    
    # przydaje sie w metodzie coSlychac() by przetlumaczyc stan studenta na to co student powie
    __stanNaKomentarz = {
        __możliweStany[0]: "...zzzZZZzzz...", 
        __możliweStany[1]: "A jakoś leci...", 
        __możliweStany[2]: "Smutno mi ;(", 
        __możliweStany[3]: "Życie jest piękne!", 
        __możliweStany[4]: "OMGGGGG!!!! JAKIE TO WSZYSTKO CIEKAWE !!!!", 
        __możliweStany[5]: "Ufff ... jak nie odpocznę to padnę ...", 
        __możliweStany[6]: "[*]"}

    # konstruktor
    def __init__(self, nick, setWiedzy=set()):
        '''konstruktor klasy. setWiedzy jest zbiorem dlatego set. 
        Domyslnie ustawiany na pusty zbior czyli set().
        setWiedzy jest zbiorem by nie bylo duplikatow umiejetnosci'''
        self.nick = nick
        self.stan = Student.__możliweStany[1]
        self.wiedza = setWiedzy

    # metoda publiczna (nie ma __ na poczatku nazwy)
    def coSlychac(self):
        '''Student cos mowi w zaleznosci od swojego stanu.'''
        print(f"- {self.nick}: {Student.__stanNaKomentarz[self.stan]}")

    def powiedzCoUmiesz(self):
        '''Student, jeśli żyje, wymienia to co wie.'''

        if self.stan == Student.__możliweStany[-1]: # martwy
            print(f"- {self.nick}: ...")
        else: # nie martwy
            if len(self.wiedza) == 0:
                print(f"- {self.nick}: Uhmm... niczego jeszcze się nie dowiedziałem ...")
            else:
                print(f"- {self.nick}: Hej mam wiedzę na następujące tematy:")
                for skill in self.wiedza:
                    print(skill, end=", ")    
                print() # przejście do nowej linii

    # metoda prywatna - mozna ją wywoływać tylko w srodku klasy; poznasz po __ na poczatku nazwy
    def __zmienStan(self, stan):
        '''Metoda prywatna do zmiany stanu studenta na stan przekazany w argumencie.'''

        # czy żyje?
        if(self.stan != Student.__możliweStany[-1]):
            self.stan = stan
            print(f"Stan studenta {self.nick} pomyślnie zmieniony na {self.stan}.")
        else:
            print("Student nie żyje ... Nic nie da się zrobić :(")

    # kolejna metoda prywatna
    def __czekanko(czas):
        '''Wyswietla kropki co pół sekundy. 
        Wyświetli tyle kropek ile jest w wartosci zmiennej czas'''

        while czas > 0:
            print(".", end="")
            czas -= 1
            sleep(0.5)
        print()

    def __nauczSie(self, wiedza):
        '''Dodaje do zbioru wiedzy studenta to co jest w przekazanym zbiorze wiedza'''
        self.wiedza = self.wiedza.union(wiedza)

    
    def śpij(self):
        print(f"- God: Studencie {self.nick} - idźże spać!")
        self.__zmienStan(Student.__możliweStany[0])

    def obudźSię(self):
        print(f"- God: Studencie {self.nick} - pobudka!")
        # losuje losowy stan po wybudzeniu
        self.__zmienStan(random.choice(Student.__możliweStany))

    def uczSię(self):
        print(f"- God: Studencie {self.nick} - a może się pouczysz?")

        if(self.stan == Student.__możliweStany[4]): # __możliweStany[4] == naukowa mania
            self.__zmienStan(Student.__możliweStany[5]) # __możliweStany[5] == zmeczenie
        elif(self.stan == Student.__możliweStany[5]):
            self.__zmienStan(Student.__możliweStany[-1]) # __możliweStany[-1] == martwy
        else: 
            self.__zmienStan(Student.__możliweStany[4])

    def spotkajPrzyjaciół(self):
        print(f"- God: Studencie {self.nick} - idźże slayować z przyjaciółmi!")
        self.__zmienStan(Student.__możliweStany[3]) # szczęśliwy


    def porozmawiajZ(self, osoba):
        '''Metoda która pozwala studentowi self uwspólnić zbiory wiedzy z obiektem osoba.
        Tzn. jeśli self.wiedza = {'a', 'b'} a osoba.wiedza = {'c'} to po wykonaniu tej operacji:
        self.wiedza = {'a', 'b', 'c'}, osoba.wiedza = {'a', 'b', 'c'}'''

        # sprawdzam czy ktorys z rozmowcow nie jest martwy
        if(self.stan == Student.__możliweStany[-1] or osoba.stan == Student.__możliweStany[-1]):
            print("- God: Jeden z rozmówców nie żyje, więc rozmowa nie dojdzie do skutku ...")
        else:
            # powitanie
            print(f"{self.nick}: Siemasz {osoba.nick}!")
            print(f"{osoba.nick}: O hej {self.nick}! Co tam?")
            print(f"{self.nick}: Pozwól, że przekażę Ci moją wiedzę ...")
            print(f"{osoba.nick}: Ok słucham!")
            Student.__czekanko(3)

            # wymiana wiedzy
            self.__nauczSie(osoba.wiedza)
            osoba.__nauczSie(self.wiedza)

            # podziekowanie
            print(f"{osoba.nick}: Wow!!! Dzięki {self.nick}! To było wspaniałe!")
            print(f"{self.nick}: No problemo {osoba.nick}!")
            
        
# Demonstracja stanu - Uwaga! Uruchom kilka razy, bo student może czasem być martwy :) :(
stud1 = Student("Baltazar")
stud1.coSlychac()
stud1.śpij()
stud1.coSlychac()
stud1.obudźSię()
stud1.coSlychac()
stud1.uczSię() 
stud1.coSlychac()
# stud1.uczSię() # odkomentuj tą i następne 5 linijek, jesli chcesz zobaczyc czym grozi przepracowanie
# stud1.coSlychac()
# stud1.uczSię()
# stud1.coSlychac()
# stud1.uczSię()
# stud1.coSlychac()
stud1.spotkajPrzyjaciół()
stud1.coSlychac()

# dwoch studentow wymienia sie wiedzą
stud1.powiedzCoUmiesz()
stud2 = Student("Hierofant", {"ping-pong", "mechanika kwantowa"})
stud2.coSlychac()
stud2.powiedzCoUmiesz()
stud1.porozmawiajZ(stud2)
stud1.powiedzCoUmiesz()
stud2.powiedzCoUmiesz()

# dochodzi trzeci student ...
stud3 = Student("Kentucky", {"liczby urojone", "udon", "historia sztuki"})
stud3.powiedzCoUmiesz()

# ... i wymienia się wiedzą z pozostałymi dwoma
stud3.porozmawiajZ(stud1)
stud1.powiedzCoUmiesz()
stud2.powiedzCoUmiesz()
stud3.powiedzCoUmiesz()

stud3.porozmawiajZ(stud2)
stud1.powiedzCoUmiesz()
stud2.powiedzCoUmiesz()
stud3.powiedzCoUmiesz()
