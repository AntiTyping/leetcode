class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.seen = [-1] * n

        def dfs(node, color):
            self.seen[node] = color  # 1
            for n in graph[node]:  # 1
                if self.seen[n] == -1:
                    dfs(n, color)

        color = 0
        for i in range(n):  # 0
            if self.seen[i] == -1:
                color += 1
                dfs(i, color)  # 0

        return color