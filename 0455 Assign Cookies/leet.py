class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        l, r = 0, 0

        n = 0

        while l < len(g) and r < len(s):
            if s[r] < g[l]:
                r += 1
            else:
                l += 1
                r += 1
                n += 1
        return n

