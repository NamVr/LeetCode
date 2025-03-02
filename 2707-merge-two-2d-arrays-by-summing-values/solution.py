class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = {} # hashmap for each id

        for i in nums1:
            m[i[0]] = i[1]
        
        for i in nums2:
            m[i[0]] = m.get(i[0], 0) + i[1]
        
        res = []

        for i, n in sorted(m.items()):
            res.append([i,n])
        return res
