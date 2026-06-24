class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [Counter()]

        i = 0
        while i < len(formula):
            if formula[i] == "(":
                stack.append(Counter())
                i += 1
            elif formula[i] == ")":
                i += 1
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i] or 1)
                top = stack.pop()
                for e, n in top.items():
                    stack[-1][e] += top[e] * mult
            else:
                start = i
                i += 1
                while i < len(formula) and formula[i].isalpha() and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                number = int(formula[start:i] or 1)
                stack[-1][name] += number

        ans = ""
        for k in sorted(stack[0].keys()):
            v = stack[0][k]
            if v == 1:
                ans += k
            else:
                ans += k + str(v)

        return ans
