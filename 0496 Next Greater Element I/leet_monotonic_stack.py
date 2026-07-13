class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h = {}
        stack = []
        for i in range(len(nums2)):
            num = nums2[i]
            while stack and nums2[stack[-1]] < num:
                j = stack.pop()
                h[nums2[j]] = num
            stack.append(i)

        ans = []

        for i in range(len(nums1)):
            ans.append(h.get(nums1[i], -1))

        return ans
