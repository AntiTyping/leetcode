class Solution:
    def countOfAtoms(self, formula):
        self.stack = [defaultdict(int)]
        self.name = ""
        self.num = 0
        self.has_num = False
        self.state = 'ELEM'

        for c in formula:
            if c.isupper():
                self._flush()
                self.name = c
            elif c.islower():
                self.name += c
            elif c.isdigit():
                self.num = self.num * 10 + int(c)
                self.has_num = True
            elif c == '(':
                self._flush()
                self.stack.append(defaultdict(int))
            else:  # ')'
                self._flush()
                self.state = 'GROUP'

        self._flush()  # commit the last pending token at EOF

        counts = self.stack[0]
        return ''.join(
            n + (str(counts[n]) if counts[n] > 1 else '')
            for n in sorted(counts)
        )

    def _flush(self):
        if self.state == 'ELEM':
            if self.name:
                self.stack[-1][self.name] += self.num if self.has_num else 1
        else:  # GROUP: close the group and merge down
            mult = self.num if self.has_num else 1
            top = self.stack.pop()
            for k, v in top.items():
                self.stack[-1][k] += v * mult
        self.name, self.num, self.has_num, self.state = "", 0, False, 'ELEM'