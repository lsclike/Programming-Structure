def double_print(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

if __name__ == '__main__':
    # iterator copy and test
    # test = [1, 2, 3, 4, 5]
    # iter1 = iter(test)
    # iter2 = iter(test)
    # next(iter1)
    # copy_v1 = iter1
    # copy_iter_v1 = iter(iter1) => yield another iterator not a copy of origin
    # v1 = next(copy_iter_v1)
    # v2 = next(iter2)
    # print(v1, v2)

    # yield an iterator to get a lazy evaluation used by map, filter, zip
    double_test = range(1, 5)
    result = map(double_print, double_test)
    # next(result)
    list(result)


