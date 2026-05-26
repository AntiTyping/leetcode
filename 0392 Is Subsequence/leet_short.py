class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l, r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] != t[r]:
                r += 1
            else:
                l += 1
                r += 1
        return l == len(s)