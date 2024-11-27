class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]

        def helper():
            q = deque()
            q.append((0,0)) # node, length

            visited = set()
            visited.add((0,0))

            while q: # while non empty
                cur, length = q.popleft()
                if cur == n-1:
                    return length
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append((nei, length+1))
                        visited.add(nei)

        res = []

        for src, des in queries:
            adj[src].append(des)
            res.append(helper())

        return res
