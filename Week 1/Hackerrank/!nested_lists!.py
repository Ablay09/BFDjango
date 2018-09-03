if __name__ == '__main__':
    n = int(input())
    list = []
    res = []
    fin = []
    mini = 111
    mini1 = 123
    cnt = 0
    var = 0
    var1 = 0
    
    fin = sorted(list)
    for i in range(n):
        name = input()
        score = float(input())
        #adds values to the list
        fin.append([name, score])
    for i in range(len(fin)):
        if(fin[i][1] < mini):
            mini = fin[i][1]
            var = i 
        else:
            continue
    #Delete the minimum element from the list
    del fin[var]
    
    for i in range(len(fin)):
        if(fin[i][1]<=mini1):
            mini1 = fin[i][1]
            var1 = i
        if(fin[i][1]==mini1):
            res.append(i)

    #print(res)
    for i in res:
        print(fin[i][0])
    #print(fin)
               
        