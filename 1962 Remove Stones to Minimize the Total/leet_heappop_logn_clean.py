class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(piles)):
            piles[i] = -piles[i]

        heapify(piles)
        for i in range(k):
            b = heappop(piles)
            b += -b // 2
            heappush(piles, b)

        return -sum(piles)

