class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        # return graph

        def dfs(node, target, weight):  # b, c
            if not node:
                return 0

            for nn in graph[node]:  # b -> a, 0.5
                n, w = nn  # a, 0.5
                if (node, n) not in self.seen:
                    self.seen.add((node, n))
                    if n == target:
                        return weight * w
                    a = dfs(n, target, weight * w)
                    if a != 0:
                        return a
            return 0

        ans = []
        for q in queries:
            a = 1
            self.seen = set()
            w = dfs(q[0], q[1], 1.0)
            if w != 0:
                ans.append(w)
            else:
                ans.append(-1)

        return ans
