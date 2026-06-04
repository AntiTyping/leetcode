class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mc = [0]*(len(cost)+1)

        # bottom up
        # O(n)
        for i in range(len(cost)+1):
            if i == 0:
                mc[i] = cost[i]
            elif i == 1:
                mc[i] = cost[i]
            elif i < len(cost):
                mc[i] = min(mc[i-2], mc[i-1]) + cost[i]
            else:
                mc[i] = min(mc[i-2], mc[i-1])

        return mc[-1]
