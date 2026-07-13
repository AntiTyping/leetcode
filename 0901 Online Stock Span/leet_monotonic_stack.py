class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):  # 100; 80
        """
        :type price: int
        :rtype: int
        """
        n = 0
        while self.stack and self.stack[-1][0] <= price:
            n += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, n + 1])
        return n + 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

