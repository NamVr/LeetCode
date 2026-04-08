class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0

        for i in range(len(s)):
            if s[i] == "(":
                # open
                stack.append(i)
            else:
                # close
                stack.pop()

                if len(stack) == 0: # change boundary marker
                    stack.append(i)
                else: # valid stack
                    res = max(res, i-stack[-1])

        return res
