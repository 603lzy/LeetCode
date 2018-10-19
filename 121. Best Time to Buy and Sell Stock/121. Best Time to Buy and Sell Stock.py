class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0 # max profit
        bt = 0 # buy time
        lenp = len(prices)
        if lenp <= 1:
            return 0
        i = 0
        while i < lenp - 1:
            if (prices[bt] < prices[i]) and (prices[i] > prices[i+1]):
                maxp = max(maxp, prices[i] - prices[bt])
                i += 1
            elif (prices[bt] > prices[i]) and (prices[i] < prices[i+1]):
                bt = i
                i += 1
            else:
                i += 1
        maxp = max(maxp, prices[i] - prices[bt])
        return maxp
