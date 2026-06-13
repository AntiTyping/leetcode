class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        st = set()
        max_l = 0
        while l < len(s) and r < len(s):
            while s[r] in st:
                st.remove(s[l])
                l += 1

            st.add(s[r])
            ln = r - l + 1
            max_l = max(max_l, ln)
            r += 1

        return max_l
