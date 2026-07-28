class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        cols = len(heights[0])

        def neighbours(node):
            n = []
            r, c = node
            dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
            for dir in dirs:
                dr, dc = dir
                n.append((r + dr, c + dc))
            return n

        def valid(node):
            r, c = node
            return 0 <= r < rows and 0 <= c < cols

        def within_effort(node1, node2, effort):
            r1, c1 = node1
            r2, c2 = node2
            return abs(heights[r1][c1] - heights[r2][c2]) <= effort

        def dfs(node, effort):
            r, c = node
            if r == rows - 1 and c == cols - 1:
                return True
            for n in neighbours(node):
                if valid(n) and within_effort(node, n, effort) and n not in seen:
                    seen.add(n)
                    if dfs(n, effort):
                        return True
            return False

        me = max([max(a) for a in heights])
        l, r = 0, me
        while l <= r:
            effort = (r + l) // 2
            seen = set()
            if dfs((0, 0), effort):
                r = effort - 1
            else:
                l = effort + 1
        return l
