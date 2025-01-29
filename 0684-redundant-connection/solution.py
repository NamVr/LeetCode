class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find a cycle, remove the last redudant connection
        n = len(edges)

        # using union find parent array
        # ith node -> parent of i
        par = [i for i in range(n+1)]

        rank = [1] * (n+1)

        # path compression using union find
        # O(1) time
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n] # if statement is not executed -> return the parent

        def union(n1,n2):
            # find parents of both nodes
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False # same parent detected
            
            # now check rank
            if rank[p1] > rank[p2]:
                par[p2] = p1 # p1 has higher rank, so naturally P1 is now P2's parent
                rank[p1] += rank[p2] # increase P1's rank by adding rank of p1 + p2
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

