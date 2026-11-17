class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        g = defaultdict(list)
        for i in range(n):
            g[i] = graph[i]

        q = deque([[0]])
        paths = []

        while q:
            path = q.popleft()
            a = path[-1]
            if a == n - 1:
                paths.append(path[:])
            for b in g[a]:
                q.append(path + [b])
        return paths

