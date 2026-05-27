class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # even lengts
        # half odd, half eve
        # two pointers

        e, o = 0, 1

        # O(n)
        while e < len(nums) and o < len(nums):
            if nums[e] % 2 == 0:
                e += 2
            elif nums[o] % 2 == 1:
                o += 2
            else:
                nums[e], nums[o] = nums[o], nums[e]
                o += 2
                e += 2

        return nums
