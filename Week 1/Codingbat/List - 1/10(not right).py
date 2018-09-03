def rotate_left3(nums):
  l = len(nums)
  new = []
  nums[0] = nums[l-1]
  nums[1] = nums[0]
  #for i in range(0, l):
   # nums[i] = nums[i-1]
  return nums
