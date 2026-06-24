class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        s = 0
        # abs(2 - x) <= 3
        # -1 5
        # 2-3 -2-3
        # abs(1-x) <= 13
        # -12 14
        # -12
        for x in range(0, n + k + 1):
            if abs(n - x) <= k and n & x == 0:
                s += x
        return s
