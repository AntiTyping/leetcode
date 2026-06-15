class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # O(n)
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # O(n)
        heapq.heapify(stones)

        # O(n)
        while len(stones) > 1:
            # O(log n)
            x = heapq.heappop(stones)
            # O(log n)
            y = heapq.heappop(stones)
            if x == y:
                pass
            elif x < y:
                x = x - y
                # O(log n)
                heapq.heappush(stones, x)
            else:
                y = y - x
                # O(log n)
                heapq.heappush(stones, y)
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]