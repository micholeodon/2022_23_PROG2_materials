from os import name, system, path
from time import sleep
import csv
from random import randint

################################################################################
# FUNKCJE GLOBALNE
################################################################################

def clear():
    '''Funkcja "kosmetyczna" służąca do czyszczenia ekranu konsoli. '''

    if name == "nt":
        system("cls")
    else:
        system("clear")


def waitForEnter():
    '''Funkcja służąca do czekania aż użytkownik da znać,
    że jest gotowy kontynuować poprzez wciśnięcie klawisza ENTER.'''

    input("Wciśnij ENTER ...")


def splashScreen():
    '''Funkcja wyświetlająca logo programu przy jego uruchomieniu.'''

    clear()

    title = '''\
             ___           ___           ___                    ___                       ___              
            /\  \         /\__\         /\__\                  /\__\                     /\__\             
            \:\  \       /:/  /        /::|  |                /:/ _/_       ___         /:/ _/_            
             \:\  \     /:/  /        /:/:|  |               /:/ /\  \     /\__\       /:/ /\__\           
         ___  \:\  \   /:/  /  ___   /:/|:|  |__            /:/ /::\  \   /:/__/      /:/ /:/ _/_          
        /\  \  \:\__\ /:/__/  /\__\ /:/ |:| /\__\          /:/_/:/\:\__\ /::\  \     /:/_/:/ /\__\         
        \:\  \ /:/  / \:\  \ /:/  / \/__|:|/:/  /          \:\/:/ /:/  / \/\:\  \__  \:\/:/ /:/  /         
         \:\  /:/  /   \:\  /:/  /      |:/:/  /            \::/ /:/  /   ~~\:\/\__\  \::/_/:/  /          
          \:\/:/  /     \:\/:/  /       |::/  /              \/_/:/  /       \::/  /   \:\/:/  /           
           \::/  /       \::/  /        |:/  /                 /:/  /        /:/  /     \::/  /            
            \/__/         \/__/         |/__/                  \/__/         \/__/       \/__/             \n'''
        
    print(title)

################################################################################
# KONIEC FUNKCJI GLOBALNYCH
################################################################################


################################################################################
# KLASA NAUCZYCIELA
################################################################################
class Nauczyciel:

    def __init__(self):
        self.file = ""
        self.numOfQuestionsToAsk = 0
        self.numCorrect = 0
        self.questions = []
        self.answers = []
        
    def loadQuestionsAndAnswers(self):
        '''Funkcja wczytująca pytania i odpowiedzi, 
        pod warunkiem, że plik ma poprawną zawartość.'''

        if self.file == "":
            print("BŁĄD! Nie załadowano pliku. Najpierw skorzystaj z opcji 'Wczytaj plik'.")
            sleep(2)
            return False

        with open(self.file, 'r') as csvinput:
            reader = csv.reader(csvinput)
            
            self.questions = [] # clear previously loaded questions
            self.answers = [] # clear previously loaded answers
            for row in reader:

                if len(row) < 2 or len(row) > 2:
                    print("BŁĄD! Niepoprawny format pliku. Przeczytaj 'Pomoc'.") 
                    sleep(2)
                    return False

                question, answer = row[0], row[1]

                self.questions.append(question)
                self.answers.append(answer)

        numQuestionsAvailable = len(self.questions)
        print(f"Poprawnie załadowano {numQuestionsAvailable} pytań.")
        sleep(1)
        return True


    def exam(self):
        '''Funkcja przeprowadzająca proces odpytywania.'''

        self.numCorrect = 0
        self.numOfQuestionsToAsk = int(input("Podaj liczbę pytań do zadania: "))
        numQuestionsAvailable = len(self.questions)

        for iDraw in range(self.numOfQuestionsToAsk):
            clear()
            splashScreen()
            
            iQuestion = randint(0, numQuestionsAvailable-1)
            
            question = self.questions[iQuestion]
            correctAnswer = self.answers[iQuestion]

            print(f"Pytanie {iDraw+1} z {self.numOfQuestionsToAsk}:")
            print(question)
            odp = input("Odp.: ")

            if(odp == correctAnswer):
                print("(^_^) Poprawna odpowiedź!")
                self.numCorrect += 1
            else:
                print("(T_T) Niepoprawna odpowiedź!")
                print(f"Poprawna odpowiedź to: {correctAnswer}")

            sleep(2)

        print("Koniec testu.")
        

    def presentScore(self):
        '''Funkcja wyświetlająca wynik odpytywania.'''
        print("Oto wyniki: ")
        percentCorrect = self.numCorrect/self.numOfQuestionsToAsk*100
        print(f"Poprawnych odpowiedzi: {self.numCorrect} / {self.numOfQuestionsToAsk} ({percentCorrect} %)")

################################################################################
# KONIEC KLASY NAUCZYCIELA
################################################################################


