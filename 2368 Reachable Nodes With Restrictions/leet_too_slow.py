class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        rest = set(restricted)

        self.ans = 0
        self.seen = set()

        def dfs(node):
            self.seen.add(node)
            if node in restricted: # silly mistake, use set! fixed in the other version
                return
            self.ans += 1
            for n in graph[node]:
                if n not in self.seen:
                    dfs(n)

        dfs(0)

        return self.ans