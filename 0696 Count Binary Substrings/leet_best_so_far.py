class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # non-empty
        # same number of 0 and 1
        # 0 and 1 are consecurive
        # same number of 0s and 1s

        # 000111
        prev, curr = 0, 1
        n = 0
        # 00110011
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                n += min(prev, curr)
                prev = curr
                curr = 1
        n += min(prev, curr)

        return n


