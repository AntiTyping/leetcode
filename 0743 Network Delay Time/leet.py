class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbours = defaultdict(list)
        for a, b, w in times:
            neighbours[a - 1].append((b - 1, w))

        distances = [float('inf')] * n
        distances[k - 1] = 0

        heap = [(k - 1, 0)]

        while heap:
            node, distance = heappop(heap)

            if distance > distances[node]:
                continue

            for n, w in neighbours[node]:
                dist = distance + w
                if dist < distances[n]:
                    distances[n] = dist
                    heappush(heap, (n, dist))

        ans = max(distances)
        return ans if ans < float('inf') else -1
