class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = 0
        ss = list(s)
        while l < len(s):
            if len(s) - l < k:
                a, b = l, len(s) - 1
                while a < b:
                    ss[a], ss[b] = ss[b], ss[a]
                    a += 1
                    b -= 1
            elif len(s) - l < 2 * k:
                a, b = l, l + k - 1
                while a < b:
                    ss[a], ss[b] = ss[b], ss[a]
                    a += 1
                    b -= 1
            else:
                a, b = l, l + k - 1
                while a < b:
                    ss[a], ss[b] = ss[b], ss[a]
                    a += 1
                    b -= 1
            l += 2 * k

        return "".join(ss)