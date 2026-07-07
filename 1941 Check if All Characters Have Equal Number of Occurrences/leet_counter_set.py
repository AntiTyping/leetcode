class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = Counter(s)
        return len(set(freq.values())) == 1
# >>> dis.dis(areOccurrencesEqual)
#   1           0 RESUME                   0
#
#   6           2 LOAD_GLOBAL              1 (NULL + Counter)
#              12 LOAD_FAST                1 (s)
#              14 CALL                     1
#              22 STORE_FAST               2 (freq)
#
#   7          24 LOAD_GLOBAL              3 (NULL + len)
#              34 LOAD_GLOBAL              5 (NULL + set)
#              44 LOAD_FAST                2 (freq)
#              46 LOAD_ATTR                7 (NULL|self + values)
#              66 CALL                     0
#              74 CALL                     1
#              82 CALL                     1
#              90 LOAD_CONST               1 (1)
#              92 COMPARE_OP              40 (==)
#              96 RETURN_VALUE