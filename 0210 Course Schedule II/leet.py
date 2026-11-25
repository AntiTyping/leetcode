class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1

        ans = []
        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while q:
            c = q.popleft()
            ans.append(c)
            for d in graph[c]:
                indegrees[d] -= 1
                if indegrees[d] == 0:
                    q.append(d)

        return ans if len(ans) == numCourses else []
