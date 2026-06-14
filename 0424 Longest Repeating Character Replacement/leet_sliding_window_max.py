class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_l = 0
        most_l = 0
        counts = defaultdict(int)

        def valid(l, r):
            if most_l + k >= r - l + 1:
                return True
            else:
                return False

        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            if counts[s[r]] > most_l:
                most_l = counts[s[r]]
            if valid(l, r):
                max_l = max(max_l, r - l + 1)
            else:
                while l < r and not valid(l, r):
                    counts[s[l]] -= 1
                    l += 1

        return max_l
