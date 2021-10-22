def cascade_tree(n: int):
    if n//10==0:
        print(n)
    else:
        print(n)
        cascade_tree(n//10)
        print(n)

