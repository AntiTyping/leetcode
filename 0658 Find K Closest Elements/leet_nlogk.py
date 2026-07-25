class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        heap = []
        for num in arr:
            heappush(heap, (-abs(x - num), -num))
            if len(heap) > k:
                heappop(heap)

        return sorted([-heappop(heap)[1] for i in range(k)])
