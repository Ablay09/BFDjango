def combo_string(a, b):
  l_a = len(a)
  l_b = len(b)
  while(l_a != l_b):
    if(l_a > l_b):
      return b+a+b
    return a+b+a
