class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # does inverse lookup help

        # at node n find all edges the point to n

        direct = defaultdict(list)
        inverse = defaultdict(list)
        for a, b in connections:
            direct[a].append(b)
            inverse[b].append(a)

        self.ans = 0

        self.seen = [0] * (len(connections) + 1)

        def dfs(node):
            self.seen[node] = 1
            # find all paths and counte inverted patsh
            neighbors = direct[node]
            for n in direct[node]:
                if self.seen[n] == 0:
                    self.ans += 1
                    dfs(n)
            for n in inverse[node]:
                if self.seen[n] == 0:
                    dfs(n)

        dfs(0)

        return self.ans
