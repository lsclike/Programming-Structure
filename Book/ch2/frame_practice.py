
# visualize in python tutor
def make_adder(n):
    def adder(k):
        return k+n
    return adder
	    
test = make_adder(1)(2)