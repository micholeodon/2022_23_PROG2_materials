# zgadywanko poprawnie

a = 1
b = int(input("Podaj górny zakres: "))
odp = a
oszust = False

print(f"Pomyśl liczbę całkowitą z zakresu a=1 do b={b}. Gdy będziesz gotów wciśnij ENTER ...")
input()

while(a != b):
    if(a > b):
        oszust = True
        print("Prosisz mnie o niemożliwe rzeczy, Złotko! \n[Komputer opuścił pokój]")
        break
    else:
        odp = round( (a + b) / 2 )
    
        print(f"a = {a}, b = {b}")
        print(f"x = {odp}?")
        print(" Za mało: L\n", "Za dużo: H\n", "Trafiony: E", end="\n")
        user = input().lower()

    
        if(user == "e"): # (odp == x): # hit!
            a = odp
            b = odp
            break
        elif(user == "h"): # (odp > x): # too big!
            b = odp - 1
        elif(user == "l"): # (odp <= x) # too small!
            a = odp + 1
        else:
            print("Nie rozumiem! Powtórz!")

if(not oszust):
    print(f"To musi być {a}")
