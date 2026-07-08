class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners = defaultdict(int)
        loosers = defaultdict(int)
        for m in matches:
            winners[m[0]] += 1
            loosers[m[1]] += 1
        one_loss = []
        for k in loosers:
            if loosers[k] == 1:
                one_loss.append(k)

        return [sorted(list(set(winners.keys()) - set(loosers.keys()))), sorted(one_loss)]