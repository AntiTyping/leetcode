class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        g = defaultdict(list)
        for node in range(len(graph)):
            for e in graph[node]:
                g[node].append(e)

        current = [0]
        ans = []

        def dfs(node):
            if node == n - 1:
                ans.append(current[:])
            for e in g[node]:
                current.append(e)
                dfs(e)
                current.pop()

        dfs(0)

        return ans