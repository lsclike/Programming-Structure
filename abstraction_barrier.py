def pair(x,y):
    def result(index):
        if index == 0:
            return x
        else:
            return y
    return result

test = pair(3,4)
test(0)
test(1)