class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for n1 in nums1:
            i = 0
            while n1 != nums2[i]:
                i += 1
            found = False
            for j in range(i, len(nums2)):
                n2 = nums2[j]
                if n2 > n1:
                    ans.append(n2)
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans

