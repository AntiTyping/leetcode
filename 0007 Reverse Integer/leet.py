class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = str(x)
        if n[0] == "-":
            num = int("-" + "".join(reversed(n[1:])))
        else:
            num = int("".join(reversed(n)))
        if num < (-2)**31 or num > 2**31-1:
            return 0
        return num
