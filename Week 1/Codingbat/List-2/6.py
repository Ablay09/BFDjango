def has22(nums):
  l = len(nums)
  for i in range (l-1):
    if(nums[i] == 2 and nums[i+1] == 2):
      return True
  return False