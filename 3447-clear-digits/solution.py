class Solution:
    def clearDigits(self, s: str) -> str:
        res = ""
        for c in s:
            if c.isdigit() and res:
                res = res[:-1] # remove the last character
            else:
                res += c # add character to result
        return res
