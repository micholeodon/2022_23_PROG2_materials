import csv

# wersja z dodawaniem nowej kolumny i with-as

def srednia(lista):
    suma = 0
    for x in lista:
        suma += x
    
    return suma/len(lista)


with open("data.csv", 'r') as inFile:
    with open('dataOut.csv', 'w') as outFile:
        reader = csv.reader(inFile)
        writer = csv.writer(outFile)


        # update header
        header = next(reader)
        header.append('avg')
        writer.writerow(header)

        # update rows
        newData = []
        for row in reader:
            newRow = [float(x) for x in row] # list comprehension
            avg = srednia(newRow)
            row.append(str(avg))
            newData.append(row)

        # write to file
        writer.writerows(newData)