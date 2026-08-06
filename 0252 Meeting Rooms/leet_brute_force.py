class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        for i in range(len(intervals)):
            i1 = intervals[i] # 1, 5
            for j in range(i + 1, len(intervals)):
                i2 = intervals[j] # 8, 9
                if i1[0] <= i2[0]: # 1 <= 8
                    if i1[1] > i2[0]: # 5 > 9
                        return False
                else:
                    if i2[1] > i1[0]:
                        return False

        return True
