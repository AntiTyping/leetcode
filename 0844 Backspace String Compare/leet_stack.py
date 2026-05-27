class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        stack1 = []
        stack2 = []
        # O(n)
        for i in s:
            if i == '#':
                if len(stack1) > 0:
                    stack1.pop()
            else:
                stack1.append(i)
        # O(n)
        for i in t:
            if i == '#':
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(i)
        if stack1 == stack2:
            return True
        else:
            return False