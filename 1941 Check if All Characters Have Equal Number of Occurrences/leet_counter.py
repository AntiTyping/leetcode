class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = Counter(s)
        count = -1
        for c in freq.values():
            if count == -1:
                count = c
            else:
                if count != c:
                    return False
        return True

# >>> dis.dis(areOccurrencesEqual)
#   1           0 RESUME                   0
#
#   6           2 LOAD_GLOBAL              1 (NULL + Counter)
#              12 LOAD_FAST                1 (s)
#              14 CALL                     1
#              22 STORE_FAST               2 (freq)
#
#   7          24 LOAD_CONST               1 (-1)
#              26 STORE_FAST               3 (count)
#
#   8          28 LOAD_FAST                2 (freq)
#              30 LOAD_ATTR                3 (NULL|self + values)
#              50 CALL                     0
#              58 GET_ITER
#         >>   60 FOR_ITER                17 (to 98)
#              64 STORE_FAST               4 (c)
#
#   9          66 LOAD_FAST                3 (count)
#              68 LOAD_CONST               1 (-1)
#              70 COMPARE_OP              40 (==)
#              74 POP_JUMP_IF_FALSE        3 (to 82)
#
#  10          76 LOAD_FAST                4 (c)
#              78 STORE_FAST               3 (count)
#              80 JUMP_BACKWARD           11 (to 60)
#
#  12     >>   82 LOAD_FAST                3 (count)
#              84 LOAD_FAST                4 (c)
#              86 COMPARE_OP              55 (!=)
#              90 POP_JUMP_IF_TRUE         1 (to 94)
#              92 JUMP_BACKWARD           17 (to 60)
#
#  13     >>   94 POP_TOP
#              96 RETURN_CONST             2 (False)
#
#   8     >>   98 END_FOR
#
#  14         100 RETURN_CONST             3 (True)
# >>>