class TwoSum(object):

    def __init__(self):
        self.numbers = []

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.numbers.append(number)

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        h = set()
        for i in range(len(self.numbers)):
            n = self.numbers[i]
            diff = value - n
            if diff in h:
                return True
            else:
                h.add(n)
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
