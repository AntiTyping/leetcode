class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # even lengts
        # half odd, half eve
        # two pointers

        # , O(n)
        even = [0] * (len(nums) // 2)
        odd = [0] * (len(nums) // 2)

        # , O(1)
        e, o = 0, 0

        # O(n),
        for i in nums:
            if i % 2 == 0:
                even[e] = i
                e += 1
            else:
                odd[o] = i
                o += 1

        # O(n), O(n)
        for i in range(len(even)):
            nums[i * 2] = even[i]
            nums[i * 2 + 1] = odd[i]

        return nums
