class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # stack for storage
        mat = { ")" : "(", "]" : "[", "}" : "{" } # close : open bracket key value pair

        for c in s:
            # for every character in stack, check if its opening bracket
            # add to stack if open bracket

            if c not in mat: # mat.keys() by default
                stack.append(c)
            
            # for every closing bracket, check if stack is not empty,
            # and the value matches the opening pair.

            else: # its a closing bracket
                if stack and stack[-1] == mat[c]:
                    stack.pop()
                else:
                    return False
            
        return True if not stack else False
