def sum_naturals(total, k):
    total += k
    return total

def sum_cubs(total, k):
    total += k*k*k
    return total

def sum_high_order(n, f):
    total, k = 0, 1
    while k <= n:
        total = f(total, k)
        k += 1
    return total


if __name__ == '__main__':
    naturals_result = sum_high_order(3, sum_naturals)
    cubs_result = sum_high_order(4, sum_cubs)
    print(naturals_result)
    print(cubs_result)