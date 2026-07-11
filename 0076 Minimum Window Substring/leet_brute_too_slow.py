class Solution:
    def minWindow(self, s: str, t: str) -> str:
# Given two strings s and t,
# return the shortest substring of s such that every character in t,
# including duplicates, is present in the substring.
# If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.
        min_l = len(s)
        min_s = ""
        # O(n)
        for i in range(len(s)):
            # O(n)
            for j in range(i, len(s)):
                ss = s[i:j+1]
                # O(n)
                if Counter(ss) & Counter(t) == Counter(t):
                    if len(ss) <= min_l:
                        min_l = len(ss)
                        min_s = ss
        return min_s
