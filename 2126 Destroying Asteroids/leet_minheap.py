class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        # O(n)
        heapify(asteroids)
        while asteroids:
            # O(logn)
            a = heappop(asteroids)
            if mass >= a:
                mass += a
            else:
                return False
        return True
