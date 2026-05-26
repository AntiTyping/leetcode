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
                a, b = l, len(s)
                ss[a:b] = reversed(ss[a:b])
            elif len(s) - l < 2 * k:
                a, b = l, l + k
                ss[a:b] = reversed(ss[a:b])
            else:
                a, b = l, l + k
                ss[a:b] = reversed(ss[a:b])
            l += 2 * k

        return "".join(ss)