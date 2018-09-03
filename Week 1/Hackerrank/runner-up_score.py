if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    mini = 0
    lst = list(arr)
    lst.sort()
    l = len(lst)
    maxi = lst[0]
    for i in range(l):
        if (maxi<lst[i]):
            maxi = lst[i]
    lst = [x for x in lst if x!=maxi]
    print(max(lst))
        
