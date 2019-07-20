# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target): 
  i = 0 
  while i < len(nums):
    f_index = nums.index(nums[i])
    numWanted = target - nums[i]
    if numWanted in nums:
      s_index = nums.index(numWanted)
      if f_index == s_index:
        nums.pop(s_index)
        numWanted = target - nums[i]
        s_index = nums.index(numWanted) + 1

      if f_index != s_index:
        return [f_index, s_index]
    i += 1

hey = twoSum([3,2,4], 6)
print(hey)
        