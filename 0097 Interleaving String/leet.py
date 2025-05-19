class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(l, r):
            n = l + r
            if n == len(s3) and l == len(s1) and r == len(s2):
                return True
            if l == len(s1) and r == len(s2):
                return False

            a = b = False
            if l < len(s1) and n < len(s3) and s1[l] == s3[n]:
                a = dp(l + 1, r)
            if r < len(s2) and n < len(s3) and s2[r] == s3[n]:
                b = dp(l, r + 1)

            return any([a, b])

        return dp(0, 0)

