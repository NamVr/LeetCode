class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # 1. Find the longest cycle
        # 2. Find sum of longest non closed circles
        
        N = len(favorite)
        longest_cycle = 0
        # major hashset for whole problem
        visit = [False] * N
        length_2_cycles = []

        for i in range(N):
            if visit[i]:
                continue
            
            # dont forget where we started
            start, cur = i, i
            cur_set = set()

            while not visit[cur]:
                visit[cur] = True
                cur_set.add(cur)
                cur = favorite[cur]
            
            if cur in cur_set:
                length = len(cur_set)
                while start != cur:
                    length -= 1
                    start = favorite[start]
                
                longest_cycle = max(longest_cycle, length)
                if length == 2:
                    length_2_cycles.append([cur, favorite[cur]])
                
        # step 2:
        inverted = defaultdict(list)
        for dst, src in enumerate(favorite):
            inverted[src].append(dst)
    
        def bfs(src, parent):
            # given source node
            q = deque([(src, 0)]) # node, length pairs
            max_length = 0

            while q:
                node, length = q.popleft()
                if node == parent:
                    continue
                max_length = max(max_length, length)

                for nei in inverted[node]:
                    q.append((nei, length+1))
            return max_length
        
        chain_sum = 0
        for n1, n2 in length_2_cycles:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chain_sum, longest_cycle)

