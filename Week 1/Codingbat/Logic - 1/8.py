def alarm_clock(day, vacation):
  str_7 = "7:00"
  str_10 = "10:00"
  if(1<=day<=5 and not vacation):
    return str_7
  if (vacation and (day == 0 or day == 6)):
    return "off"
  if((day == 0 or day == 6) or (vacation and 1<=day<=5)):
    return str_10
  