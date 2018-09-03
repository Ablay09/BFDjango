def cat_dog(str):
  l = len(str)
  c_cnt = 0
  d_cnt = 0
  for i in range (l-2):
    if (str[i] == 'c' and str[i+1] =='a' and str[i+2] == 't'):
      c_cnt +=1
    if(str[i] == 'd' and str[i+1] =='o' and str[i+2] == 'g'):
      d_cnt+=1
  if(d_cnt==c_cnt):
    return True
  return False
    
