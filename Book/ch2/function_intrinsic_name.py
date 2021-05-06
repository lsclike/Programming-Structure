# display intrinsic function name from frame
def test_func(x):
    return x
    
test = test_func
test_func = 123
resut = test(4)