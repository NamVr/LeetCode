class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        if n < 3:
            return s
        
        # use stack approach. no three consecutive chars are equal.
        # create a stack and dont push if dq.count(num) is 3.
        # at the end, convert the stack to string

        dq = []

        for c in s:
            if len(dq) >= 2 and dq[-1] == c and dq[-2] == c:
                continue
            
            dq.append(c)
        
        return "".join(dq)
