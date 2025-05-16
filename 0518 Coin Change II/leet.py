class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        def ways(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0

            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                memo[i][amount] = ways(i + 1, amount)
            else:
                memo[i][amount] = ways(i, amount - coins[i]) + ways(i + 1, amount)

            return memo[i][amount]

        return ways(0, amount)
