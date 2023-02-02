# I. Typy

1. **Benzyna**


Jedziesz z Torunia do Poznania (187 km). Ile benzyny musisz zatankować,
jeśli Twój samochód spala średnio 7 litrów benzyny na 100 km? Ile
zapłacisz za potrzebną do przejazdu benzynę (6.65 zł / litr)? Napisz
prosty program, który odpowie na postawione pytania.

2. **Wielomian kwadratowy**


Napisz program, który oblicza wartość wielomianu
$a_2 x^2 + a_1 x + a_0$. Program prosi użytkownika o
podanie wartości współczynników $a_0, a_1, a_2$. Na końcu
użytkownik podaje wartość $x$, a program liczy i wyświetla wartość
wielomianu dla podanego $x$.

3. **Dzielenie łańcucha**

Dzielenie łańcucha wg separatora. Użytkownik podaje łańcuch składający
się z pięciu elementów oddzielonych przecinkiem bez spacji, a program
zaspisuje je do pięcioelementowej krotki (5-tuple). Użyj funkcji `split`.

4. **Słownik**


Napisz słownik, który dla każdej z planet poniżej przechowa Twoj ciężar
wyrażony w kg, jaki pokazałaby waga, gdybyś ważył się na danej planecie.
Kluczami powinny być nazwy planet, a wartościami waga wyrażona w
kilogramach.

1kg na Ziemi \"waży\":

-   0.1655 kg na Księżycu
-   0.3985 kg na Marsie
-   0.9032 kg na Wenus
-   1.1390 kg na Saturnie
-   2.6400 kg na Jowiszu
-   27.9000 kg na Słońcu

Sprawdź działanie programu dla wypisując wartości na ekranie dla trzech
wybranych planet, np:

```
mojaWaga["Ziemia"] = 77.5 
mojaWaga["Księżyc"] = 12.82625
mojaWaga["Słońce"] = 2162.25
```

# II. Flow (if, while, for)

1. **Dowolny wielomian**


Napisz program, który oblicza wartość wielomianu
$a_n x^n + a_{n-1} x^{n-1} + ... a_3 x^3 + a_2 x^2 + a_1 x + a_0$.
Użytkownik podaje liczbę $n \geq 0$. Program sprawdza czy liczba jest
nieujemna. Następnie prosi użytkownika o podanie wartości współczynników
$a_0, a_1, ..., a_n$. Na końcu użytkownik podaje wartość $x$, a program
liczy i wyświetla wartość wielomianu.

2. **Silnia**


Napisz program, do którego użytkownik podaje liczbę nieujemną `n`, a program
liczy jego silnię, tj.
$n! = 1 \cdot 2 \cdot 3 \cdot ... \cdot (n-1) \cdot (n-2)$. Program
powinien sprawdzać, czy podana liczba jest nieujemna.


3. **How I flirt**

Napisz program, który zada użytkownikowi serię pytań, podsumuje wybrane
przez niego odpowiedzi, a następnie doradzi, wg schematu na rysunku `how_i_flirt.png`

Przykładowe wyjście: 

```
You see a guy. Is he looking at you? Yes 
Is he cute? Yes.
Ok ... so you see a guy, he is looking at you, and he is cute. 
Avoid eye contact!
```


# III. Funkcje


1. **Liczby pierwsze**


Napisz metodę, która sprawdza czy liczba naturalna podana jako argument
do funkcji jest liczbą pierwszą.

2. **Ciąg arytmetyczny**


Napisz funkcję zwracającą w postaci 2-krotki (tuple) n-ty wyraz ciągu
arytmetycznego i sumę n-pierwszych wyrazów tego ciągu. Funkcja przyjmuje
trzy argumenty: $n$, $a_0$ (pierwszy wyraz tego ciągu) i $r$ (różnicę ciągu).

3. **Urodziny**


Napisz funkcję wyświetlającą na ekranie życzenia urodzinowe zawierające
imię solenizanta i wiek na podstawie dwóch argumentów metody:
imienia oraz roku urodzenia. Dla uproszczenia przyjmij, że funkcja
oblicza wiek zawsze względem roku 2023 (tj. wynik będzie ten sam gdy uruchomisz program dziś i za 100 lat).

4. **Plansza X-O**

Napisz funkcję, która wyświetla w konsoli planszę do gry w kółko i
krzyżyk na podstawie zawartości 9-elementowej listy, która zawiera
elementy \'X\' lub \'O\'.

# IV. Klasy


1. **Bity**

Napisz klasę, która zamienia liczbę w postaci binarnej, na postać
dziesiętną.

2. **Bity 2**

Napisz klasę, która zamienia liczbę w postaci dziesiętnej, na postać
binarną.

3. **Wektory2D**

Napisz klasę `Wektor2D`, która opisuje wektor o dwóch współrzędnych. Klasa
implementuje metody obliczania długości wektora, dodawania dwóch
wektorów, obliczania iloczynu skalarnego dwóch wektorów i obliczania
cosinusa kąta między dwoma wektorami.


