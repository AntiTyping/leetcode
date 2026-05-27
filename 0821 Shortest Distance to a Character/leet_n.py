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

        # O(1)
        first = idx[0]

        out = [0] * len(s)

        # O(n)
        for i in range(len(s)):
            if s[i] == c:
                first = i
            out[i] = abs(i - first)

        last = idx[-1]
        # O(n)
        for i in range(len(s) - 1, 0, -1):
            if s[i] == c:
                last = i
            if out[i] > abs(i - last):
                out[i] = abs(i - last)

        return out

