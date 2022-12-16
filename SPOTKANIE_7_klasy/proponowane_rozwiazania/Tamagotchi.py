import random

class Zwierzak:

    __mozliweHumory = ['nieszczesliwy', 'szczesliwy'] 

    def __init__(self, imie):
        self.imie = imie
        self.humor = random.choice(Zwierzak.__mozliweHumory)
        self.nasycenie = 3 # utrzymywac miedzy 1 a 5 by przezyc
        self.energia = 5 # utrzymywac miedzy 1 a 5 by przezyc
        self.czyZyje = True

        print(f"[ Narodził się nowy Zwierzak - {self.imie}! ]")

    def powiedzJakSieMasz(self):
        
        if not self.czyZyje:
            self.__czynnosciPosmiertne()
            return

        print(f"- {self.imie}: ", end="")
        if self.humor == Zwierzak.__mozliweHumory[0]:
            print("Jestem nieszczęśliwy ;(")
        else:
            print("Moje życie jest wspaniałe :):):)")

        if self.nasycenie > 4:
            print("Jestem bardzo najedzony. Nie zjem nic więcej.")

        if self.nasycenie < 2:
            print("Jestem głodny. Może coś zjemy?")

        if self.energia < 2:
            print("Czuję się zmęczony. Nic mi się nie chce.")


        self.__akcjaZaleznaOdStanu()


    def pobawSie(self):

        if not self.czyZyje:
            self.__czynnosciPosmiertne()
            return

        print(f"{self.imie}: Łiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!!!!!!!!!!!!!!")

        if self.humor == Zwierzak.__mozliweHumory[0]:
            self.humor = Zwierzak.__mozliweHumory[1]
        
        self.nasycenie -= 1 
        self.energia -= 1

        self.__akcjaZaleznaOdStanu()


    def nakarm(self):

        if not self.czyZyje:
            self.__czynnosciPosmiertne()
            return

        print(f"{self.imie}: OmNomNom!!!")


        self.nasycenie += 3

        self.__akcjaZaleznaOdStanu()


    def odpocznij(self):

        if not self.czyZyje:
            self.__czynnosciPosmiertne()
            return

        print(f"{self.imie}: ... ")

        self.nasycenie -= 1
        self.energia += 3

        self.__akcjaZaleznaOdStanu()

        
    def __umrzyj(self):
        self.czyZyje = False

    def __akcjaZaleznaOdStanu(self):
        # Ta metoda jest wykorzystywana po wykonaniu kazdej czynnosci

        # smierc glodowa
        if(self.nasycenie < 1):
            print(f"[ Zwierzak {self.imie} zdechł z głodu ... :( ]")
            self.__umrzyj()

        # smutek jesli glodny
        if(self.nasycenie < 3):
            self.humor = Zwierzak.__mozliweHumory[0]

        # dobry humor jesli zwierze syte
        if(self.nasycenie > 3):
            self.humor = Zwierzak.__mozliweHumory[1]
        
        if(self.nasycenie > 5):
            self.humor = Zwierzak.__mozliweHumory[0]

        # smierc z przejedzenia
        if(self.nasycenie > 6):
            print(f"[ Zwierzak {self.imie} zjad za dużo i zdechł... :( ]")
            self.__umrzyj()

        # smierc z braku energii
        if(self.energia < 1):
            print(f"[ Zwierzak {self.imie} stracił całą energię i zdechł ... :( ]")
            self.__umrzyj()

        # smutek jesli zbyt zmeczony
        if(self.energia < 3):
            self.humor = Zwierzak.__mozliweHumory[0]

        # limit na energie
        if(self.energia > 5):
            self.energia = 5

    def uplywCzasu(self):
        # ta metoda jest wywolywana po kazdym wyborze czynnosci przez uzytkownika (poza wybraniem zwierzaka)
        # "postarza" zwierzaka: zwierzak z czasem robi sie glodny, traci sily 
        # ta metoda jest tez wywolywana jesli uzytkownik jest zajety innym zwierzakiem!   
        
        if not self.czyZyje:
            return

        self.energia -= 1
        self.nasycenie -= 1

    def __czynnosciPosmiertne(self):
        ''' Ta funkcja bedzie sie wykonywala zawsze gdy uzytkownik bedzie 
        probowal cos zrobic gdy zwierzatko zdechlo'''

        print(f"[ Zwierzak {self.imie} nie zyje. Nic nie da się zrobić. ]")



def tworzenieZwierzaka(listaZwierzakow):
    imieZwierzaka = input("Podaj imie: ")
    zwierzak = Zwierzak(imieZwierzaka)
    listaZwierzakow.append(zwierzak)
    return
   
def menuZwierzaka(listaZwierzakow, nrWybranegoZwierzaka):
    # Podmenu [Zwierzaka]
    # - Powiedz jak sie masz
    # - Nakarm
    # - Pobaw sie
    # - Daj odpocząc
    # - WRÓĆ
    
    nrOstatniejOpcji = 5
    odp = '-1'
    while int(odp) != nrOstatniejOpcji:
        
        print("1. Powiedz jak się masz")
        print("2. Nakarm")
        print("3. Pobaw się")
        print("4. Daj odpocząć")
        print("5. WRÓĆ")
        
        print()
        odp = input("Wybierz opcję: ")

        if int(odp) == 1:
            listaZwierzakow[nrWybranegoZwierzaka].powiedzJakSieMasz()
        elif int(odp) == 2:
            listaZwierzakow[nrWybranegoZwierzaka].nakarm()
            listaZwierzakow[nrWybranegoZwierzaka].uplywCzasu()
        elif int(odp) == 3:
            listaZwierzakow[nrWybranegoZwierzaka].pobawSie()
            listaZwierzakow[nrWybranegoZwierzaka].uplywCzasu()
        elif int(odp) == 4:
            listaZwierzakow[nrWybranegoZwierzaka].odpocznij()
            listaZwierzakow[nrWybranegoZwierzaka].uplywCzasu()
                


def menuGłówne(listaZwierzaków):
    # MENU
    # - Stworz nowego Zwierzaka
    # - [Zwierzak 1]
    # - [Zwierzak 2]
    # - ...
    # - WYJDŹ Z GRY

    nrOstatniejOpcji = 2+len(listaZwierzakow)
    odp = '-1'
    while int(odp) != nrOstatniejOpcji:
        
        print("1. Stwórz nowego Zwierzaka")
        optNr = 2
        for zwierz in listaZwierzakow:
            print(f"{optNr}. {zwierz.imie}")
            optNr += 1
        
        print(f"{optNr}. WYJDŹ Z GRY")
        
        print()
        odp = input("Wybierz opcję: ")


        if int(odp) == 1:
            tworzenieZwierzaka(listaZwierzakow)
        elif int(odp) < nrOstatniejOpcji:

            nrWybranegoZwierzakaNaLiscie = int(odp) - 2
            menuZwierzaka(listaZwierzakow, nrWybranegoZwierzakaNaLiscie)

        nrOstatniejOpcji = 2+len(listaZwierzakow)

    pass

listaZwierzakow = []
menuGłówne(listaZwierzakow)
