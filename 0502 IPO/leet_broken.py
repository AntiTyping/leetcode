class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # k projects
        # min capital
        # distinct projects

        n = len(profits)
        # O(n)
        # O(n log n)
        projects = sorted(zip(capital, profits))
        i = 0
        heap = []

        # O(k)
        for _ in range(k):
            # O(n)
            while i < n and projects[i][0] <= w:
                # O(log n)
                heapq.heappush(heap, -projects[i][1])
                i += 1

            if len(heap) == 0:
                return w

            # O(log n)
            w -= heapq.heappop(heap)
        return w
