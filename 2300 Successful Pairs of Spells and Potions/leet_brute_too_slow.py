class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # 100_000
        ans = [0] * len(spells)
        # 100_000 * 100_000 = 10_000_000
        for i, spell in enumerate(spells):
            for potion in potions:
                if spell * potion >= success:
                    ans[i] += 1

        return ans
