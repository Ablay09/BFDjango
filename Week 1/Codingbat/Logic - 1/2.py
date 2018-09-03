def caught_speeding(speed, is_birthday):
  res = 0
  a = 60
  b = 61 
  c = 80
  d = 81
  if(is_birthday):
    a+=5
    b+=5
    c+=5
    d+=5
    
  if(speed<=a):
        res = 0
  if (b<=speed<=c): 
      res = 1
  if (speed>=d):
      res = 2
  return res