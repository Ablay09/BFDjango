def front3(str):
  a = str[:3]
  b = str[3:]
  c= len(str)
  if(c>=2 or c!=0 or c!=1 ):
    return a+a+a
  else:
    return a+b