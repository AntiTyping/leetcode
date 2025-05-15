class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area