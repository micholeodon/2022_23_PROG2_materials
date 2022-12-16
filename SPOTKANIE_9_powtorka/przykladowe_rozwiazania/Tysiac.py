import random 

lista = []
for i in range(1000):
    lista.append(random.random())

suma = 0
for x in lista:
    suma += x

av = suma / len(lista)

print(suma)
print(av)