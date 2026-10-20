class Complex:
    def __init__(self, re, im):
        self.real = re
        self.imag = im

    def __mul__(self, other):
        # (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        re = self.real * other.real - self.imag * other.imag
        im = self.real * other.imag + self.imag * other.real
        return Complex(re, im)

    def __repr__(self):
        return 'real = %0.2f, imag = %0.2f' % (self.real, self.imag)

c1 = Complex(3, -4)
c2 = Complex(-3, 4)

c3 = c1 * c2

print(c1)
print(c2)
print(c3)
