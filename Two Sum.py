class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
           Map = {}
           for i in range(len(num)):
                  if target - num[i] not in Map:
                         Map[num[i]] = i
                  else:
                         return (Map[target-num[i]]+1,i+1)
                        

s=Solution()
num = [3,2,4]
target=6
print(s.twoSum(num,target))
