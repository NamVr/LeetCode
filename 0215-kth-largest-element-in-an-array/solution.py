class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)

        for i in range(k):
            heappush(heap, nums[i])
        
        for i in range(k,n):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        
        return heap[0]
