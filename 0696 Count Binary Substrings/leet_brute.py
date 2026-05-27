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

        # O(n), O(1)
        def is_valid(s, l, r):
            f = s[l]
            while l < r:
                if s[l] != f:
                    return False
                if s[l] == s[r]:
                    return False
                l += 1
                r -= 1
            return True

        out = 0
        # O(n)
        for i in range(len(s)):
            # O(n)
            for j in range(i, len(s)):
                ss = s[i:j + 1]
                if len(ss) > 1:
                    if len(ss) % 2 == 0:
                        if is_valid(s, i, j):
                            out += 1

        return out


