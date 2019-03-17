from math import atan2, cos, sin, pi
class Number:
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.img + other.img)

    def mul(self, other):
        magnitute = self.magnitude * other.magnitude
        return ComplexMA(magnitute, self.angle + other.angle)

class ComplexRI(Complex):
    # constructs a complex number from real and imaginary parts
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

class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def img(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g})'.format(self.magnitude, self.angle)

if __name__ == '__main__':
    ma = ComplexMA(2, pi/2)
    ma1 = complex(3, pi/3)
    print(help(ma))