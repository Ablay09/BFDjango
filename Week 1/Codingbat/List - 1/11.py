def sum2(nums):
  l = len(nums)
  res = 0
  if(l>2):
    return nums[0]+nums[1]
  elif(l<=2):
    for i in range (0, l):
      res += nums[i]
    return res
  else:
    return 0