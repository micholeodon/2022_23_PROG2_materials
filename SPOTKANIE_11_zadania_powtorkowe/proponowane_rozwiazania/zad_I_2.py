
print("Wartość wielomianu a2 * x^2 + a1 * x + a0 dla wybranego x.")
a2 = float(input("Podaj a2: "))
a1 = float(input("Podaj a1: "))
a0 = float(input("Podaj a0: "))

print("Twój wielomian to:")
print(f"{a2}x^2 + {a1}x + {a0}")

x = float(input("Podaj x: "))
y =  a2 * x*x + a1 * x + a0
print(f"Wartość wielomianu dla x = {x}: \n{y}")

