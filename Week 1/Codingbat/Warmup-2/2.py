def string_splosion(str):
  res = ""
  sol = ""
  for i in range(0, len(str)):
    if(len(str)==1):
      return str
    else:
      res += str[i]
      sol += res
  return sol