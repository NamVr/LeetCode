class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # get total sum of both arrays individually.
        # update all zeros later to match the their sum.

        s1 = s2 = 0
        z1 = z2 = 0

        for i in nums1:
            s1 += i

            if i == 0:
                # add minimum 1 to sum, 0 -> 1
                s1 += 1
                z1 += 1

        for i in nums2:
            s2 += i

            if i == 0:
                # add minimum 1 to sum, 0 -> 1
                s2 += 1
                z2 += 1

        # Finally, check if there are zeros that can help mediate the overall sum.
        if (
            z1 == 0 and s2 > s1
        ) or (
            z2 == 0 and s1 > s2
        ):
            return -1
        
        # Else, we can match the overall sum to the max of both arrays.
        return max(s1,s2)
