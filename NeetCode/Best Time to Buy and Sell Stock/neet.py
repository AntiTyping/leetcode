class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            lp = prices[left]
            rp = prices[right]
            local_profit = rp - lp
            if local_profit > profit:
                profit = local_profit
            right += 1
        return profit