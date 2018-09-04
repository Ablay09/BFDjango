def centered_average(nums):
  lst = sorted(nums)
  #lst[1] = mini
  #lst[-1] = maxi
  cnt = 0
  ans = 0
  cnt_num = 0
  for i in range (1, len(lst)-1):
    cnt += lst[i]
    cnt_num+=1
  ans =int(cnt/cnt_num)
  
  
  return ans