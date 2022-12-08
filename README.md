# 2022_23_PROG2_materials


## Zadania domowe

### SPOTKANIE nr 2 (21.10.2022)

1. **Znajdź x**. Program ma znajdować rozwiązanie równania `ax + b = c`. Parametry `a`, `b`, `c` podaje użytkownik. Program niech działa następująco:
    - Wyświetli tekst "ax + b = c"
    - Poprosi użytkownika o podanie liczb a, b, c.
    - Wyświetli równanie "ax + b = c" z podstawionymi wartościami liczbowymi
    - Program oblicza wartość x
    - Wyświetli wynik 


### SPOTKANIE nr 3 (28.10.2022)

1. **Kalkulator**. Program pozwala na wprowadzenie dwóch liczb **zmiennoprzecinkowych** oraz wybrania jednej z cztereach operacji: `+`, `-`, `*`, `/`, odpowiadającym dodawaniu, odejmowaniu, mnożeniu i dzieleniu. Program oblicza wynik operacji wykonanej na dwóch podanych przez użytkownika liczbach.

	Schemat działania:

    * Program prosi o podanie pierwszej liczby,
    * Program prosi o podanie drugiej liczby,
    * Program pokazuje jakie operacje są do wyboru i prosi o wybranie jednej z nich,
	* W przypadku podania nieprawidłowej operacji, program informuje o tym fakcie użytkownika i kończy się lub pozwala na ponowny wybór operacji, aż do skutku,
	* Program następnie wypisuje na ekranie jakie działanie rozwiązuje i podaje wynik tego działania, po czym kończy działanie.


2. **Pogoda**. Plik `czyPada.png` przedstawia schemat blokowy postępowania w przypadku deszczowej pogody. W zależności od zmiennych logicznych `czyPada` oraz `czyParasol` program powinien zachowywać się wg schematu. Po uruchomieniu program powinien wypisać na ekranie coś podobnego do przykładu poniżej:

```
    Czy pada (1) czy nie pada (0)? 1
    A masz parasol (1) czy nie masz (0)? 0
    Poczekaj chwile ...
    Poczekaj chwile ...
    Wyjdź na zewnątrz.
```	

Długość oczekiwania możesz uzależnić od losowej jakiejś losowej wartości. W tym celu przydać się może znajomość funkcji `random.choice()`.

3. **Menu / Rozmowa**. Wykorzystując funkcję `while` oraz inne znane Ci mechanizmy języka Python, spróbuj zaprogramować przykładowe menu (przykładowo to co dzieje się kiedy wchodzisz w ustawienia swojego telewizora / monitora), tj. przedstaw użytkownikowi wybór jednej z kilku opcji. Po wyborze, przedstaw kolejny wybór itd. Nie ma zadanej liczby poziomów tego menu. Zaprogramuj też możliwość powrotu do poprzedniego poziomu.

Alternatywnie, możesz zasymulować dialog z wirtualną postacią.


### SPOTKANIE nr 4 (4.11.2022)

4. **Komputer zgaduje liczbę** (PRACA DOMOWA)

W tym zadaniu to komputer ma za zadanie zgadnąć liczbę, którą sobie pomyślisz. 
Użytkownik podaje komputerowi górną granicę przeszukiwania czyli wartość zmiennej `N`. 
Następnie, komputer podaje zaczyna zgadywać. Użytkownik odpowiada czy podana przez komputer liczba jest za duża, za mała, czy zgadł. Trwa to, do momentu aż komputer zgadnie.
Zastosuj poznaną na zajęciach strategię bisekcji (dzielenia na pół).


### SPOTKANIE nr 7 (1.12.2022)

5. **Roma** (łatwe)

Zaprojektuj klasę przyjmującą liczbę całkowitą z zakresu 1-20 i zamieniająca je na liczbę zapisaną cyframi rzymskimi.

Wskazówka: nagródź się dziś po arabsku lub po rzymsku: dobrą kawą lub herbatką lub pizzą  ;)

6. **Tamagotchi** (trudniejsze)

Tamagochi było niegdyś bardzo popularną zabawką - https://pl.wikipedia.org/wiki/Tamagotchi

Zaprojektuj klasę `Zwierzątko` modelującą zachowanie wirtualnego zwierzątka, o które trzeba dbać - karmić by nie było głodne, bawić się z nim by miało dobry humor :)
Zwierzątko powinno mieć swoje unikalne imię, stan i umieć powiedzieć jak się czuje.

Zademonstruj działanie klasy na conajmniej dwóch instancjach. 

Użytkownik wchodzi w interakcję z wybranym zwierzątkiem za pomocą prostego menu.

### SPOTKANIE nr 8 (9.12.2022)

7. **Filmoteka** (łatwe)

Program zapisujący dane wprowadzane przez użytkownika do pliku w formacie CSV - https://pl.wikipedia.org/wiki/CSV_(format_pliku)

1. Program prosi o podanie liczby rekordów (czyli wierszy do wpisania w pliku)
1. Następnie prosi użytkownika o podanie dwóch rzeczy: nazwy filmu, a następnie wartość liczbową oceny w skali od 1.0 - 10.0 
1. Prośba jest powtarzana tyle razy ile ma być rekordów
1. Wpisane dane są zapisywane do pliku filmy.csv 
1. Na końcu wyświetlana jest zawartość pliku
1. Przykładowa zawartość pliku:

```
L.p.,Tytuł_filmu,Ocena
1,Incepcja,8.3
2,Room,2.9
3,Matrix,7.6
4,Pianista,8.3
5,Diuna,7.7
6,Paterson,7.1
```
Zwróć uwagę na nagłówek (pierwszy wiersz w pliku)!

Dla sprawdzenia, stworzony plik możesz otworzyć w Excelu lub LibreOffice Calc by sprawdzić czy plik po otwarciu dobrze wpasuje się komórki arkusza kalkulacyjnego.



6. **UczSie!** (trudniejsze)

Program, który pomaga w powtarzaniu materiału do nauki.

Użytkownik może przygotować własny zestaw pytań i poprawnych odpowiedzi w pliku tekstowym.
Na każde pytanie powinna istnieć jedna poprawna odpowiedź. Zaletą programu jest uniwersalność - każdy może stworzyć swoje zestawy pytań w osobnych plikach (każdy plik to np. inny przedmiot) i wybierać z czego być odpytywanym w zależności od potrzeb :)

Program powinien:

1. Poprosić użytkownika o podanie nazwy pliku z pytaniami, który ma zostać wczytany.
1. Wczytać wskazany plik tekstowy
1. Poprosić użytkownika o podanie liczby pytań jaka ma być mu zadana
1. Zadać **losowo** wybrane pytanie z listy pytań z pliku
1. Poprosić o podanie odpowiedzi
1. Sprawdzić czy odpowiedź poprawna. 
1. Jeśli odpowiedź jest poprawna: dodać punkt za poprawną odpowiedź, 
1. Jeśli odpowiedź nie jest poprawna: zdradzić jaka jest poprawna odpowiedź.
1. Po zadaniu określonej przez użytkownika liczbie pytań powinno wyświetlić się podsumowanie. Podsumowanie powinno zawierać następujące elementy: liczbę zadanych pytań, liczbę poprawnych odpowiedzi, procent poprawnych odpowiedzi i (opcjonalnie) wskazanie pytań na które została udzielona zła odpowiedź wraz z podaniem poprawnej odpowiedzi.


