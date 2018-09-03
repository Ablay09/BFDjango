 def array_front9(nums):
  a = nums[:3]
  b = nums[4:]
  for i in range(len(nums)):
    if(nums[i] == 9 and i!=4):
      return True
  return False
