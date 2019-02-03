empty = 'empty'
def is_list(s):
    return s == empty or (len(s) == 2 and is_list(s[1]))

def link(first, rest):
    assert is_list(rest)
    return [first, rest]

def first(s):
    assert is_list(s)
    assert s != empty
    return s[0]

def rest(s):
    assert is_list(s)
    assert s != empty
    return s[1]

def len_link(s):
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    while i > 0:
        s = rest(s)
        i -= 1
    return first(s)

if __name__ == '__main__':
    test_link = link(5,link(4, link(3, link(2, link(1,empty)))))
    print(getitem_link(test_link, 0))
