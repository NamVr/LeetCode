class Solution:
    def minimumLength(self, s: str) -> int:
        m = Counter(s) # counts of each character in string
        res = 0

        for freq in m.values():
            if freq % 2 == 1:
                res += 1
            else:
                res += 2

        return res

        # return sum(
        #    1 if x%2 # event
        #    else 2
        #    for x in Counter(s).values()
        #)
