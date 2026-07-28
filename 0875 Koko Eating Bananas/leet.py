class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def enough_time(k):
            sum = 0
            for bannanas in piles:
                sum += ceil(bannanas / float(k))
            return sum <= h

        l, r = 1, max(piles)
        while l <= r:
            m = (r + l) // 2
            if enough_time(m):
                r = m - 1
            else:
                l = m + 1

        return l
