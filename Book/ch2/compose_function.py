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

def level_1(n):
    def level_2(k):
        def level_3(l):
            return l+k+n
        return level_3
    return level_2

#inner_function = compose1(square, make_adder(2))
#print(inner_function(4))
compose1(square, make_adder(2))(3)