class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        # xor results for both arrays
        xor1, xor2 = 0,0

        # if nums2 len is odd, each element in nums1 appear odd times in final result
        if n2 % 2:
            for num in nums1:
                xor1 ^= num
        if n1 % 2:
            for num in nums2:
                xor2 ^= num
        
        return xor1 ^ xor2
