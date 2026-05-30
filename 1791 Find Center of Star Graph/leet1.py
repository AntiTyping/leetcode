class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        h = defaultdict(int)
        for e in edges:
            h[e[0]] += 1
            h[e[1]] += 1
        max_ = [0, 0]
        for i in h.items():
            if i[1] > max_[1]:
                max_ = i
        return max_[0]

