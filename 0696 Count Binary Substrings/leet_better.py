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

        out = 0
        # O(n)
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                out += 1
                l, r = i - 1, i + 1 + 1
                # O(n)
                while l >= 0 and r < len(s) and s[l] == s[i] and s[r] == s[i + 1]:
                    out += 1
                    l -= 1
                    r += 1

        return out


