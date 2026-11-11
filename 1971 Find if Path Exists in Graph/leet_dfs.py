class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for e in edges:
            f, t = e
            graph[f].append(t)
            graph[t].append(f)

        self.found = False

        visited = set()

        def dfs(node):
            if node == destination:
                self.found = True
                return
            visited.add(node)
            for e in graph[node]:  # 1
                if e not in visited:
                    dfs(e)

        dfs(source)

        return self.found