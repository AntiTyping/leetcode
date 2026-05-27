class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two pointers
        l, r = 0, len(s) - 1

        # ,O(n)
        ss = list(s)
        # O(n)
        while l < r:
            while not s[l].isalpha() and l < r:
                l += 1
            while not s[r].isalpha() and l < r:
                r -= 1
            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1

        # O(n)
        return "".join(ss)