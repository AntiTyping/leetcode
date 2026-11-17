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
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])
        visited = {source}

        while q:  # V
            n = q.popleft()
            if n == destination:
                return True
            for u in graph[n]:  # E
                if u not in visited:
                    visited.add(u)
                    q.append(u)

        return False
