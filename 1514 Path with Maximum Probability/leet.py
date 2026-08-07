class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        distances = [0] * n
        distances[start_node] = 1

        heap = [(-1, start_node)]

        while heap:
            distance, node = heappop(heap)
            distance = - distance

            if distance < distances[node]:
                continue

            for n1, w in graph[node]:
                dist = distance * w
                if dist > distances[n1]:
                    distances[n1] = dist
                    heappush(heap, (-dist, n1))

        return distances[end_node]