import math
import copy
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        B =copy.deepcopy(A)
        B.sort()
        last = len(B) - 1
        first = 0
        middle = None
        find = False
        while first <= last:
               middle = int((first + last)/2)
               if B[middle] == target:
                      find = True
                      break
               elif B[middle] < target:
                      first = middle +1
               elif B[middle] > target:
                      last = middle - 1
              
        for k in range(len(A)):
               if find == True:
                      if B[middle] == A[k]:
                             return k
               else:
                      return -1
               

s = Solution()
A = [1]
print(s.search(A,2))
