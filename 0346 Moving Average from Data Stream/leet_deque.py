class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.deque = deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.deque.append(val)  # 1, 10
        self.sum += val  # 1, 11
        if len(self.deque) > self.size:  # 1 > 3; 2 > 3
            old = self.deque.popleft()
            self.sum -= old
        return float(self.sum) / len(self.deque)  # 1 / 1; 11 / 2

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)