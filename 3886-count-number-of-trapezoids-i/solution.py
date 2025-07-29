class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1000000007
        m = defaultdict(int)

        for _, y in points:
            m[y] += 1
        
        res = total = 0
        for y, count in m.items():
            lines = count * (count - 1) // 2 # number of lines between 2 points => n * n - 1 // 2
            res = (res + total * lines) % MOD # current total + prev * number of new lines
            total = (total + lines) % MOD # total number of lines.
        return res
        
