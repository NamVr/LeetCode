class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = set() # use a set to store pairwise information

        for i in nums:
            if i in count:
                count.remove(i)
            else:
                count.add(i)
        
        return not count
