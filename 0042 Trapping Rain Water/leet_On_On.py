class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h = height
        max_l = [0] * len(h)
        max_r = [0] * len(h)
        max_i = [0] * len(h)

        for i in range(1, len(h)):
            max_l[i] = max(max_l[i - 1], h[i - 1])
        for i in range(len(h) - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], h[i + 1])
        for i in range(len(h)):
            max_i[i] = min(max_l[i], max_r[i])

        w = 0
        for i in range(len(h)):
            w += max(0, max_i[i] - h[i])

        return w