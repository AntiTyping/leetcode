class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """

        def time(speed):
            sum = 0
            for i in range(len(dist) - 1):
                sum += ceil(float(dist[i]) / speed)
            sum += float(dist[-1]) / speed
            return sum

        for speed in range(1, 10 ** 7):
            if time(speed) <= hour:
                return speed

        return -1