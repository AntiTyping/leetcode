class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1011
        h = 0
        while n != 0:
            h += 1
            n = n & (n - 1)

        return h