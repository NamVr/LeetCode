class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap for choosing 2 heavy stones.
        # smash (stimulate) 2 popped stones and add x-y weight stone back.
        # do this till len(stones) == 1, return that value.

        stones = [-s for s in stones] # for max heap
        heapq.heapify(stones) # O(logn)

        while len(stones) > 1:

            # Stimulation: Pick 2 stones.
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
        
            # smash the stones, add the new stone.
            # edge case, both stones can have same weight.
            if x != y:
               heapq.heappush(stones, y-x) # negative value for max heap stimulation

        # edge case: last both stones are equal and smashed together.
        return abs(stones[0]) if len(stones) else 0
