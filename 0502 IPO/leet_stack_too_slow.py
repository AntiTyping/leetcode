class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        backlog = sorted(zip(capital, profits))

        stack = []
        i = 0
        for _ in range(k):
            while i < len(backlog) and backlog[i][0] <= w:
                stack.append(backlog[i][1])
                i += 1

            stack.sort()

            if len(stack) == 0:
                return w

            w += stack.pop()

        return w





