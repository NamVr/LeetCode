class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        a: set[str] = {c for c in w if c.islower()}
        b: set[str] = {c.lower() for c in w if c.isupper()}
        return len(a & b)
