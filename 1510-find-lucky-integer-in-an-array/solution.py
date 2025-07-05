class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        
        m = Counter(arr)
        
        for key, value in m.items():
            if key == value:
                res = max(res, key)

        return res
