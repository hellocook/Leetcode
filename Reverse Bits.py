class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
           array = [0]*32
           i = 0
           result = 0
           while n!=0:
               array[i] = n&1
               i += 1
               n = n>>1
           i = 0
           while i <= 31:
                  result = result | array[i]
                  result = result << 1
                  i += 1
           return result>>1


s = Solution()
print(s.reverseBits(43261596))
