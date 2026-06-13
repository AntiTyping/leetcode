class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        h = {}
        max_l = 0
        while l < len(s) and r < len(s):
            while s[r] in h:
                del h[s[l]]
                l += 1

            h[s[r]] = True
            ln = r - l + 1
            max_l = max(max_l, ln)
            r += 1

        return max_l
