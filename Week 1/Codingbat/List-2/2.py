def sum13(nums):
  l = len(nums)
  cnt = 0
  for i in range (0, l):
    if(nums[i] == 13):
      continue
    if(i>0 and nums[i-1] == 13):
      continue
    cnt += nums[i]
  return cnt