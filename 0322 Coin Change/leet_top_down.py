class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}
        def dp(a): # number of coins
            if a == 0:
                return 0
            elif a < 0:
                return float('inf')
            else:
                if a not in memo:
                    result = float('inf')
                    for c in coins:
                        result = min(result, dp(a-c)+1)
                    memo[a] = result
                return memo[a]

        ans = dp(amount)
        return ans if ans != float('inf') else -1