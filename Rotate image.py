class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):

           result = []
           for i in range(len(matrix)):
                  step = []
                  for j in range(len(matrix)-1,-1,-1):
                         step.append(matrix[j][i])
                  result.append(step)
           return result


A = [
       []
       ]
s = Solution()
print (s.rotate(A))
               
