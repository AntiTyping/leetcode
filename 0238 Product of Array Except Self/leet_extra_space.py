class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rl = [0] * len(nums)
        p = 1
        for i in range(len(nums) - 1, 0, -1):
            p *= nums[i]
            rl[i] = p

        out = []
        pl = 1
        for i in range(len(nums)):
            p = 1
            if i > 0:
                pl *= nums[i - 1]
            # O(n)
            # for j in range(i+1,len(nums)):
            #     p *= nums[j]
            # O(1)
            if i < len(nums) - 1:
                p = rl[i + 1]

            out.append(pl * p)
        return out