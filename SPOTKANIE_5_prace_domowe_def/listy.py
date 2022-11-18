lista = [2, 7, -1, 234, -900]

# print(max(lista))

M = lista[0]

for el in lista:
    if(el > M):
        M = el

print(M)
