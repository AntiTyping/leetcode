class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1011
        h = 0
        for i in range(32):
            if n & 2**i == 2**i:
                h += 1
        return h