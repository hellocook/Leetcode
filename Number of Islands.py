class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
           self.index_x = [0,1,0,-1]
           self.index_y = [-1,0,1,0]
           self.number = 0
           self.len_x = len(grid)
           self.len_y = len(grid[0])
           for i in range(self.len_x):
                  for j in range(self.len_y):
                         if(grid[i][j]=='1'):
                                self.number += 1
                                self.dfs(grid,i,j)
           return self.number
       
    def dfs(self,grid,x,y):
           if(grid[x][y]=='1'):
                  grid[x][y] = '0'
                  for i in range(4):
                         new_x = x + self.index_x[i]
                         new_y = y + self.index_y[i]
                         if new_x >= 0 and new_x<self.len_x and new_y>=0 and new_y < self.len_y:
                                if grid[new_x][new_y] == '1':
                                       self.dfs(grid,new_x,new_y)


s = Solution()
data2 = []
data = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','1','1']]
print (s.numIslands(data2))
