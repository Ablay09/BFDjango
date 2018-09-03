def not_string(str):
  for i in str:
    if len(str)>=3 and str[0] == "n" and str[1] == "o" and str[2] == "t":
      return str
    else :
      return "not " + str