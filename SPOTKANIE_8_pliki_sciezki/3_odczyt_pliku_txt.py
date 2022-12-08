
# odczytywanie pliku tekstowego

print()
print()

file = open("gradientMargulies_Sch100.csv", "r") # r = read czyli odczyt

# caly tekst jako jeden string
text = file.read()
print(text)
print(len(text))

print()
print()

file.seek(0) # cofa pozycję odczytu do początku pliku

# po linijce
text = file.readline()
print(text)
text = file.readline()
print(text)
text = file.readline()
print(text)

# linie tekstu do listy
file.seek(0)
lista = file.readlines()
print(lista)

# za pomocą pętli
file.seek(0)
for line in file:
    print(line, end="")
    print(type(line))

file.close() # trzeba pamiętać o zamknięciu pliku