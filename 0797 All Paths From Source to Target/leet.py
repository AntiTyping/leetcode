class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        last = len(graph) - 1

        out = []

        def backtrack(curr):
            if curr[-1] == last:
                out.append(curr[:])
                return
            n = curr[-1]
            for k in graph[n]:
                curr.append(k)
                backtrack(curr)
                curr.pop()

        backtrack([0])
        return out
