import os, sys

os.chdir(sys.path[0])

os.chdir("bajzel")
print(os.getcwd()) # upewniam sie ze jestem we wlasciwym katalogu

# listuje pliki i katalogi obecne w katalogu bajzel
lista = os.listdir()

liczbaPlikowCSV = 0
listaSciezekCSV = [] # pusta lista do ktorej bede "appendowal" sciezki

# sprawdzam kazdy element w katalogu bajzel
for sth in lista:

    # identyfikacja - czy ten element to katalog ...
    if os.path.isdir(sth):

        # listuje elementy w znalezionym podkatalogu katalogu bajzel
        lista2 = os.listdir(sth)

        # sprawdzam kazdy element
        for sth2 in lista2:
            ext = os.path.splitext(sth2)[1] # jakie ma rozszerzenie
            if ext.lower() == ".csv": 
                listaSciezekCSV.append(os.path.join(sth,sth2)) # jesli .csv to appenduje sciezke do tego pliku
        
    # ... czy plik
    elif os.path.isfile(sth):
        ext = os.path.splitext(sth)[1] # sprawdzam rozszerzenie
        if ext.lower() == ".csv": 
            listaSciezekCSV.append(sth) # jesli .csv to appenduje sciezke do tego pliku
    else:
        pass

# zliczanie
liczbaPlikowCSV = len(listaSciezekCSV) # licze ile plikow .csv jest na liscie
print(f"Liczba znalezionych plikow CSV: {liczbaPlikowCSV}")

# wypisnie sciezki
print("Scieżki do znalezionych plików: ")
for sciezka in listaSciezekCSV:
    print(sciezka)