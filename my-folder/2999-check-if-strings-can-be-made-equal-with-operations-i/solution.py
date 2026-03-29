class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # swaps allowed:
        # j - i = 2. i.e., 1-3, 2-4 only
        a = sorted([s1[0], s1[2]])
        b = sorted([s1[1], s1[3]])
        c = sorted([s2[0], s2[2]])
        d = sorted([s2[1], s2[3]])

        return a == c and b == d
