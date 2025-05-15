class MedianFinder(object):

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            a = - heapq.heappop(self.small)
            heapq.heappush(self.large, a)
        if len(self.small) > len(self.large) + 1:
            a = - heapq.heappop(self.small)
            heapq.heappush(self.large, a)
        if len(self.small) + 1 < len(self.large):
            a = - heapq.heappop(self.large)
            heapq.heappush(self.small, a)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / float(2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()