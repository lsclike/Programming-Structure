def make_adder(n):
    def adder(k):
        return k+n
    return adder

def square(x):
    return x * x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

inner_function = compose1(square, make_adder(2))
print(inner_function(4))