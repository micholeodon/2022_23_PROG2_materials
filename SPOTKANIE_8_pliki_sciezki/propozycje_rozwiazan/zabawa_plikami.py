import os, sys, shutil, random

os.chdir(sys.path[0])

listaKatalogow = ["pierwszy", "drugi"]

for katalog in listaKatalogow:
    os.mkdir(katalog)

nazwaPliku = "dane.csv"
plik = open(nazwaPliku, "w")
plik.close()


nowaNazwaPliku = "data.csv"
os.rename(nazwaPliku, nowaNazwaPliku)

przeniesionyPlikSciezka = os.path.join(listaKatalogow[0], nowaNazwaPliku)
os.rename(nowaNazwaPliku, przeniesionyPlikSciezka)

skopiowanyPlikSciezka = os.path.join(listaKatalogow[1], nowaNazwaPliku)
shutil.copy(przeniesionyPlikSciezka, skopiowanyPlikSciezka)

x1 = random.random()
print("pierwsza liczba:", x1)
f = open(przeniesionyPlikSciezka, "w")
f.write(str(x1))
f.close()

x2 = random.random()
print("druga liczba:", x2)
f = open(skopiowanyPlikSciezka, "w")
f.write(str(x2))
f.close()

os.remove(przeniesionyPlikSciezka)
os.rmdir(os.path.dirname(przeniesionyPlikSciezka))
os.rename(listaKatalogow[1],listaKatalogow[0])

plikKoncowy = przeniesionyPlikSciezka
f = open(plikKoncowy, "r")
print(f.read())
f.close()

