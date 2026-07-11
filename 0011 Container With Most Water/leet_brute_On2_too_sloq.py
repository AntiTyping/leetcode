class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_w = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                w = (j-i)*min(height[i], height[j])
                max_w = max(max_w, w)
        return max_w
