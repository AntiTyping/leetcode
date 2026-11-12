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

        ans = []

        stack = [[0]]

        while stack:
            path = stack.pop()
            node = path[-1]
            if node == n - 1:
                ans.append(path[:])
            for e in g[node]:
                stack.append(path + [e])

        return ans