class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
           self.num = 0
           while n != 0:
                  if n&1==1:
                         self.num += 1
                  n = n>>1
           return self.num

s = Solution()
print(s.hammingWeight(11))
