def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def square(x):
    return mul(x, x)

def sum_square(x, y):
    return add(square(x), square(y))

if __name__ == '__main__':
    result = sum_square(3, 5)
    print(result)