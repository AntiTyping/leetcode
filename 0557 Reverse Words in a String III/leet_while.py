class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, 0

        ss = list(s)

        while l < len(s):
            r = l
            while r < len(s) - 1 and ss[r + 1] != " ":
                r += 1
            n = r + 1
            while l < r:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
            l = n + 1

        return "".join(ss)
