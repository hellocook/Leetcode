class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
           s = 0
           for i in range(1,len(prices)):
                  if prices[i] > prices[i-1]:
                         s += prices[i] - prices[i-1]
           return s


                  
