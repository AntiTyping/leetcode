class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_so_far = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_so_far:
                min_so_far = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_so_far)

        return max_profit