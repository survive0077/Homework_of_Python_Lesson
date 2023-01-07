class Fraction:
    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            self.num = top
            self.den = bottom
        else:
            raise RuntimeWarning("Warning : The numerator and denominator of the fraction must be both integers.")


example1 = Fraction(1, 2)
example2 = Fraction(1.1, 2)
