class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        n = 0

        h = {}

        def is_nice(h):
            a = ""
            for k in h:
                if k.isupper() == True:
                    if k.lower() not in h:
                        return False
                if k.islower() == True:
                    if k.upper() not in h:
                        return False
            return True

        for x in range(len(s)):
            h[s[x]] = True
            for y in range(x, len(s)):
                h[s[y]] = True
                if is_nice(h):
                    if y - x + 1 > n:
                        n = y - x + 1
                        i = x
            h = {}

        return s[i:i + n]

