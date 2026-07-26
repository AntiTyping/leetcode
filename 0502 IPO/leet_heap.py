class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        backlog = sorted(zip(capital, profits))

        heap = []

        i = 0
        for _ in range(k):
            while i < len(backlog) and backlog[i][0] <= w:
                heappush(heap, -backlog[i][1])
                i += 1

            if len(heap) == 0:
                return w

            p = heappop(heap)

            w += -p

        return w




