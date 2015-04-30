class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
           l = len(nums)
           k %= l
           self.reverse(nums,0,l-k-1)
           self.reverse(nums,l-k,l-1)
           self.reverse(nums,0,l-1)
    def reverse(self,nums,first,last):
           while first<last:
                  var = nums[first]
                  nums[first] = nums[last]
                  nums[last] = var
                  first += 1
                  last -= 1
       
           
          
           
           
s=Solution()
array=[1,2,3]
s.rotate(array,4)
print(array)
