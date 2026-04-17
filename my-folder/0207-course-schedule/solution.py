class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for c, pre in prerequisites:
            preMap[c].append(pre)
        
        visit = set()
        def dfs(c):
            # base conditions.
            if c in visit: return False
            if preMap[c] == []: return True

            # start exploration.
            visit.add(c)

            for p in preMap[c]:
                if not dfs(p): return False

            visit.remove(c)

            # success.
            preMap[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
