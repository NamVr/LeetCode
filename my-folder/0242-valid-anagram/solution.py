class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if len(s) == len(t) and Counter(s) == Counter(t) else False
