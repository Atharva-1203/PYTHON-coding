class Solution(object):
    def maxProfit(self, prices):
        min_price=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cp=prices[i]-min_price
            if cp>profit:
                profit=cp
            min_price=min(min_price,prices[i])
        return profit
        """
        :type prices: List[int]
        :rtype: int
        """
        