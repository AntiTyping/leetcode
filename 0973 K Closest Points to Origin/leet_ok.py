class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def distance(p):
            return sqrt(p[0] ** 2 + p[1] ** 2)

        heap = []
        for p in points:
            heappush(heap, (distance(p), p))

        return [heappop(heap)[1] for i in range(k)]