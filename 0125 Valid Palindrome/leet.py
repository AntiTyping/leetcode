class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                b.append(s[i].lower())

        i, j = 0, len(b) - 1
        while i <= j:
            if b[i] != b[j]:
                return False
            i += 1
            j -= 1

        return True