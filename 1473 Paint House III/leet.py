class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # min
        # min cost at i with n neighborhoods
        # variables: ith house, n neighborhoods, previous house color

        maximum = float('inf')
        memo = {}

        @cache
        def paint(i, neighborhoods, lastcolor):
            if neighborhoods > target:
                return maximum
            if i == m and neighborhoods == target:
                return 0
            if i == m and neighborhoods != target:
                return maximum

            curr_color = houses[i]
            if curr_color:
                if curr_color != lastcolor:
                    return paint(i + 1, neighborhoods + 1, curr_color)
                return paint(i + 1, neighborhoods, curr_color)

            temp = maximum
            for nextcolor in range(1, n + 1):
                if nextcolor != lastcolor:
                    temp = min(temp, cost[i][nextcolor - 1] + paint(i + 1, neighborhoods + 1, nextcolor))
                else:
                    temp = min(temp, cost[i][nextcolor - 1] + paint(i + 1, neighborhoods, nextcolor))
            return temp

        r = paint(0, 0, 0)
        return -1 if r == maximum else r