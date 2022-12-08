import os, sys

os.chdir(sys.path[0])
os.chdir("bajzel") # upewniam sie ze jestem we wlasciwym katalogu
print(os.getcwd())

# listuje pliki i katalogi obecne w katalogu bajzel
lista = os.listdir()

liczbaPlikow = 0
liczbaKatalogow = 0
for sth in lista:
    # identyfikacja - czy katalog ...
    if os.path.isdir(sth):
        liczbaKatalogow += 1

        lista2 = os.listdir(sth) # listuje elementy w znalezionym podkatalogu katalogu bajzel
        liczbaPlikow += len(lista2) # zakladam ze nie ma kolejnych podkatalogow

    # ... czy plik
    elif os.path.isfile(sth):
        liczbaPlikow += 1
    else:
        pass

print(f"Liczba znalezionych katalogow: {liczbaKatalogow}")
print(f"Liczba znalezionych plikow: {liczbaPlikow}")
