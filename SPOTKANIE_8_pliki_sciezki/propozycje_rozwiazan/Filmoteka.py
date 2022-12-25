import os, sys

os.chdir(sys.path[0]) # upewniam sie ze jestem w katalogu gdzie znajduje sie ten skrypt


liczbaRekordowDoWpisania = int(input("Podaj liczbe rekordow: "))

wszystkieNazwy = []
wszystkieOceny = []

nrFilmu = 1
while liczbaRekordowDoWpisania > 0:
    nazwa = input(f"Podaj nazwe filmu nr {nrFilmu}: ")
    
    ocena = -1
    while float(ocena) < 1 or float(ocena) > 10:
        ocena = input("Podaj jego ocenę w skali 1-10: ")


    wszystkieNazwy.append(nazwa)
    wszystkieOceny.append(ocena)

    liczbaRekordowDoWpisania -= 1
    nrFilmu += 1


nazwaPliku = "filmoteka.csv"
f = open(nazwaPliku, "w")
# naglowek
f.write("L.p.,Tytuł_filmu,Ocena\n")

# rekordy
for iFilm in range(len(wszystkieNazwy)):
    nrRekordu = iFilm+1
    f.write(str(nrRekordu) + "," + wszystkieNazwy[iFilm] + "," + wszystkieOceny[iFilm] + "\n")

f.close()

print()
print("Oto zwartość twojego pliku: ")
f = open(nazwaPliku, "r")
print(f.read())
f.close()

