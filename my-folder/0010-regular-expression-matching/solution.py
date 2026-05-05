class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # memo solution

        cache = {}

        def dfs(i, j):
            # CACHE CHECK: MEMO
            if (i,j) in cache:
                return cache[(i,j)]

            # BASE CASE: both pointers are out of bounds
            if i >= len(s) and j >= len(p): return True

            # BASE CASE: pattern is out of bounds
            if j >= len(p): return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j+1) < len(p) and p[j+1] == "*": # highest precedence
                # two choices.
                cache[(i,j)] = (dfs(i, j+2) or # dont use the star
                    (match and dfs(i+1, j))) # use the star (if match happens)
                return cache[(i,j)]
            
            # dont have a star character.
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            
            cache[(i,j)] = False
            
            # if characters don't match.
            return False
        
        return dfs(0,0)
