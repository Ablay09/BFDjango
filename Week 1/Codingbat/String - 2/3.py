def count_hi(str):
  cnt = 0
  l = len(str)
  for i in range(l-1):
    if str[i] == 'h' and str[i+1]=='i':
      cnt+=1
  return cnt
