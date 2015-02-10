class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
               if A[i] == target:
                      return i
               elif target < A[i]:
                      return i
               else:
                      continue
        if i + 1 == len(A):
               return len(A)

s = Solution()
A =[1,3,5,6]
print (s.searchInsert(A,0))
               
