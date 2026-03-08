class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        n = len(nums)

        for i in range(n):
            curr = nums[i][i] # the ith bit of ith element

            res.append("1" if curr == "0" else "0") # append 1 if current bit is 0 and vice versa
        
        return "".join(res)
