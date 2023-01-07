
def gcd(m, n):
    n = abs(n)
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        if (newnum // common) * (newden // common) > 0:
            return Fraction(abs(newnum // common), abs(newden // common))
        else:
            return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        if (newnum // common) * (newden // common) > 0:
            return Fraction(abs(newnum // common), abs(newden // common))
        else:
            return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        if (newnum // common) * (newden // common) > 0:
            return Fraction(abs(newnum // common), abs(newden // common))
        else:
            return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        if (newnum // common) * (newden // common) > 0:
            return Fraction(abs(newnum // common), abs(newden // common))
        else:
            return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum


f1 = Fraction(1, -2)
f2 = Fraction(-1, 4)
f3 = f1 + f2
f4 = f1 - f2
f5 = f1 * f2
f6 = f2 / f1
f3.show()
f4.show()
f5.show()
f6.show()