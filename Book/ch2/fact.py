def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)


def count_up(n):
    if n==1:
        print(1)
    else:
        count_up(n-1)
        print(n)

