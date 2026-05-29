class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        out = []

        for s in strs:
            out.append(str(len(s)) + "|" + s)

        return "".join(out)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        j = 0
        out = []
        while j < len(s):
            l = []
            while s[j] != "|":
                l.append(s[j])
                j += 1
            n = int("".join(l))
            out.append(s[j + 1:j + n + 1])
            j += n + 1

        return out

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))