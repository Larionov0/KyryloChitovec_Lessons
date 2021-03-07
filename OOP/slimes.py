class Slime:
    name = 'Slime'
    v = 10
    eyes = 3

    def __add__(self, other):  # +
        new_slime = Slime()
        new_slime.name = self.name + other.name
        new_slime.v = self.v + other.v
        new_slime.eyes = self.eyes + other.eyes
        return new_slime

    def __gt__(self, other):  # >
        if self.v > other.v:
            return True
        else:
            return False

    def __str__(self):  # str, print
        return f"Slime {self.name} (v={self.v} eyes={self.eyes})"


s1 = Slime()
s1.name = 'Sleezy'
s1.v = 5
s1.eyes = 2

s2 = Slime()
s2.name = 'Breezy'
s2.v = 8
s2.eyes = 1

s3 = s1 + s2

print(s1)
