def pair(x, y):

    def get(index):
        if index==0:
            return x
        else:
            return y
    return get

def select(p, i):
    return p(i)