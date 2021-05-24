# start playing bit operations

def count_even_odd(n):
    even_count, odd_count = 0, 0
    for i in range(0,n):
        if i & 1 == 0:
            even_count +=1
        else:
            odd_count +=1
    
    print(even_count)
    print(odd_count)


count_even_odd(100)