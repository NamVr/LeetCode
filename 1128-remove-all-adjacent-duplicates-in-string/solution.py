class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []

        # one pass solution
        # check for each letter, if the stack is empty, add the letter
        # if stack has something, check last element [-1] and compare
        # if equal, remove that element, otherwise append
        # return the list of strings, .join them

        for c in s:
            if not res or res[-1] != c:
                res.append(c)
            else:
                res.pop()

        return "".join(res)
