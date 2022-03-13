def cascade_tree(n: int):
    if n//10==0:
        print(n)
    else:
        print(n)
        cascade_tree(n//10)
        print(n)


# a range value maps to an exit way
def finbo(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return finbo(number-1) + finbo(number-2)

    