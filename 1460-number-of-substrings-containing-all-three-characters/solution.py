class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l,res = 0,0
        count = [0] * 3 # a,b,c counts

        for r in range(n):
            count[ord(s[r]) - ord('a')] += 1

            while count[0] and count[1] and count[2]:
                res += n-r

                count[ord(s[l]) - ord('a')] -= 1
                #if count[s[l]] == 0:
                #    count.pop(s[l])
                                
                l += 1
        
        return res
