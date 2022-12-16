import csv

# Skrypt tworzy nowy plik z danymi z data.csv uzupelnionymi o dodatkowa kolumne
# zawierajaca pole prostokata o bokach a i b

fileIn =  open('data.csv', 'r') 
fileOut =  open('data_out.csv', 'w')

# tworzy "czytajacego" i "piszącego"
reader = csv.reader(fileIn)
writer = csv.writer(fileOut, lineterminator='\n')

newData = [] # lista wierszy nowego pliku
row = next(reader) # pobiera kolejny wiersz (tutaj nr 1 czyli nagłówek)
row.append('P') # dodaje naglowek nowej kolumny do istniejacego naglowka
newData.append(row) # dodaje zaktualizowany nagłówek do listy wierszy

# zczytujemy kolejne wiersze i dodajemy na ich koncu dodatkowy element do nowej kolumny
for row in reader:
    a = float(row[0])
    b = float(row[1])
    P = a*b
    row.append(P)  
    newData.append(row)

writer.writerows(newData) # zapisz to co na liście wierszy do pliku

fileIn.close()
fileOut.close()