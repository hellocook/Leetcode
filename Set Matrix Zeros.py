class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
           self.change = {}
           for row in range(len(matrix)):
                  for col in range(len(matrix[row])):
                         if matrix[row][col] == 0:
                                for i in range(len(matrix[0])):
                                       if row not in self.change:
                                              self.change[row] = []
                                       self.change[row].append(i)
                                for j in range(len(matrix)):
                                       if j not in self.change:
                                              self.change[j] = []
                                       self.change[j].append(col)
           #print(self.change)
           for (k,v) in self.change.items():
                  for g in range(len(v)):
                         matrix[k][v[g]] = 0

A = [
       [0,3,2],
       [2,7,5],
       [1,3,1]
       ]
s = Solution()
s.setZeroes(A)
print (A)
