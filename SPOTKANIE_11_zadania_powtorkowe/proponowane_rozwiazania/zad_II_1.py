coeffs = [] # wspolczynniki

N = int(input("Podaj liczbe wspolczynnikow wielomianu. N = "))

if N < 0 :
    print("Bład! N ujemne, a powinno być N >= 0")
else:

    # zbieranie współczynników
    for i in range(N-1, -1, -1):
        a = float(input(f"Podaj współczynnik a{i}: "))
        coeffs.append(a)

    print(coeffs)

    # wyświetlanie wielomianu
    print("Oto twój wielomian:")
    p = N-1
    for a in coeffs:
        if p > 0 :
            print(f"{a}x^{p} + ", end='')
        else:
            print(f"{a}")
        p -= 1
    
    # obliczenie wartosci dla zadanego x

    x = float(input("Podaj x, dla którego zostanie oblicznona wartość wielomianu: "))

    p = N-1
    y = 0
    for a in coeffs:
        y += a*x**p
        p -= 1

    print(f"Wartość wielomianu dla x = {x}")
    print(f"y = {y}")