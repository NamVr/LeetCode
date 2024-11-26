class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # keep track of all incoming vertices
        incoming = [0] * n

        for src, dst in edges:
            # set destination +1
            incoming[dst] += 1

        # now iterate through the incoming vertices
        champions = []
        for i, cnt in enumerate(incoming):
            # if incoming is zero, append it to a champion.
            if not cnt:
                champions.append(i)
        
        if len(champions) > 1:
            return -1
        return champions[0]

