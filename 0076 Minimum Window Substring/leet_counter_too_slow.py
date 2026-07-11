class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Given two strings s and t,
        # return the shortest substring of s such that every character in t,
        # including duplicates, is present in the substring.
        # If such a substring does not exist, return an empty string "".

        # You may assume that the correct output is always unique.
        ct = Counter(t)
        min_l = len(s)
        min_s = ""
        # O(n)
        l, r = 0, 0

        def valid(l, r):
            ss = s[l:r + 1]
            # O(n)
            if Counter(ss) & ct == ct:
                return True
            else:
                return False

        # O(n)
        while l < len(s) and r < len(s):
            # O(n)
            if valid(l, r):
                if min_l >= r - l + 1:
                    min_l = r - l + 1
                    min_s = s[l:r + 1]
                l += 1
            else:
                r += 1
        return min_s
