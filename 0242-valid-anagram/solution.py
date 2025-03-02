class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        S, T = {}, {} # maps

        for i in range(len(s)):
            S[s[i]] = S.get(s[i], 0) +1
            T[t[i]] = T.get(t[i], 0) +1

        return S == T 
