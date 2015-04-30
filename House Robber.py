class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        result = [0 for i in range(len(nums)+1)]
        for i in range(1,len(nums)+1):
               if i-1 > 0:
                      if i-2 >= 0:
                             result[i] = max(nums[i-1]+result[i-2],result[i-1])
               else:
                      result[i] = nums[i-1]
        return result[len(nums)]

s =Solution()
nums=[2,3,5,3,7,19]
print (s.rob(nums))
