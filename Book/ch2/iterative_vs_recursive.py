def fact_iter(n):
    total, i = 1,1,
    while i <= n:
        total, i = total*i, i+1
    return total

def fact_recursive(n):
    if n==1:
        return 1
    else:
        return n*(n-1)