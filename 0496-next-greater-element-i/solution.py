class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map all values to its indexes for ease of access later. O(N)
        numsToIdx = { n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1) # O(N) result array.

        stack = [] # create a monotonic stack.

        for i in range(len(nums2)): # O(M) traverse for all elements in bigger array.
            # keep monotonicity. get current element
            curr = nums2[i]

            # if the current element is bigger than the stack top, you have found your greatest element.
            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = numsToIdx[val]
                res[idx] = curr

            # finally, if this element exists in first array, then only update the stack.
            if nums2[i] in numsToIdx:
                stack.append(curr)

        return res
