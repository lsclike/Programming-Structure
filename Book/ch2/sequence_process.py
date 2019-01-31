import math


def divisors(n):
    return [ x for x in range(1, n+1) if n % x == 0 ]

def get_perfect_number(n):
    return [ x for x in range(1, n+1) if sum(divisors(x)) == x]

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

if __name__ == '__main__':
    test_prime = get_prime(1000)
    print(test_prime)