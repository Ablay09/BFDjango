if __name__ == '__main__':
    n = int(input())
    cnt  = 0
    lst = []
    
    dict = {}
    command, *line = input().split()
    numbers = list(map(int, line))
    dict[command] = numbers
    
    #for i in range(0, n-1):
    for command in dict:
        if (command = "insert"):
            lst.append(dict)
            
        
    
   