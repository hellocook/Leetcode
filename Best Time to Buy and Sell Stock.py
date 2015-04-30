class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
           if not prices:
                  return 0
           cur = prices[0]
           low =0
           for i in range(1,len(prices)):
                  if prices[i]<cur:
                         cur = prices[i]
                  low = max(low,prices[i]-cur)
           return low
 
       
s=Solution()
A=[1,2]
print (s.maxProfit(A))
