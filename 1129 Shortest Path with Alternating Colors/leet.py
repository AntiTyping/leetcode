class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red = defaultdict(list)
        for a, b in redEdges:
            red[a].append(b)

        blue = defaultdict(list)
        for a, b in blueEdges:
            blue[a].append(b)

        queue = deque()
        seen = set()
        ans = [float('inf')] * n

        queue.append((0, 0, 0))
        queue.append((0, 0, 1))

        while queue:  # 0,0,0; 0,0,1
            node, steps, color = queue.popleft()  # 0, 0, 0
            seen.add((node, color))  # 0, 0
            ans[node] = min(ans[node], steps)  # Inf, 0 -> 0
            if color == 0:
                for n in blue[node]:  #
                    if (n, 1) not in seen:
                        seen.add((n, 1))
                        queue.append((n, steps + 1, 1))
            else:
                for n in red[node]:
                    if (n, 0) not in seen:
                        seen.add((n, 0))
                        queue.append((n, steps + 1, 0))

        return [(-1 if a == float('inf') else a) for a in ans]

