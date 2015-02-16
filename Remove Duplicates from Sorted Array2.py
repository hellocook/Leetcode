class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
           i = 0
           count = 0
           count_each=0
           lenth = len(A)
           if not A:
                  return 0
           elif len(A)==1:
                  return 1
           while i < lenth:
                  if i+1< lenth and A[i+1]==A[i]:
                         count_each += 1
                         if count_each >=2:
                                count += count_each - 1
                  else:
                         A[i-count] = A[i]
                         count_each = 0
                  i = i+1
           return lenth-count
           

a=[1,1,1,2,3,3,3,4]
s=Solution()
s.removeDuplicates(a)
print(a)
