def xyz_there(str):
  cnt = 0
  l = len(str)
  for i in range(0, l-3):
    if(str[i-1]!= '.' and str[i]=='x' and str[i+1]=='y' and str[i+2]=='z') or (str[i]!= '.' and str[i+1]=='x' and str[i+2]=='y' and str[i+3]=='z'):
      return True
  return False
  