class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        a = []
        for i in range(len(piles)):
            a.append([piles[i], i])

        for i in range(k):
            a.sort(key=lambda x: x[0], reverse=True)
            a[0][0] -= a[0][0] // 2

        s = 0
        for i in range(len(a)):
            s += a[i][0]
        return s

