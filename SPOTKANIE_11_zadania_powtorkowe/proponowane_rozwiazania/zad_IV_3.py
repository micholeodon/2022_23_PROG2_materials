from math import sqrt

class Wektor2D:

    def __init__(self, coord1, coord2) -> None:
        self.x = coord1
        self.y = coord2

    def norm(self):
        return sqrt(self.x**2 + self.y**2)

    def add(self, w2):
        self.x += w2.x
        self.y += w2.y

    def dotProduct(self, w2):
        return self.x*w2.x + self.y*w2.y

    def cosAngle(self, w2):
        n1 = Wektor2D.norm(self)
        n2 = Wektor2D.norm(w2)
        return Wektor2D.dotProduct(self,w2)/(n1*n2)

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

w1 = Wektor2D(1,1)
w2 = Wektor2D(-1,-1)
print(w1.norm())
print(w1.dotProduct(w2))
print(w1.cosAngle(w2))
w1.add(w2)
print(w1)
