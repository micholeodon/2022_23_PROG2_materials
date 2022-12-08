## ZADANIA NA ZAJĘCIA nr 8 (9.12.2022)

1. **Pisząca papuga**

Program ktory wyświetla na ekranie i jednocześnie zapisuje do pliku to co mu poda użytkownik (input). 
Użytkownik może przerwać działanie programu pisząc "END" i wciskając ENTER.

2. **Zabawa plikami**

Niech program wykona poniższe czynności w podanej kolejności:

1. Utworzy dwa katalogi o nazwach: `pierwszy`, `drugi`, 
1. Utworzy nowy plik tekstowy o nazwie `dane.csv` w katalogu gdzie znajduje się skrypt
1. Zmieni nazwę wybranego pliku na `data.csv`
1. Przeniesie plik `data.csv` do katalogu `pierwszy`
1. Skopiuje ten plik do katalogu `drugi`
1. Wpisze losową liczbę do pliku `pierwszy/data.csv`
1. Wpisze **inną** losową liczbę do pliku `drugi/data.csv`
1. Usunie katalog `pierwszy` wraz z zawartością (najpierw plik, potem katalog)
1. Zmieni nazwę katalogu `drugi` na `pierwszy`
1. Odczyta zawartość pliku `pierwszy/data.csv` i wyświetli na ekranie

**UWAGA!** Przed każdorazowym uruchomieniem programu, w celu uniknięcia błędów, można **ręcznie** usunąć tworzone pliki i katalogi. 

3. **Bajzel #1**

Napisz program, który:

 * policzy liczbę katalogów i plików w katalogu `bajzel` (łącznie z tymi w obecnych podkatalogach). 

*Poprawna odpowiedź*: 2 katalogi, 355 plików.

 **Uwaga!** Dla uproszczenia dopuszczam program bez rekurencji, czyli żeby sprawdzał jeden poziom podkatalogów wgłąb.
 
 Katalog `bajzel` znajduje się w pliku do pobrania i rozpakowania `bajzel.zip`.

4. **Bajzel #2**

Napisz program, który:

  * Przeszuka katalog `bajzel` w poszukiwaniu plików o rozszerzeniu `.csv` 
  * Wyświetli liczbę tych plików (wraz z tymi w podkatalogach, bez rekurencji - patrz poprzednie zadanie), listę znalezionych plików `.csv` wraz z ich względnymi scieżkami dostępu. 
	
	
**UWAGA!** Może się przydać funkcja `append` wbudowana w każdą listę.

 Katalog `bajzel` znajduje się w pliku do pobrania i rozpakowywania `bajzel.zip`.

*Poprawna odpowiedź*: program powinien znaleźć 126 plików CSV.
