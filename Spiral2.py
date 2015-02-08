class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def definition(self,n):
           self.result = [[None for col in range(n)] for row in range(n)]
           self.visit = [[False for col in range(n)] for row in range(n)]
           self.x = [0,1,0,-1]
           self.y = [1,0,-1,0]
    def path(self,x,y,direction,k,n):
           for i in range(4):
                  d = (direction + i) % 4
                  new_x = x + self.x[d]
                  new_y = y + self.y[d]
                  if new_x >= 0 and new_x < n and \
                  new_y >= 0 and new_y < n and \
                  self.visit[new_x][new_y] == False:
                         self.visit[new_x][new_y] = True
                         self.result[new_x][new_y]=k
                         #print (new_x,new_y)
                         #print (self.visit)
                         self.path(new_x,new_y,d,k+1,n)
    def generateMatrix(self, n):
           self.definition(n)
           if n == 0:
                  return []
           else:
                  self.visit[0][0]=True
                  i =1
                  self.result[0][0]=i
                  self.path(0,0,0,i+1,n)
                  return self.result
           #print(self.result)


n = 2
s = Solution()
print(s.generateMatrix(n))
