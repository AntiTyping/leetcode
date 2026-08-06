class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        b = 2**31
        c = 0
        while b > 0:
            c += (a & b > 0)
            b = b >> 1

        return c