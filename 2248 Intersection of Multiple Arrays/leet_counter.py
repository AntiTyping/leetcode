class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        freq = Counter()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                freq[nums[i][j]] += 1
        ans = []
        for k in freq:
            if freq[k] == len(nums):
                ans.append(k)
        return sorted(ans)
