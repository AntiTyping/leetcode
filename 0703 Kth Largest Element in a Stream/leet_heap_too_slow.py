class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = [-n for n in nums]
        heapq.heapify(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        a = []
        heapq.heappush(self.nums, -val)
        for i in range(self.k):
            a.append(heapq.heappop(self.nums))
        for i in range(self.k):
            heapq.heappush(self.nums, a[i])

        return -a[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)