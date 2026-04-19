class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 1

        while i < n1 and j < n2:
            # keep i as left as possible
            # keep j as right as possible
            if nums1[i] > nums2[j]:
                i += 1
            
            j += 1

        return j-i-1
