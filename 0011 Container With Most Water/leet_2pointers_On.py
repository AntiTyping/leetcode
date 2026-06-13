class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        h = heights
        l, r = 0, len(h)-1
        while l < r:
            a = min(h[l], h[r]) * (r-l)
            max_w = max(max_w, a)
            if h[l] > h[r]:
                r -= 1
            else:
                l += 1
        return max_w