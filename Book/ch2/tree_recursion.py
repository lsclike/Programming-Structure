def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [root_label] + list(branches)

def branches(tree):
    return tree[1:]

def label(tree):
    return tree[0]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if(not is_tree(branch)):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branches_count = [count_leaves(branch) for branch in branches(tree)]
        return sum(branches_count)

if __name__ == '__main__':
    t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    fib_test =fib_tree(5)
    leaf_count = count_leaves(fib_test)
    print(leaf_count)

