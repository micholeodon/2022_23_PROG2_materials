# silnia

n = int(input("Podaj liczbe naturalną: "))
if n < 0:
    print("Bład! n ujemne, a powinno być n >= 0")

else:

    fact = 1
    for k in range(1, n+1):
        fact *= k

    print("n! =", fact)