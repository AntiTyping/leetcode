class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for l in range(len(s) - 3 + 1):
            if len(set(s[l:l + 3])) == 3:
                n += 1
        return n
