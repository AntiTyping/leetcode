class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        idx = []
        # O(n), O(n)
        for i in range(len(s)):
            if s[i] == c:
                idx.append(i)

        # ,O(n)
        out = [0] * len(s)
        # O(n)
        for i in range(len(s)):
            m = len(s)
            # O(n)
            for j in range(len(idx)):
                if abs(idx[j] - i) < m:
                    m = abs(idx[j] - i)
            out[i] = m
        return out

