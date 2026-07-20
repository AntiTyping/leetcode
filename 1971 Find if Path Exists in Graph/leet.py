class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        self.seen = [-1] * n

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, color):
            self.seen[node] = color
            for n in graph[node]:
                if self.seen[n] == -1:
                    dfs(n, color)
        color = 0
        for i in range(n):
            if self.seen[i] == -1:
                color += 1
                dfs(i, color)

        return self.seen[source] == self.seen[destination]