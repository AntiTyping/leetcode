class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h = height
        w = 0
        for i in range(1, len(h) - 1):
            max_l = 0
            for l in range(i - 1, -1, -1):
                max_l = max(max_l, h[l])
            max_r = 0
            for r in range(i + 1, len(h)):
                max_r = max(max_r, h[r])

            hh = min(max_l, max_r)
            ww = max(0, hh - h[i])
            w += ww

        return w