class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
           for i in range(len(matrix)):
                  if self.function(matrix[i],target) == True:
                         return True
           return False
    def function(self,vector,target):
           first = 0
           last  = len(vector) - 1
           while first <= last:
                  middle = int((first + last)/2)
                  if vector[middle] == target:
                         return True
                  elif vector[middle] < target:
                         first = middle + 1
                  elif vector[middle] > target:
                         last = middle - 1
           return False


A = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
s= Solution()
print (s.searchMatrix(A,24))
           
