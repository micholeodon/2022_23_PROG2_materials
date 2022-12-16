import csv

# wersja z tworzeniem nowego pliku zamiast dodawania kolumny

def srednia(lista):
    suma = 0
    for x in lista:
        suma += x
    
    return suma/len(lista)


pliczke = open("data.csv", "r")

csvreader = csv.reader(pliczke)
header = next(csvreader)
print(header)


srednie = []
for row in csvreader:
    newRow = [float(x) for x in row] # convert str to float
    srednie.append(srednia(newRow))
    

print(srednie)

pliczke.close()


nowyPlik = open("newData.csv", 'w')

nowyPlik.write('av')
nowyPlik.writelines(['\n' + str(x) for x in srednie])

nowyPlik.close()
