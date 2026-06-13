class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # You are given a string s consisting of only uppercase english characters
        # and an integer k.
        # You can choose up to k characters of the string
        #   and replace them with any other uppercase English character.

        # After performing at most k replacements,
        # return the length of the longest substring which contains only one distinct character.
        # XYYX
        # YYYY -> 4
        # XXYXXYXX
        # XYXYXXYXX
        # .  .  .

        def valid(h):
            n = 0
            for v in h.values():
                if v > 0:
                    n += v
            max_c = max(h.values())
            return max_c + k >= n

        max_l = 0
        l, r = 0, 0
        h = defaultdict(int)
        # O(n)
        while r < len(s) and l < len(s):
            h[s[r]] += 1
            if valid(h):
                max_l = max(max_l, r - l + 1)
                r += 1
            else:
                ss = s[l]
                if h[ss] > 0:
                    h[ss] -= 1
                l += 1
                r += 1
        return max_l