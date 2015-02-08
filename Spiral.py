class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def definition(self,matrix):
           self.result = []
           self.visit = [[False] * len(matrix[0]) for row in range(len(matrix))]
           self.x = [0,1,0,-1]
           self.y = [1,0,-1,0]
    def path(self,x,y,direction,matrix):
           for i in range(4):
                  d = (direction + i) % 4
                  new_x = x + self.x[d]
                  new_y = y + self.y[d]
                  if new_x >= 0 and new_x < len(matrix) and \
                  new_y >= 0 and new_y < len(matrix[0]) and \
                  self.visit[new_x][new_y] == False:
                         self.visit[new_x][new_y] = True
                         self.result.append(matrix[new_x][new_y])
                         print (new_x,new_y)
                         print (self.visit)
                         self.path(new_x,new_y,d,matrix)
    def spiralOrder(self, matrix):
           self.definition(matrix)
           if not matrix:
                  return []
           else:
                  self.visit[0][0]=True
                  self.result.append(matrix[0][0])
                  self.path(0,0,0,matrix)
           print(self.result)


A = [
       [1,2,3],
       [4,5,6],
       [7,8,9],      
       [10,11,12]
       ]
s = Solution()
s.spiralOrder(A)
