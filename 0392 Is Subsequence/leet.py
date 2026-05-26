class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        l, r = 0, 0

        while l < len(s):
            while r < len(t) and s[l] != t[r]:
                r += 1
            if r < len(t) and s[l] == t[r]:
                l += 1
                r += 1
                if l == len(s):
                    return True
            if r == len(t):
                return False
        return True
