import math
from operator import add

# list comprehension for divisors and perfect number
def divisors(n):
    return [x for x in range(1, n) if n % x == 0]

def get_perfect_number(n):
    return [x for x in range(1, n+1) if sum(divisors(x)) == x]

def verify_prime(n):
    if n == 0:
        return False
    if n == 1:
        return True
    for x in range(2, math.ceil((math.sqrt(n))+1)):
        if n % x == 0:
            return False
    return True

def get_prime(n):
    return [x for x in range(n) if verify_prime(x)]

# high-order function
def map_function(map_fn, s):
    [map_fn(x) for x in s]

def keep_if(f_function, s):
    return [x for x in s if f_function(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        # required two parameters
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return keep_if(divides_n, range(1, n))

def sum_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_divisors(n) == n

# width height area
def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

if __name__ == '__main__':
    # perfect_n = get_perfect_number(1000)
    # print(perfectprint(width_test)
    #     # print(perimeter_test)_n)
    divisors_h_test = divisors_of(12)
    sum_divisors_test = sum_divisors(10)
    get_perfect_number_high_test = keep_if(perfect, range(1, 1000))
    print(get_perfect_number_high_test)
    print(sum_divisors_test)
    width_test = width(100, 25)
    perimeter_test = perimeter(25, 4)
    minimum_peris = minimum_perimeter(100)
    print(minimum_peris)
    #