class Complex:
    def __init__(self, re, im):
        self.real = re
        self.imag = im

    def __truediv__(self, other):
        # (a+bi)/(c+di) = (ac+bd)/(c^2+d^2) + (bc-ad)/(c^2+d^2)i
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            raise ZeroDivisionError('cannot divide by zero complex number')
        re = (self.real * other.real + self.imag * other.imag) / denominator
        im = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(re, im)

    def __repr__(self):
        return 'real = %0.2f, imag = %0.2f' % (self.real, self.imag)

c1 = Complex(3, -4)
c2 = Complex(-3, 4)

c3 = c1 / c2

print(c1)
print(c2)
print(c3)
