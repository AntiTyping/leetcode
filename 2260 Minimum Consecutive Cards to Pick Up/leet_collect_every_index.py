class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        # [3,4,2,3,4,7]
        # [1,4,2,3,4,7]

        h = defaultdict(list)
        # n
        for i in range(len(cards)):
            h[cards[i]].append(i)

        ans = float('inf')
        for c in h:
            card = h[c]
            if len(card) > 1:
                for i in range(1, len(card)):
                    ans = min(ans, card[i] - card[i - 1] + 1)

        return ans if ans < float('inf') else -1


