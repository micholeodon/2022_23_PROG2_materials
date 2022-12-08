
# zapisywanie do pliku tekstowego

# stworzy nowy plik
file = open("Zodiakary.txt", "w")

for i in range(3):
    name = input("Wpisz imie kolejnej zodiakary: ")
    file.write(name)
    file.write("\n")
	
file.close()

print("Dane wpisane do pliku.")

# UWAGA! Nadpisze istniejący plik!
file1 = open("Zodiakary.txt", "w")
lst = []
for i in range(3):
	name = input("Wpisz imie kolejnej zodiakary: ")
	lst.append(name + '\n')
	
# zapis wszystkich elementow listy do pliku
file1.writelines(lst)
file1.close()
print("Dane wpisane do pliku.")

# UWAGA! Dopisze do pliku
file = open("Zodiakary.txt", "a") # dopisywanie zamiast nadpisywania
file.write("Dopisana linijka\n")

file.close()