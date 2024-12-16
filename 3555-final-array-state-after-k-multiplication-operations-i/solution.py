class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(val, i) for i, val in enumerate(nums)] # priority queue or min heap
        heapify(pq) # min heap done

        for _ in range(k):
            _, i = heappop(pq) # _ is val (not needed), i is index (needed)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))
        
        return nums
