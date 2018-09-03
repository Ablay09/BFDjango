def same_first_last(nums):
  l = len(nums)
  if (l>=1 and nums[0] == nums[-1]):
    return True
  return False
