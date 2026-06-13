import unittest

from leet_brute import Solution

class Test3Sum(unittest.TestCase):
    def test_threeSum(self):
        self.assertEqual(Solution().threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])