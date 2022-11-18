from random import randint as losowanko

N = int(input("Podaj górny zakres: "))

x = losowanko(1, N)
print(f"Ok. Wybrałem losową liczbę z przedziału 1 do {N}.")

while True: 
    odp =  int(input("Zgadnij jaką?"))
    if(odp > x):
        print("Za dużo!")
    elif(odp < x):
        print("Za mało!")
    else:
        print("Zgadłeś!")
        break

print("Koniec programu.")
