def missing_char(str, n):
  a = str[ : n]
  b = str[ n+1 :]
  for i in range(0, len(str)-1):
     if(str[i] == n):
      remove(str, i)
  return a+b
 