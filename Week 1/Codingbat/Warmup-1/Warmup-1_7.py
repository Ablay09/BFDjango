def pos_neg(a, b, negative):
  if((a>0 and b<0) or (a<0 and b>0)) and not negative:
    return True
  if negative and a<0 and b<0:
    return True
  else:
    return False
