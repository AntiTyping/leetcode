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

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for e in graph[node]:
                if e not in visited:
                    if dfs(e):
                        return True
            return False

        return dfs(source)