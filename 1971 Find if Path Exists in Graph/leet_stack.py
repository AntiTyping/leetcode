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

        stack = [source]
        visited = {source}

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for e in graph[node]:
                if e not in visited:
                    visited.add(e)
                    stack.append(e)

        return False