class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        h = {"0": "0", "1": "1", "2": "e", "3": "a", "4": "b", "5": "d", "6": "9", "7": "c", "8": "8", "9": "6"}

        l, r = 0, len(num) - 1
        # n
        while l <= r:
            if num[l] != h[str(num[r])]:
                return False
            l += 1
            r -= 1
        return True
