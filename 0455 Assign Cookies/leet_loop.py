class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        l = 0
        n = 0
        for c in s:
            if l < len(g):
                if g[l] <= c:
                    l += 1
                    n += 1
        return n

