class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        res = []

        for c, p in prerequisites:
            preMap[c].append(p)
        
        state = [0] * numCourses
        # 0 means not visited yet.
        # 1 means being visited.
        # 2 means visited.

        def dfs(c):
            if state[c] == 1:
                return False # cycle detection.
            if state[c] == 2:
                return True # already visited.
            
            state[c] = 1 # mark is being visited.
            # explore all it's pre-requiste courses.

            for p in preMap[c]:
                if not dfs(p): return False

            state[c] = 2 # now visited.
            
            # after succesful exploration
            res.append(c)
            return True
    
        for c in range(numCourses):
            if not dfs(c): return []
        
        return res
