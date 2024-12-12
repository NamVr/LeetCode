class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # py has min heap so use - minus sign to simulate max heap
        h = [-g for g in gifts]
        heapq.heapify(h)

        for _ in range(k):
            maxElement = -heapq.heappop(h)

            heapq.heappush(h, -math.floor(math.sqrt(maxElement)))
        
        res = 0
        while h:
            # now use - to make it back positive
            res -= heapq.heappop(h)
        
        return res
