def cascade(x):
    if (x // 10) == 0:
        print(x)
    else:
        print(x)
        cascade(x//10)
        print(x)