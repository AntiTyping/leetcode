class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        # [3,4,2,3,4,7]
        # [1,4,2,3,4,7]

        pairs = {}
        ans = float('inf')
        for r in range(len(cards)): # 0, 1, 2, 3
            if cards[r] in pairs: # 0 - 3, 1 - 4, 2 - 2, 3 - 3
                ans = min(ans, r - pairs[cards[r]] + 1) # inf, 3 - 0 + 1 = 4;
                pairs[cards[r]] = r  # 3 -> 3
            else:
                pairs[cards[r]] = r # 3 -> 0, 4 -> 1, 2 - 2
        return ans if ans < float('inf') else -1