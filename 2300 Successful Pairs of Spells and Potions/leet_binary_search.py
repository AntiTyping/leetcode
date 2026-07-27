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
        # 100_000 * 17 = 1_700_000
        for i, spell in enumerate(spells):
            left = bisect.bisect_left(potions, ceil(float(success) / spell)) # 8
            if left < len(potions) and potions[left] == ceil(float(success) / spell):
                ans[i] = len(potions) - left
            else:
                ans[i] = len(potions) - left

        return ans
