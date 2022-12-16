import csv

# Skrypt tworzy nowy plik z danymi z data.csv uzupelnionymi o dodatkowa kolumne
# zawierajaca pole prostokata o bokach a i b.
#
# Ta wersja używa with-as do otwarcia/zamknięcia pliku i kontroli przed błędami.

with open('data.csv','r') as csvinput:
    with open('data_out.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        newData = []
        row = next(reader)
        row.append('P') # dodaje naglowek nowej kolumny do istniejacego naglowka
        newData.append(row) 

        # zczytujemy kolejne wiersze i dodajemy na ich koncu dodatkowy element do nowej kolumny
        for row in reader:
            a = float(row[0])
            b = float(row[1])
            P = a*b
            row.append(P)  
            newData.append(row)

        writer.writerows(newData)