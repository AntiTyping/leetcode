class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        u = ['a', 'e', 'i', 'o', 'u']

        ss = set()
        for v in u:
            ss.add(v)
            ss.add(v.upper())

        l, r = 0, len(s)-1
        sl = list(s)
        while l <= r:
            while (sl[l] not in ss) and l < r:
                l += 1
            while (sl[r] not in ss) and l < r:
                r -= 1
            sl[l], sl[r] = sl[r], sl[l]
            l += 1
            r -= 1

        return "".join(sl)