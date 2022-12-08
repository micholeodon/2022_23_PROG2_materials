from math import pi

class Circle: 

    def __init__(self, promien):
        self.r = promien

    def obliczObwod(self):
        return 2*pi*self.r
        
    def obliczPole(self):
        return pi*self.r*self.r


kolo1 = Circle(0)
kolo2 = Circle(2)

print("1: ", kolo1.obliczObwod(), kolo1.obliczPole())
print("2: ", kolo2.obliczObwod(), kolo2.obliczPole())