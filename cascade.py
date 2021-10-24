def cascade_tree(n: int):
    if n//10==0:
        print(n)
    else:
        print(n)
        cascade_tree(n//10)
        print(n)


# a range value maps to an exit way
def finbo(number):
    if number <= 2:
        return 1
    else:
        return finbo(number-1) + finbo(number-2)

4

f(3) + f(2)
f(1) + f(2) + f(2)