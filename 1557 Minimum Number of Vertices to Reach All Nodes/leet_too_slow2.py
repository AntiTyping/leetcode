class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)

        self.seen = [-1] * n
        self.best = float('inf')

        def dfs(node, color):
            self.seen[node] = color
            for n in graph[node]:
                if self.seen[n] != -1:
                    self.seen[n] = color
                dfs(n, color)

        for i in range(n):
            if self.seen[i] == -1:
                dfs(i, i)

        return list(set(self.seen))