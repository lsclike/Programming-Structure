def is_link(s):
        return s == empty or (len(s) == 2 and is_link(s[1]))
def link(first, rest):
        assert is_link(rest), "rest must be a linked list."
        return [first, rest]
def first(s):

        assert is_link(s), "first only applies to linked lists."
        assert s != empty, "empty linked list has no first element."
        return s[0]
def rest(s):
        assert is_link(s), "rest only applies to linked lists."
        assert s != empty, "empty linked list has no rest."
        return s[1]

