from math import atan2
class Number:
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.img + other.img)

    def mul(self, other):
        magnitute = self.magnitute * other.magnitute
        return ComplexMA(magnitute, self.angle + other.angle)

class ComplexRI(Complex):
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def magnitude(self):
        return (self.real ** 2 + self.img ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.img, self.real)

    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.img)