class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        h = {"1": "1", "2": "e", "3": "a", "4": "b", "5": "d", "6": "9", "7": "c", "9": "6"}

        n = list(reversed(num))
        out = []
        for i in range(len(num)):
            digit = n[i]
            if digit in h:
                out.append(h[digit])
            else:
                out.append(num[i])
        return "".join(out) == num