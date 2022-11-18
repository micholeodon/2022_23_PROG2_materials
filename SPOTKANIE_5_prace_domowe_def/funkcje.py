from math import pi

def obliczObwodKola(r):
    return 2*pi*r

def obliczPoleKola(r):
    return pi*r*r

def obliczPoleProstokata(a,b):
    return a*b

R = float(input("Podaj promien R: "))
A = float(input("Podaj bok prostokata a: "))
B = float(input("Podaj bok prostokata b: "))

# ob = 2*pi*R
# poleKola = pi*R*R 
# polePro = a*b 
 
print(f"Obwód koła o promieniu {R} wynosi {obliczObwodKola(R)}")
print(f"Pole koła o promieniu {R} wynosi {obliczPoleKola(R)}")
print(f"Pole prostokąta o wymiarach {A} x {B} wynosi {obliczPoleProstokata(A,B)}")

# obliczObwodKola(R)
# obliczPoleKola(R)
# obliczPoleProstokata(a,b)