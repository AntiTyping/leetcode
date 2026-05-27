class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_palindrom(s, l, r):
            l, r = 0, len(s) - 1

            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)):
            if is_palindrom(s[:i] + s[i + 1:]):
                return True

        return False