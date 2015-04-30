class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
           length=len(prices)
           f1=[0 for i in range(length)]
           f2=[0 for i in range(length)]
           if length !=0:
                  m_min=prices[0]
                  f1[0]=0
                  f2[length-1]=0
                  m_max=prices[length-1]
           for i in range(1,len(prices)):
                  if prices[i]<m_min:
                         m_min=prices[i]
                  f1[i]=max(f1[i-1],prices[i]-m_min)
           for i in range(length-2,-1,-1):
                  if prices[i]>m_max:
                         m_max=prices[i]
                  f2[i]=max(f2[i+1],m_max-prices[i])
           result = 0
           for i in range(length):
                  result = max(result,f1[i]+f2[i])
           return result
                  
s = Solution()
array=[]
print(s.maxProfit(array))
