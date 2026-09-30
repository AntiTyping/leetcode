class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(31):
            ans |= (n & 1)
            ans <<= 1
            n >>= 1

        return ans
