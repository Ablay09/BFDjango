def end_other(a, b):
  a_lower = a.lower()
  b_lower = b.lower()
  if b_lower.endswith(a_lower):
    return True
  if a_lower.endswith(b_lower):
    return True
  return False
  
  """a_new = a.lower()
  b_new = b.lower()
  l_a = len(a_new)
  l_b = len(b_new)
  last_a = a_new[-1:]
  last_b = b_new[-1:]
  if len(last_a) == len(last_b) and last_a in last_b or last_b in last_a:
    return True
  return False
  """