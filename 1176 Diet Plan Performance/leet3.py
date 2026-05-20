class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        points = 0
        T = 0

        for i in range(0, k):
            T += calories[i]
        if T > upper:
            points += 1
        if T < lower:
            points -= 1

        l = 0
        for r in range(k, len(calories)):
            T -= calories[l]
            T += calories[r]

            l += 1

            if T > upper:
                points += 1
            if T < lower:
                points -= 1

        return points

