UinputCorrect = False
while not UinputCorrect:
    U = float(input("Podaj wartość napięcia zasilania obwodu: "))
    if U < 0:
        print("ERROR: U < 0 ")
    else:
        UinputCorrect = True

RinputCorrect = False
while not RinputCorrect:
    R = float(input("Podaj wartość rezystancji opornika obwodu: "))
    if R <= 0:
        print("ERROR: R <= 0 ")
    else:
        RinputCorrect = True

# obliczenie wartosci pradu
I = U/R  # [A]
print(f"Prad obwodu: {I} A")