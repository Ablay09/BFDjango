def last2(str):
  l_two = str[-2:]
  l = len(str)
  ch = str[:l-1]
  cnt = 0
  for i in range (l-2):
    if(l_two == str[i] + str[i+1]):
      cnt+=1
  return cnt