class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        meeting = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < meeting[1]:
                return False
            meeting = intervals[i]
        return True