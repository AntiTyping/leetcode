class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        l = 0
        r = len(people) - 1
        n = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            n += 1

        return n