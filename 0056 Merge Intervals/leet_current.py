class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        ans = []
        intervals.sort()

        curr = intervals[0]
        for i in range(1, len(intervals)):
            i2 = intervals[i]
            if i2[0] <= curr[1]:
                curr[1] = max(i2[1], curr[1])
            else:
                ans.append(curr)
                curr = i2
        ans.append(curr)

        return ans