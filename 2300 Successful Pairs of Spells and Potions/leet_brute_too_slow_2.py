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
        # 100_000 * 17 = 1_700_000
        potions.sort()
        # 100_000 * 50_000 = 5_000_000
        for i, spell in enumerate(spells):
            for j, potion in enumerate(potions):
                if spell * potion >= success:
                    ans[i] = len(potions) - j
                    break

        return ans
