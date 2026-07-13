class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):  # 100; 80
        """
        :type price: int
        :rtype: int
        """
        self.stack.append(price)
        n = 0
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] <= price:
                n += 1
            else:
                break
        return n

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

