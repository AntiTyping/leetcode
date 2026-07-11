class RecentCounter(object):

    def __init__(self):
        self.stack = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.stack.append(t)
        l = bisect.bisect_left(self.stack, t - 3000)
        return len(self.stack) - l

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# sorted