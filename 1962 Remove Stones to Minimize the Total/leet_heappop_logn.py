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

        for i in range(k):
            heapify(a)
            b = -a[0][0]
            b -= b // 2
            a[0][0] = -b

        s = 0
        for i in range(len(a)):
            s += a[i][0]
        return -s

