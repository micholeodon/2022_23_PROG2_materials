def obliczPoleProstokata(a, b=0):
    print(f"a={a} ; b={b}")
    return a*b

A = float(input("Podaj bok prostokata a: "))
B = float(input("Podaj bok prostokata b: "))

pole = obliczPoleProstokata(b=B)
print(pole)