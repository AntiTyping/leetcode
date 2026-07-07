class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter()
        l = ans = 0
        for r in range(len(s)):
            c[s[r]] += 1
            while c[s[r]] > 1:
                c[s[l]] -= 1
                if c[s[l]] == 0:
                    del c[s[l]]
                l += 1
            ans = max(ans, r - l + 1)

        return ans