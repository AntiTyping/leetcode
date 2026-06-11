class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}

        for i in range(len(s)):
            x = s[i]
            if x in m:
                m[x] += 1
            else:
                m[x] = 1

        l = 0
        for k, v in m.items():
            if v % 2 == 1:
                l = 1
                break

        for k, v in m.items():
            if v % 2 == 0:
                l += v
            else:
                l += 2 * (v // 2)

        return l


