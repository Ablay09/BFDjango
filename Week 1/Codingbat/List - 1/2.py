def common_end(a, b):
  a_f = a[0]
  b_f = b[0]
  l_a = len(a)
  l_b = len(b)
  a_l = a[l_a-1]
  b_l = b[l_b-1]
  if(a_f == b_f or a_l == b_l):
    return True
  return False