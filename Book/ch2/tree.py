def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree()

    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]