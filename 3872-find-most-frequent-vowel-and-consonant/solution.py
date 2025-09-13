class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)

        vow = max((c[i] for i in c if i in "aeiou"), default=0)
        con = max((c[i] for i in c if i not in "aeiou"), default=0)

        return vow + con

