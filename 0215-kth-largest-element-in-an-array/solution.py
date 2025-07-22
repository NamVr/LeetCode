class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapify(nums) # O(n log n) min heap

        for _ in range(n-k):
            heappop(nums)
        
        return heappop(nums)
        
