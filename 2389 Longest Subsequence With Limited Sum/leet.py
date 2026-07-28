class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()

        csum = [0] * len(nums)
        csum[0] = nums[0]
        for i in range(1, len(nums)):
            csum[i] = csum[i - 1] + nums[i]

        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            j = bisect.bisect_left(csum, q)
            # if i == 1:
            #     return csum, j, q
            if j < len(nums) and csum[j] == q:
                ans[i] = j + 1
            else:
                ans[i] = j

        return ans
