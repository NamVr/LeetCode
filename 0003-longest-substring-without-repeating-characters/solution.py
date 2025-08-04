class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)

        m = set() # to check duplicated characters.

        l = 0
        for r in range(n):
            while s[r] in m:
                m.remove(s[l])
                l+=1
                
            m.add(s[r])
            res = max(res, r-l+1)

        return res
