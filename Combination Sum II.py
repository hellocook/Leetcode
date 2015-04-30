import copy
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        var = []
        self.use = [0]*len(candidates)
        self.result = []
        candidates.sort()
        self.dfs(candidates,target,var,0)
        return self.result
    def dfs(self,candidates,target,var,start):
           if target == 0 and var not in self.result:
                  self.result.append(var[:])
           elif target < 0:
                  return
           else:
                  for i in range(start,len(candidates)):
                         if i==0 or candidates[i]!=candidates[i-1] or self.use[i-1] == 1:
                                var.append(candidates[i])
                                target -= candidates[i]
                                self.use[i] = 1
                                self.dfs(candidates,target,var,i+1)
                                target += candidates[i]
                                var.pop()
                                self.use[i] = 0

                                
a = [13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19]
s = Solution()
print (s.combinationSum2(a,25))
