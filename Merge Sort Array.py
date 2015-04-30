class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
           i=0
           j=0
           var = []
           while i<m and j<n:
                  if A[i]<=B[j]:
                         var.append(A[i])
                         i += 1
                  else:
                         var.append(B[j])
                         j += 1
           if i == m:
                  for k in range(j,n):
                         var.append(B[k])
           elif j == n:
                  for k in range(i,m):
                         var.append(A[k])
           while len(A)>0:
                  A.pop()
           A.extend(var)

s = Solution()
A=[1,2,3]
B=[2,5,6]
s.merge(A,3,B,3)
print (A)
                         
                  
        
