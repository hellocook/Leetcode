class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
           result = 0
           for value in A:
                  result ^= value
           return value
           
                     
                            

A=[1,1,4,3,2,2,4,5,3]
s=Solution()
print(s.singleNumber(A))

