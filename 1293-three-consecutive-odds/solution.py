class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        check = 0

        for i in arr:
            if i % 2 == 1: # odd
                check += 1
            else:
                check = 0 # reset counter
        
            # check for 3 consecutive odds.
            if check == 3:
                return True
        
        return False
