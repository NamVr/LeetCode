class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # create a final answer string
        res = []
        for i in range(len(nums)):
            curr = nums[i][i] # fetch the current index value
            res.append("1" if curr == "0" else "0") # flip the binary digit to create a new digit
        
        return "".join(res) # join the array
