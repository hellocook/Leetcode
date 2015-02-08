class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
             if not triangle:
                    return 0
             if len(triangle) == 1:
                    return triangle[0][0]
             oldresult =  [0] *len(triangle[ (len(triangle)-1)])
             result = [0] *len(triangle[ (len(triangle)-1)])
             oldresult[0] = triangle[0][0]
             for i in range(len(triangle)):
                if i == 0 :
                       continue
                
                for j in range(len(triangle[i])):
 
                     if j - 1 >= 0:
                            
                            if j < len(triangle[i-1]):
 
                                   result[j] = min(oldresult[j-1],oldresult[j]) + triangle[i][j]
                            else:
                                   result[j] = triangle[i][j] + oldresult[j-1]

                     else:
 
                            result[j] = oldresult[j] + triangle[i][j]
 
 
                oldresult=[]
                for value in result:
                       oldresult.append(value)
 
                                 
             Max = 10000000
             for i in result:
                     if i < Max:
                            Max = i
             return Max




s = Solution()
A =[[1],[2,3]]
print (s.minimumTotal(A))


