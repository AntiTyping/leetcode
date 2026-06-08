class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()

        m = mass
        for i in range(len(asteroids)):
            if m >= asteroids[i]:
                m += asteroids[i]
            else:
                return False
        return True