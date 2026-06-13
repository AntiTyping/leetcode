class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        # O(n)
        for i in range(len(heights)):
            # O(n)
            for j in range(i + 1, len(heights)):
                if i != j:
                    a = min(heights[i], heights[j]) * (j - i)
                    if a > max_w:
                        max_w = a
        return max_w