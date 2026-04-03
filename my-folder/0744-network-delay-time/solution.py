class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)] # k is starting note.
        visit = set()
        t = 0 # create max value

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)
            t = max(t, weight)

            for nei_node, nei_weight in edges[node]:
                if nei_node not in visit:
                    heapq.heappush(minHeap, (weight + nei_weight, nei_node))

        return t if len(visit) == n else -1
