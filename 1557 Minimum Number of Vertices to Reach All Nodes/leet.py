class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        inedges = defaultdict(list)
        for a, b in edges:
            inedges[b].append(a)

        return [k for k in range(n) if len(inedges[k]) == 0]

