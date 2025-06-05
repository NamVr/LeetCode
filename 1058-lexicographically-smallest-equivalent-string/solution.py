class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rx < ry:
                parent[ry] = rx
            else:
                parent[rx] = ry
        
        for a, b in zip(s1, s2):
            union(ord(a) - 97, ord(b) - 97)
        
        res = []
        for c in baseStr:
            r = find(ord(c) - 97)
            res.append(chr(r + 97))
        
        return "".join(res)
