def string_match(a, b):
  l_a = len(a)
  l_b = len(b)
  cnt = 0
  res = 0
  for i in range(0, l_a - 1):
    for j in range(0, l_b - 1):
      if(a[i] + a[i+1] == b[j] + b[j+1]):
          cnt+=1
  res = res+cnt
  return res