4. **Rozmowa z kosmitami**

Napisz dwie klasy: `Player` i `Alien`. `Player` powinien implementować metodę
`zagadaj()`, która sprawia, że podana do niej jako argument instancja
klasy `Alien` opowiada coś o sobie. Klasa `Alien` powinna implementować
metodę `talk()` wywoływaną w momencie zagadania kosmity.


# V. Praca z plikami

1. **Odczyt**

Napisz program odczytujący plik linia po linii, powracający do początku
otwartego pliku i wypisujący to jeszcze raz (w ramach JEDNEGO otwarcia
pliku).


2. **Kopiowanie**

Napisz program kopiujący zawartość wskazanego pliku do innego pliku.


3. **Losowe liczby w pliku**

Napisz program, który do pliku zapisze $N$ wygenerowanych liczb losowych z
przedziału $\[A, B\]$. Nazwę pliku wynikowego oraz wartości $A$, $B$, i $N$
podaje użytkownik.


4. **Prostokąt**

Napisz program, który obliczy pole prostokąta, którego współrzędne $x,y,z$
wierzchołków są podane w pliku CSV. Odległość między dwoma punktami $A$ i $B$
liczona jest ze wzoru:

$$d(A,B) = \sqrt{(x_A-x_B)^2 + (y_A-y_B)^2 + (z_A-z_B)^2}$$


5. **Medyczna baza danych**

Załóżmy, że istnieje pewien plik przechowujący następujące informacje:
nazwisko (nie dłuższe niż 20 znaków), imię (nie dłuższe niż 20 znaków),
następnie umieszczona jest liczba całkowita określająca wiek a następnie
dwie liczby rzeczywiste określające wzrost i wagę. Np.: 

```
Harry Potter 33 182.5 80.5 
```
Napisz program, który:

-   Wyświetli na ekranie w kolejnych liniach imię, nazwisko i współczynnik masy ciała BMI każdego badanego. Dla pacjentów z nadwagą lub niedowagą wyświetlany jest dodatkowo komunikat o przekroczeniu normy.
-   Wyświetli wpisy w porządku rosnącej wagi ciała
-   Wyświetli wpisy w porządku alfabetycznym względem nazwisk
-   Wyznaczy średni wzrost dla wszystkich pacjentów powyżej 30. roku życia

Do sortowania może przydać się funkcja `argsort` z modułu `numpy`.

Współczynnik BMI liczony jest na podstawie wzrostu $h$ wyrażonego w metrach i masy ciała $m$ wyrażonej w kilogramach:

$$\text{BMI} = \frac{m}{h^2} \qquad \big[\frac{kg}{m^2}\big]$$

6. **Szyfr Cezara** 

Napisz program, który odczytuje tekst z pliku i zapisuje nowy plik z tym samym tekstem zaszyfrowany metodą Cezara. Program prosi użytkownika o podanie liczby nieujemnej $N$ będącej przesunięciem.


7. **Rozszerzenia**

Napisz program wypisujący rozszerzenia wszystkich plików znajdujących
się w dowolnie wybranym katalogu. Wybrany katalog może być wpisany jako
zmienna w kodzie (użytkownik programu nie musi podawać tej ścieżki).

8. **Kody osób badanych**

Napisz program, który stworzy katalogi dla osób badanych, których dane znajdują się w pliku `badani.csv`. Nazwami katalogów powinny być kody osób badanych utworzone w następujący sposób: 

-  badany o imieniu `Michał`, nazwisku `Kowalski`, roku urodzenia `2003` otrzymuje kod `KOMI003`, 
-  badana o imieniu `Anna`, nazwisku `Nowak`, roku urodzenia `1999` otrzymuje kod `NOAN999`.


9. **Bajzel \#1.**

Napisz program, który:

-   policzy liczbę katalogów i plików w katalogu `bajzel` (łącznie z tymi
    w obecnych podkatalogach). Poprawna odpowiedź: 2 katalogi, 355
    plików.
-   Uwaga! Dla uproszczenia dopuszczam program bez rekurencji, czyli
    żeby sprawdzał jeden poziom podkatalogów wgłąb.
-   Katalog `bajzel` znajduje się w pliku do pobrania i rozpakowania
    `bajzel.zip`.

10. **Bajzel \#2.**

Napisz program, który:

-   Przeszuka katalog bajzel w poszukiwaniu plików o rozszerzeniu `.csv`
-   Wyświetli liczbę tych plików (wraz z tymi w podkatalogach, bez
    rekurencji - patrz poprzednie zadanie), listę znalezionych plików
    `.csv` wraz z ich względnymi scieżkami dostępu.
-   UWAGA! Może się przydać funkcja append wbudowana w każdą listę.
-   Katalog bajzel znajduje się w pliku do pobrania i rozpakowywania
    `bajzel.zip`.
-   Poprawna odpowiedź: program powinien znaleźć 126 plików CSV.
