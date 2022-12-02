## ZADANIA NA ZAJĘCIA nr 7 (1.12.2022)

### ŁATWE

1. **Circle** 

Napisz klasę opisującą koło. Koło powinno mieć atrybut instancji `promień` oraz dwie metody: `obliczObwod` - przyjmująca promień i zwracająca obwód koła, `obliczPole` - przyjmująca promień i zwracająca pole koła.

W programie zademonstruj działanie klasy tworząc conajmniej dwie różne instancje klasy `Circle`.

Liczbę `pi` zaimportujesz z modułu math.


2. **Kalkulator**

Napisz klasę implementującą działanie kalkulatora. 

Instancja klasy przechowuje dwie liczby **zmiennoprzecinkowe** zainicjalizowane w konstruktorze klasy. Klasa posiada cztery metody każda pozwala obliczyć wynik jednej z cztereach operacji: `+`, `-`, `*`, `/`, odpowiadającym dodawaniu, odejmowaniu, mnożeniu i dzieleniu. 

W programie zademonstruj działanie klasy.


3. **Pracownik**

Napisz klasę `Pracownik` opisującą następujące dane przykładowego pracownika: imię, nazwisko, miesięczną pensję.

Zademonstruj działanie klasy tworząc conajmniej dwie różne instancje klasy Pracownik.



### TRUDNIEJSZE

4. **Firma**

Napisz implementację klasy `Pracownik` z zadania nr 3. 

Następnie zaprojektuj klasę `Firma` w taki sposób aby przechowywała listę pracowników (listę instancji klasy Pracownik). 

Wyposaż klasę w metodę pozwalającą na zatrudnianie i zwalnianie pracowników (dodawanie/usuwanie z listy instancji klasy `Pracownik`). 
Klasa powinna również zawierać metodę obliczającą łączny wydatek jaki miesięcznie ponosi firma zatrudniając swoich pracowników.

Zademonstruj działanie klasy odpowiednimi przykładami.


5. **Wymiana wiedzy**

Zaprojektuj klasę `Student` z następującymi atrybutami:
  
  * `nick`
  * `stan` (ogranicz liczbę możliwych stanów do następujących: "śpi", "szczęśliwy", "zmęczony", "wczorajszy") 
  * `wiedza` (zbiór w przykładowej instancji mógłby być np. taki: {'magia ognia', 'psychologia', 'ping-pong', 'programowanie'} - UWAGA! Powinien być to **zbiór** czyli zmienna typu `set` a nie lista, by elementy nie mogły się powtarzać!)

oraz następującymi metodami zmieniającymi stan studenta na inny (wg uznania):
  
  * `śpij`
  * `obudź się`
  * `ucz się`
  * metodę pozwalającą stać się szczęśliwym (nazwij ją jak chcesz, w zależności od tego co sprawia Ci radość :)  
  * specjalną metodę, która przyjmie na wejściu innego studenta i sprawi, że studenci wymienią się swoją wiedzą, tj. zbiór wiedzy każdego z nich zostanie poszerzony o nowe elementy, których nie umiał a nauczył się od swojego rozmowcy 

