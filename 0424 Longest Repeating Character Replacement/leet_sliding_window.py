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

        def valid(s):
            # O(n)
            c = Counter(s)
            # O(n)
            mc = c.most_common()[0][1] + k
            if mc < len(s):
                return False
            else:
                return True

        max_l = 0
        l, r = 0, 0
        # O(n)
        while r < len(s):
            if valid(s[l:r + 1]):
                max_l = max(max_l, r - l + 1)
                r += 1
            else:
                l += 1
        return max_l