class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapify(sticks)

        cost = 0
        for i in range(len(sticks) - 1):
            a = heappop(sticks)
            b = heappop(sticks)
            cost += a + b
            heappush(sticks, a + b)

        return cost

