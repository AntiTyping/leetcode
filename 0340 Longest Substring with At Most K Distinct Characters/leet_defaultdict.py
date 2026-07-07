class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c = defaultdict(int)
        l = ans = 0
        for r in range(len(s)):
            c[s[r]] += 1
            while len(c) > k:
                c[s[l]] -= 1
                if c[s[l]] == 0:
                    del c[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
