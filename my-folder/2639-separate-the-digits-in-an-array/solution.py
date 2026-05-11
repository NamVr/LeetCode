class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            s = str(i)
            
            for c in s:
                res.append(int(c))
        
        return res
