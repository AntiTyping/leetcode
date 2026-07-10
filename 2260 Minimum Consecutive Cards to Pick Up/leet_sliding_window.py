class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        # [3,4,2,3,4,7]
        # [1,4,2,3,4,7]

        h = defaultdict(int)
        l = 0
        ans = float('inf')
        for r in range(len(cards)): # 0
            h[cards[r]] += 1 # 3 - 1
            # window property: only one pair -> h[x] == 2
            if h[cards[r]] >= 2:
                while cards[l] != cards[r] or h[cards[r]] > 2:
                    h[cards[l]] -= 1
                    if h[cards[l]] == 0:
                        del h[cards[l]]
                    l += 1
                ans = min(ans, r - l + 1)
        return ans if ans < float('inf') else -1
