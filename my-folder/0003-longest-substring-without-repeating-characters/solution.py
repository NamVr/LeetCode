class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        res = 0
        seen = set()
        
        for r in range(n):
            # add r to set.
            while s[r] in seen:
                # remove and shift l
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            res = max(res, r-l+1)

        return res
