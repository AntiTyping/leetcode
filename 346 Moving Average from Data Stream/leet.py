class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.q = []
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.q.append(val)
        if len(self.q) > self.size:
            x = self.q.pop(0)
            self.sum -= x
        return float(self.sum) / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)