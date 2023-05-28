def f(x):
    return x ** 2

def g(x):
    y = f(x)
    def f():
        return y + x
    return y

print(g(2))