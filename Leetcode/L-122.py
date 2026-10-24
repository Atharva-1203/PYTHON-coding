class Solution(object):
    def maxProfit(self, prices):
        profit=0
        for i in range(len(prices)-1):
            if(prices[i]<prices[i+1]):
                profit=profit+(prices[i+1]-prices[i])
        return profit
        
        """
        :type prices: List[int]
        :rtype: int
        """
        