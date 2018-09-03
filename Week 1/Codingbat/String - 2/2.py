def count_code(str):
  l = len(str)
  cnt = 0
  for i in range(l-3):
    if str[i]=='c' and str[i+1]=='o' and str[i+3] == 'e':
      cnt+=1
  return cnt