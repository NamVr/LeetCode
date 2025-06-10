class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        odd = max(i for i in c.values() if i % 2 == 1)
        even = min(i for i in c.values() if i % 2 == 0)

        return odd - even
