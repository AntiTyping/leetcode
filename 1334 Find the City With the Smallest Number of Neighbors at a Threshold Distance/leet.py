class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(n, edges, src):
            graph = defaultdict(list)
            for a, b, w in edges:
                graph[a].append((b, w))
                graph[b].append((a, w))

            distances = [inf] * n
            distances[src] = 0

            heap = [(0, src)]

            while heap:
                distance, node = heappop(heap)

                if distance > distances[node]:
                    continue


                for n, w in graph[node]:
                    dist = distance + w
                    if dist < distances[n]:
                        distances[n] = dist
                        heappush(heap, (dist, n))

            ans = 0
            for d in distances:
                if d <= distanceThreshold:
                    ans += 1

            return ans

        ans = inf
        citi = -1
        for src in range(n):
            d = dijkstra(n, edges, src)
            if d <= distanceThreshold and d <= ans:
                ans = d
                citi = src

        return citi

