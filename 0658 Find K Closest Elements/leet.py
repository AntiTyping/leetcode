class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        heap = []
        for i in range(len(arr)):
            heappush(heap, (abs(x - arr[i]), arr[i]))

        return sorted([heappop(heap)[1] for i in range(k)])

