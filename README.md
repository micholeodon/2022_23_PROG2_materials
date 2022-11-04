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


### SPOTKANIE nr 3 (4.11.2022)

4. **Komputer zgaduje liczbę** (PRACA DOMOWA)

W tym zadaniu to komputer ma za zadanie zgadnąć liczbę, którą sobie pomyślisz. 
Użytkownik podaje komputerowi górną granicę przeszukiwania czyli wartość zmiennej `N`. 
Następnie, komputer podaje zaczyna zgadywać. Użytkownik odpowiada czy podana przez komputer liczba jest za duża, za mała, czy zgadł. Trwa to, do momentu aż komputer zgadnie.
Zastosuj poznaną na zajęciach strategię bisekcji (dzielenia na pół).
