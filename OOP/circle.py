import math


class Circle:
    x = 0
    y = 0
    r = 0

    def P(self):
        return 2 * math.pi * self.r

    def S(self):
        return math.pi * self.r * self.r

    def distance(self, other):
        d = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1/2)
        return d - self.r - other.r


c1 = Circle()
c2 = Circle()
c1.x = 3
c1.y = 6
c2.x = 8
c2.y = 30

c1.r = 2
c2.r = 1

print(c1.distance(c2))
