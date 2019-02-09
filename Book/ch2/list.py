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

# recursive length
def len_link_recursive(s):
    if s == empty:
        return 0
    else:
        return len_link_recursive(rest(s)) + 1

def getitem_link(s, i):
    while i > 0:
        s = rest(s)
        i -= 1
    return first(s)

def getitem_link_recursive(s, i):
    if i == 0:
        return first(s)
    else:
        return getitem_link_recursive(rest(s), i - 1)

def extend_link(s, t):
    assert is_list(s) and is_list(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def join_link(s, separator):
    if s == empty:
        return ''
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

# implementing a mutable link
def mutable_link():

    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ', ')
    return dispatch

if __name__ == '__main__':
    test_link = link(5,link(4, link(3, link(2, link(1,empty)))))
    print(join_link(test_link, '=>'))
    mutable_link_test = mutable_link()
    mutable_link_test('push_first', 5)
    mutable_link_test('push_first', 4)
    mutable_link_test('push_first', 3)
    getted_item = mutable_link_test('getitem', 1)
    print(getted_item)
    # l1 = link(6, link(5, link(4, link(3, link(2, link(1, 'empty'))))))
    # result_link = extend_link(test_link, l1)
    # print(result_link)
