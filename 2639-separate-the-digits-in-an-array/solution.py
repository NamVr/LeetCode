class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(b) for a in nums for b in str(a)]
        # for each a in nums -> for each b in string a
        # finally str of b --> int of a return using string comprehension
