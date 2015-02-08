class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def __init__(self):
 #          self.visit = [None] * 3
           self.final = []
    def result(self, level,level_now):
           if len(level) == level_now:
                  vector = []
                  for i in range(len(self.visit)):
                         if self.visit[i] == True:
                                #if vector.count(level[i]) == 0:
                                vector.append(level[i])
                  vector.sort()
                  if self.final.count(vector) == 0:
                         self.final.append( vector )
           else:
                  self.visit[level_now] = False
                  self.result(level,level_now+1)
                  self.visit[level_now] = True
                  self.result(level,level_now+1)
                  
    def subsetsWithDup(self, S):
           if not S:
                  return None
           else:
                  self.visit = [None] * len(S)
                  self.result (S,0)
                  return self.final

    
                  
s = Solution()
A =[0]
print(s.subsetsWithDup(A))
