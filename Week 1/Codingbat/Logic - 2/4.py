def lone_sum(a, b, c):
  cnt = 0
  tot = a+b+c
  if(tot/3 == a and tot/3 == b and tot/3 ==c):
    a=0
    b=0
    c=0
  if(a==b or b==a):
    a=0
    b=0
    cnt += c
  if(a==c or c==a):
    a=0
    c=0
    cnt += b
  if(b==c or c==b):
    b=0
    c=0
    cnt+= a
  else:
    cnt = a +b +c
  return cnt
