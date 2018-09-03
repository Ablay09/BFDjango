def array_count9(nums):
  l = len(nums)
  cnt = 0
  for i in range(l):
    if(nums[i] == 9):
      cnt +=1
  return cnt
