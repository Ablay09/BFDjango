if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print (hash(t))
    """
    hash_n  = 0
    arr = list(integer_list)
    for i in range(len(arr)):
        hash_n += (hash(i))
    print(hash_n)
    
    """
    