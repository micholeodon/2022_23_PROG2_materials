for buka in "Kognitywiści to my!":
    # print(buka, end="")
    print("!")

print("Po petli...")

lista = [23, 1, -7, True, "Boguś", 1+8j]

print(lista[2:5])

for i in range(7, 34, -7):
    print(i)


for i in range(34, 4, -7):
    print(i)


M = [[1,2,3], [4,5,6]]

for wiersz in M:
    # print(wiersz)
    for kolumna in wiersz:
        print(kolumna)

dict = {"pn":1, "wt":2}

for k in dict.keys():
    print(k)

for v in dict.values():
    print(v)

for el in dict.items():
    print(el)

for k,v in dict.items():
    print("klucz: " + k)
    print("wartosc: " + str(v))