################################################################################
# KLASA MENU
################################################################################
class UczSieMenu:

    def __init__(self):
        self.nauczyciel = Nauczyciel()
        pass


    def endProgram(self):
        '''Funkcja wykonująca działania przewidziane na zakończenie programu.'''
        
        clear()
        splashScreen()
                
        print("Dziękuję za skorzystanie z programu :) \n \
            Do zobaczenia!")
        sleep(2)
        

    def loadFile(self):
        '''Funkcja prosząca użytkownika o podanie pliku do załadowania.'''
        
        odp = input("Podaj nazwę pliku do wczytania: ") 

        if not path.exists(odp):
            print("BŁĄD! Nie ma takiego pliku!")
            sleep(2)
            return ""
        if not path.isfile(odp):
            print("BŁĄD! Podany element nie jest plikiem!")
            sleep(2)
            return ""
        
        loadedFile = odp
        return loadedFile


    def help(self):
        '''Funkcja wyświetlająca instrukcje jak przygotować plik do nauki 
        i jak korzystać z programu.'''
        
        helpLines = [
"""UŻYWANIE PROGRAMU""",

"""Program UczSie! pozwala na samodzielne odpytywanie siebie ze
wskazanego przez użytkownika materiału do nauki""",

"""Najpierw należy skorzystać z opcji '1. Wczytaj plik'.
Użytkownik zostanie poproszony o podanie ścieżki względnej do pliku 
zawierającego materiał do nauki (wskazówki nt. przygotowania
takiego pliku zostaną omówione dalej.)""",

"""Jeśli wskazana ścieżka nie prowadzi do pliku, nastąpi powrót do
głownego menu.""",

"""Po poprawnym wskazaniu pliku, należy użyć opcji '2. Ucz się!'.""",

"""Zostanie sprawdzona poprawność pliku.""",

"""Jeśli plik jest poprawny, użytkownik zostanie poproszony 
o podanie liczby pytań do wylosowania.""",

"""Następnie użytkownik odpowiada na serię pytań.""",

"""Na każde pytanie jest jedna poprawna odpowiedź.""",

"""Pytania mogą się powtarzać.""",

"""Wielkość liter w odpowiedzi MA znaczenie.""",

"""Po przejściu przez zadaną liczbę pytań wyświetlane jest 
podsumowanie: liczba i procent poprawnych podpowiedzi.""",

"""Potem następuje powrót do głównego menu i użytkownik może:
- przeegzaminować się jeszcze raz z wykorzystaniem tego samego pliku,
- wczytać inny plik do nauki,
- wyjść z programu.""",

"""PLIKI Z PYTANIAMI - WSKAZÓWKI""",

"""Użytkownik może przygotować więcej niż jeden plik do nauki.""",

"""Każdy plik musi zawierać dwie kolumny danych BEZ NAGŁÓWKA
oddzielone PRZECINKIEM (tzw. format CSV), tzn.:

pytanie1,odp1
pytanie2,odp2
pytanie3,odp3

Przykład poniżej:
""",

"""
Ile księżyców krąży wokół Ziemii?,3
Kto był pierwszym władcą Polski?,Mieszko I
Podaj wzór na pole prostokąta.,P=ab
""",

"""Ważne wskazówki:
- W każdym wierszu pliku musi wystąpić DOKŁADNIE JEDEN przecinek, który oddziela
  pytanie od odpowiedzi.
- Po przecinku NIE MOŻE pojawić się spacja.
- Liczba wierszy w pliku jest jednocześnie liczbą możliwych pytań, 
  spośród których następuje losowanie.
"""


"""
KONIEC POMOCY
"""
        ]

        for line in helpLines:
            print(line)
            print()
            waitForEnter()
            clear()
            splashScreen()
    

        # instrukcja przygotowania pliku

        # opcja 3: pomoc
        #  - wyswietlenie instrukcji przygotowania pliku
        #  - powrot do glownego menu po wcisnieciu ENTER 


    def mainMenu(self):
        '''Funkcja wyświetlająca i obsługująca główne menu programu.'''
        
        
        while True:
            try:

                clear()
                splashScreen()

                print(f"[Obecnie wczytany plik: {self.nauczyciel.file}]\n")
                print("1. Wczytaj plik ")
                print("2. Ucz się! ")
                print("3. Pomoc ")
                print("4. Wyjdź ")

                odp = input("Wybierz opcję 1-4: ")

                clear()
                splashScreen()

                if odp not in {"1", "2", "3", "4"}:
                    print("NIEPOPRAWNA OPCJA! Spróbuj ponownie.")
                    sleep(2)
                    continue

                if odp == "1": # Wczytanie pliku
                    self.nauczyciel.file = self.loadFile()
                    
                    if self.nauczyciel.file == "":
                        continue
                    
                if odp == "2": # Ucz Się!
                    if(self.nauczyciel.loadQuestionsAndAnswers()):
                        clear()
                        splashScreen()
                        self.nauczyciel.exam()

                        clear()
                        splashScreen()
                        self.nauczyciel.presentScore()
                        waitForEnter()

                if odp == "3": # Wyświetlenie pomocy
                    self.help()

                if odp == "4": # Wyjście z programu
                    self.endProgram()
                    break
            except:
                print("WYSTĄPIŁ BŁĄD! Następuje powrót do głównego menu ...")
                sleep(2)

################################################################################
# KONIEC KLASY MENU
################################################################################