def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1

def curry2(f):

    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f

if __name__ == '__main__':
    result = curried_pow(2)(4)
    # print(result)
    # mapResult = map_to_range(0, 10, curried_pow(2))
    curry2_result = curry2(pow)
    # print(curry2_result(2)(3))
    curry2_result_final = curry2(pow)(2)(3)
    uncurry2_result_1 = uncurry2(curry2_result)(2, 3)
    print(uncurry2_result_1)