def array123(nums):
  rangel = ([1, 2, 3])
  check =  rangel[0] + rangel[1] + rangel[2]
  l = len(nums)
  for i in range (l-2):
    if(nums[i]+nums[i+1]+nums[i+2] == check):
      return True
  else:
    return False
