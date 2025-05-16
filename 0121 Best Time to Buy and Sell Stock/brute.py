class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best = 0
        for l in range(len(prices)):
            for r in range(l+1, len(prices)):
                d = prices[r] - prices[l]
                if d > best:
                    best =  d

        return best