class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        st = set()

        i, j = 0, 0

        while i < len(s) and j < len(s):
            x = s[j]

            while x in st:
                st.remove(s[i])
                i += 1
            st.add(x)
            n = max(len(st), n)
            j += 1

        return n

