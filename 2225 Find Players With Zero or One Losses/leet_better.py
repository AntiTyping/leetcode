class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losses = defaultdict(int)
        for m in matches:
            losses[m[0]] += 0
            losses[m[1]] += 1
        only_wins = []
        one_loss = []

        for player in losses:
            if losses[player] == 0:
                only_wins.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

        only_wins.sort()
        one_loss.sort()
        return [only_wins, one_loss]