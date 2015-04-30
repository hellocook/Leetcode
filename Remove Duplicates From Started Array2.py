import copy
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
           directionary={}
           for i in range(len(A)):
                  if A[i] not in directionary:
                         directionary[A[i]]=1
                  else:
                         if directionary[A[i]] <2:
                                directionary[A[i]] += 1
           sorted(directionary.items(),key = lambda e:e[0], reverse=False)
           print (directionary)
           values = directionary.values()
           length = sum(values)
           j=0
           for i in directionary.keys():
                  if directionary[i] == 1:
                         A[j] = i
                         j += 1
                  elif directionary[i] == 2:
                         A[j] = i
                         A[j+1] = i
                         j += 2
           return length

s=Solution()
A=[-7,0,-5,-5,0,3,2]
s.removeDuplicates(A)
