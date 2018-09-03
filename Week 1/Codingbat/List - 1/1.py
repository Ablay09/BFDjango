def first_last6(nums):
  l = len(nums)
  for i in range(0, l):
    if(nums[0] == 6 or nums[l-1]==6):
      return True
  return False