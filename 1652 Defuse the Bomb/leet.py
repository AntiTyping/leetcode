class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        out = [0] * len(code)

        if k > 0:
            s = sum(code[1:k + 1])
            out[0] = s
            for l in range(1, len(code)):
                s -= code[l % len(code)]
                s += code[(l + k) % len(code)]
                out[l] = s
        elif k < 0:
            s = sum(code[k:])
            out[0] = s
            for l in range(1, len(code)):
                s -= code[(l - 1 + k) % len(code)]
                s += code[(l - 1)]
                out[l] = s
        else:
            None

        return out

