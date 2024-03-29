import math
from operator import getitem
# using constructor and selector layer - 2
def rational(n, d):
    # lowest barrier layer - 1
    rational_gcd = math.gcd(n, d)
    return [n // rational_gcd, d // rational_gcd]

def number(x):
    return x[0]

def denom(x):
    return x[1]

# using rational to perform calculation layer - 3
def add_rationals(x, y):
    nx, dx = number(x), denom(x)
    ny, dy = number(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(number(x) * number(y), denom(x) * denom(y))

def print_rational(x):
    print(number(x), '/' ,denom(x))

def rationals_are_equal(x, y):
    return number(x) * denom(y) == number(y) * denom(x)


## violate abstract barrier
def square_rational(x):
    return mul_rationals(x, x)

def square_rational_violate_once(x):
    return rational(number(x) * number(x), denom(x) * denom(x))

def square_rational_violate_twice(x):
    return [x[0] * x[0], x[1] * x[1]]

if __name__ == '__main__':
    r1 = rational(1, 2)
    r2 = rational(2, 4)
    print_rational(r1)
    print_rational(r2)
    print(rationals_are_equal(r1, r2))