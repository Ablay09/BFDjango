def front_back(str):
  l = len(str)
  if (l<=1):
      return str
  return str[l-1]+str[1:-1]+str[0]
      