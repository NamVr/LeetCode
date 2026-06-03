class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        curr = defaultdict(int)
        match = Counter(p)
        l = 0

        res = [] # start indexes of each anagram

        for r in range(len(s)):
            curr[s[r]] += 1 # add current letter

            # while k length is build up.
            if r-l+1 != len(p):    
                continue
            
            # length of r-l+1 window is now k to match anagrams.
            if curr == match:
                res.append(l)
            
            # otherwise move forward.
            curr[s[l]] -= 1

            if curr[s[l]] == 0:
                del curr[s[l]]

            l += 1

        return res
