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
        counts = [0] * 26

        def valid():
            n = 0
            for v in counts:
                if v > 0:
                    n += v
            max_c = max(counts)
            return max_c + k >= n

        max_l = 0
        l, r = 0, 0
        h = defaultdict(int)
        # O(n)
        while r < len(s) and l < len(s):
            counts[ord(s[r]) - ord('A')] += 1
            if valid():
                max_l = max(max_l, r - l + 1)
                r += 1
            else:
                ss = ord(s[l]) - ord('A')
                if counts[ss] > 0:
                    counts[ss] -= 1
                l += 1
                r += 1
        return max_l