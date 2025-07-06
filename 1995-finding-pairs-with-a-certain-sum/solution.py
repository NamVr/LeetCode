class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.m = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.n2[index] # get the old value before addition
        self.m[old] -= 1 # decrement the counter for old value
        self.n2[index] += val
        self.m[self.n2[index]] += 1 # increment the counter for new value 

    def count(self, tot: int) -> int:
        res = 0
        for i in self.n1: # apply two sum
            res += self.m[tot-i]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
