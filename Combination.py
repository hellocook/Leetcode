import copy

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
           self.answer=[]
           var=[]
           candidates.sort()
           self.search(candidates,target,0,var)
           return self.answer
    def search(self,candidates,target,start,var):
           if target == 0:
                  self.answer.append(copy.deepcopy(var))
                  #var.sort()
                  #if var not in self.answer:
                         #self.answer.append(copy.deepcopy(var))
                  #print (self.answer)
           elif target < 0:
                  return
           else:
                  for i in range(start,len(candidates)):
                         target -= candidates[i]
                         var.append(candidates[i])
                         self.search(candidates,target,i,var)
                         target += candidates[i]
                         var.pop()

a=[8,10,6,3,4,12,11,5,9]
s=Solution()
print (s.combinationSum(a,28))
