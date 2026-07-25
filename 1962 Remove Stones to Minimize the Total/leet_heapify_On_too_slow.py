class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        a = []
        for i in range(len(piles)):
            a.append([-piles[i], i])

        heapify(a)
        for i in range(k):
            b = heappop(a)
            b[0] = -b[0]
            b[0] -= b[0] // 2
            b[0] = -b[0]
            heappush(a, b)

        s = 0
        for i in range(len(a)):
            s += a[i][0]
        return -s

