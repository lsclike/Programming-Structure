def f(x):
    1/0
def g(x):
    f(x)
def h(x):
    g(x)

print(h(2))