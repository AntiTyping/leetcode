class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # before, after, merge

        merged = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                merged.append(newInterval)
                return merged + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                merged.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        merged.append(newInterval)

        return merged

if __name__ == "__main__":
    print(Solution().insert([[1,2], [3, 4]], [1,9]))