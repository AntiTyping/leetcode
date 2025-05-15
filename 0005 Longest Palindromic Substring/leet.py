class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = ""
        for k in range(len(s)):
            i, j = k,k
            while i > -1 and j < len(s) and s[i] == s[j]:
                new_p = s[i:j+1]
                if len(new_p) > len(p):
                    p = new_p
                i -= 1
                j += 1
            i, j = k,k+1
            while i > -1 and j < len(s) and s[i] == s[j]:
                new_p = s[i:j+1]
                if len(new_p) > len(p):
                    p = new_p
                i -= 1
                j += 1
        return p