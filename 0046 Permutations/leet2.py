class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []

        def perm(nums):
            if len(nums) == 1:
                return [nums]
            elif len(nums) == 2:
                return [[nums[0], nums[1]], [nums[1], nums[0]]]
            else:
                ps = []
                perms = perm(nums[1:])
                for p in perms:
                    for i in range(len(p) + 1):
                        nc = p[:]
                        nc.insert(i, nums[0])
                        ps.append(nc)
                return ps

        return perm(nums)
