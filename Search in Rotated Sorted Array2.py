class Solution:
       def search(self,A,target):
              if target in A:
                     return True
              else:
                     return False

A =[1,2,3,4,5,6]
s = Solution()
print (s.search(A,10))
